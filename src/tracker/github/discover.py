"""Org/repo resolution, module proposals, path probing."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any

from tracker.config import (
    GeneratedModule,
    OrgSource,
    ProjectConfig,
    RepoSource,
    Tier,
    effective_tier,
    parse_proposals_dir,
)
from tracker.github.client import GitHubClient, GitHubError

PROPOSAL_CANDIDATES = [
    "docs/proposals",
    "proposals",
    "docs/rfcs",
    "rfcs",
    ".github/proposals",
    "docs/design-docs",
    "designs",
    "docs/designs",
]


@dataclass
class ResolvedRepo:
    full_name: str
    tier: Tier
    description: str | None = None
    default_branch: str | None = None
    is_archived: bool = False
    stars: int = 0
    pushed_at: str | None = None
    activity_90d: int = 0
    latest_release_tag: str | None = None
    latest_release_at: str | None = None
    modules: list[GeneratedModule] = field(default_factory=list)
    modules_source: str = "none"  # config|generated|none
    org_source: str | None = None


@dataclass
class ValidationFinding:
    level: str  # ok|warn|error
    subject: str
    message: str


def _split(full_name: str) -> tuple[str, str]:
    owner, name = full_name.split("/", 1)
    return owner, name


def _since_90d() -> str:
    dt = datetime.now(timezone.utc) - timedelta(days=90)
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def resolve_project_repos(
    client: GitHubClient,
    project: ProjectConfig,
    *,
    max_repos_per_org: int = 25,
    compute_activity: bool = True,
) -> tuple[list[ResolvedRepo], list[ValidationFinding]]:
    """Expand org + repo sources into a deduped ranked list."""
    findings: list[ValidationFinding] = []
    by_name: dict[str, ResolvedRepo] = {}
    # Track org-tier attribution for merges
    org_tier_for: dict[str, Tier | None] = {}
    since = _since_90d()

    for src in project.org_sources():
        try:
            nodes = client.list_org_repos(src.org)
            findings.append(
                ValidationFinding("ok", f"org:{src.org}", f"found {len(nodes)} repos")
            )
        except GitHubError as e:
            findings.append(
                ValidationFinding("error", f"org:{src.org}", str(e))
            )
            continue

        matched: list[dict[str, Any]] = []
        for node in nodes:
            short = node["name"]
            if src.skip_archived and node.get("isArchived"):
                continue
            if not src.matches(short):
                continue
            matched.append(node)

        scored: list[tuple[int, dict]] = []
        for node in matched:
            full = node["nameWithOwner"]
            activity = 0
            if compute_activity:
                owner, name = _split(full)
                try:
                    activity = client.count_merged_since(owner, name, since)
                except GitHubError:
                    activity = 0
            scored.append((activity, node))
        scored.sort(key=lambda x: (-x[0], x[1]["nameWithOwner"]))

        for idx, (activity, node) in enumerate(scored):
            full = node["nameWithOwner"]
            if idx >= max_repos_per_org:
                tier = Tier.OVERFLOW
            else:
                tier = effective_tier(
                    repo_tier=None,
                    org_tier=src.tier,
                    project_tier=project.tier,
                )
            org_tier_for[full] = src.tier
            existing = by_name.get(full)
            if existing and existing.tier == Tier.CORE:
                existing.activity_90d = max(existing.activity_90d, activity)
                continue
            by_name[full] = ResolvedRepo(
                full_name=full,
                tier=tier,
                description=node.get("description"),
                default_branch=((node.get("defaultBranchRef") or {}) or {}).get(
                    "name"
                ),
                is_archived=bool(node.get("isArchived")),
                stars=int(node.get("stargazerCount") or 0),
                pushed_at=node.get("pushedAt"),
                activity_90d=activity,
                org_source=src.org,
            )

    for src in project.repo_sources():
        owner, name = _split(src.repo)
        try:
            meta = client.get_repo(owner, name)
        except GitHubError as e:
            findings.append(
                ValidationFinding("error", f"repo:{src.repo}", str(e))
            )
            continue
        if meta is None:
            findings.append(
                ValidationFinding(
                    "error", f"repo:{src.repo}", "repository not found"
                )
            )
            continue
        findings.append(
            ValidationFinding("ok", f"repo:{src.repo}", "resolved")
        )
        activity = 0
        if compute_activity:
            try:
                activity = client.count_merged_since(owner, name, since)
            except GitHubError:
                activity = 0
        release = meta.get("latestRelease") or {}
        tier = effective_tier(
            repo_tier=src.tier,
            org_tier=org_tier_for.get(src.repo),
            project_tier=project.tier,
        )
        mods = [
            GeneratedModule(
                name=m.name, paths=m.paths, description=m.description
            )
            for m in src.modules
        ]
        by_name[src.repo] = ResolvedRepo(
            full_name=src.repo,
            tier=tier,
            description=meta.get("description"),
            default_branch=((meta.get("defaultBranchRef") or {}) or {}).get(
                "name"
            ),
            is_archived=bool(meta.get("isArchived")),
            stars=int(meta.get("stargazerCount") or 0),
            pushed_at=meta.get("pushedAt"),
            activity_90d=activity,
            latest_release_tag=release.get("tagName"),
            latest_release_at=release.get("publishedAt"),
            modules=mods,
            modules_source="config" if mods else "none",
        )

    repos = sorted(
        by_name.values(),
        key=lambda r: (
            {"core": 0, "watch": 1, "overflow": 2}[r.tier.value],
            -r.activity_90d,
            r.full_name,
        ),
    )
    return repos, findings


def parse_codeowners(text: str) -> list[tuple[str, list[str]]]:
    """Return (path_pattern, owners) pairs from CODEOWNERS content."""
    entries: list[tuple[str, list[str]]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        entries.append((parts[0], parts[1:]))
    return entries


def propose_modules(
    client: GitHubClient,
    full_name: str,
    *,
    codeowners_paths: list[str] | None = None,
    branch: str | None = None,
) -> list[GeneratedModule]:
    """Propose modules from top-level packages + CODEOWNERS groupings."""
    owner, name = _split(full_name)
    branch = branch or "HEAD"
    codeowners_paths = codeowners_paths or [
        ".github/CODEOWNERS",
        "CODEOWNERS",
    ]

    modules: dict[str, GeneratedModule] = {}

    # Top-level directories that look like packages
    entries = client.get_tree_entries(owner, name, "", branch=branch)
    package_dirs: list[str] = []
    for e in entries:
        if e.get("type") != "tree":
            continue
        dname = e["name"]
        if dname.startswith(".") or dname in {
            "docs",
            "tests",
            "test",
            "examples",
            "scripts",
            "ci",
            "build",
            "dist",
            "vendor",
            "node_modules",
            "third_party",
            "hack",
            "deploy",
            "chart",
            "charts",
            "site",
        }:
            continue
        package_dirs.append(dname)

    # Special-case Python monorepos: look under main package for v1/ etc.
    for pkg in list(package_dirs):
        sub = client.get_tree_entries(owner, name, pkg, branch=branch)
        for e in sub:
            if e.get("type") == "tree" and e["name"] in {"v1", "core", "engine"}:
                subpath = f"{pkg}/{e['name']}"
                # further one level for v1/*
                if e["name"] == "v1":
                    v1 = client.get_tree_entries(
                        owner, name, subpath, branch=branch
                    )
                    for ve in v1:
                        if ve.get("type") == "tree":
                            path = f"{subpath}/{ve['name']}/**"
                            mod_name = f"{pkg}-v1-{ve['name']}"
                            modules[mod_name] = GeneratedModule(
                                name=mod_name, paths=[path]
                            )
                else:
                    mod_name = f"{pkg}-{e['name']}"
                    modules[mod_name] = GeneratedModule(
                        name=mod_name, paths=[f"{subpath}/**"]
                    )

    for dname in package_dirs:
        if dname not in {m.name.split("-")[0] for m in modules.values()} or True:
            key = dname
            if key not in modules:
                modules[key] = GeneratedModule(
                    name=key, paths=[f"{dname}/**"]
                )

    # CODEOWNERS groupings
    for path in codeowners_paths:
        text = client.get_file_text(owner, name, path, branch=branch)
        if not text:
            continue
        for pattern, _owners in parse_codeowners(text):
            clean = pattern.lstrip("/")
            if clean in {"*", "**", ""}:
                continue
            # derive module name from first path segment(s)
            parts = re.split(r"[/*]+", clean)
            parts = [p for p in parts if p and p != "**"]
            if not parts:
                continue
            mod_name = "-".join(parts[:3])
            glob = clean if clean.endswith("*") else f"{clean.rstrip('/')}/**"
            if mod_name not in modules:
                modules[mod_name] = GeneratedModule(
                    name=mod_name, paths=[glob]
                )
            elif glob not in modules[mod_name].paths:
                modules[mod_name].paths.append(glob)

    return sorted(modules.values(), key=lambda m: m.name)


def probe_proposals_dir(
    client: GitHubClient, entry: str, default_repo: str | None = None
) -> tuple[str | None, str | None, list[ValidationFinding]]:
    """Resolve proposals_dirs entry. Returns (full_name, path, findings)."""
    findings: list[ValidationFinding] = []
    full, path = parse_proposals_dir(entry)
    full = full or default_repo
    if not full:
        findings.append(
            ValidationFinding(
                "warn",
                f"proposals:{entry}",
                "no repo specified and no default",
            )
        )
        return None, None, findings

    owner, name = _split(full)
    if path == "<discover>" or path.endswith(":<discover>"):
        found: list[str] = []
        for candidate in PROPOSAL_CANDIDATES:
            try:
                if client.path_exists(owner, name, candidate):
                    found.append(candidate)
            except GitHubError as e:
                findings.append(
                    ValidationFinding(
                        "warn", f"proposals:{full}:{candidate}", str(e)
                    )
                )
        if found:
            findings.append(
                ValidationFinding(
                    "ok",
                    f"proposals:{full}",
                    f"discovered: {', '.join(found)} (suggested: {found[0]})",
                )
            )
            return full, found[0], findings
        findings.append(
            ValidationFinding(
                "warn",
                f"proposals:{full}",
                f"no candidates found among {PROPOSAL_CANDIDATES}",
            )
        )
        return full, None, findings

    try:
        exists = client.path_exists(owner, name, path)
    except GitHubError as e:
        findings.append(
            ValidationFinding("error", f"proposals:{full}:{path}", str(e))
        )
        return full, None, findings
    if exists:
        findings.append(
            ValidationFinding("ok", f"proposals:{full}:{path}", "resolved")
        )
        return full, path, findings
    findings.append(
        ValidationFinding(
            "warn", f"proposals:{full}:{path}", "path not found"
        )
    )
    return full, None, findings


def validate_codeowners(
    client: GitHubClient,
    full_name: str,
    paths: list[str],
    branch: str | None = None,
) -> list[ValidationFinding]:
    owner, name = _split(full_name)
    findings: list[ValidationFinding] = []
    found_any = False
    for path in paths:
        try:
            ok = client.path_exists(owner, name, path, branch=branch or "HEAD")
        except GitHubError as e:
            findings.append(
                ValidationFinding("warn", f"codeowners:{full_name}:{path}", str(e))
            )
            continue
        if ok:
            findings.append(
                ValidationFinding(
                    "ok", f"codeowners:{full_name}:{path}", "resolved"
                )
            )
            found_any = True
        else:
            findings.append(
                ValidationFinding(
                    "warn",
                    f"codeowners:{full_name}:{path}",
                    "path not found",
                )
            )
    if not found_any and paths:
        findings.append(
            ValidationFinding(
                "warn",
                f"codeowners:{full_name}",
                "no CODEOWNERS file resolved",
            )
        )
    return findings

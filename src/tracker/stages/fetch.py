"""Deterministic GitHub → SQLite ingest."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from typing import Any

from rich.console import Console

from tracker.config import (
    ProjectConfig,
    RootConfig,
    load_generated_modules,
    parse_proposals_dir,
)
from tracker.db import Database
from tracker.github.client import GitHubClient
from tracker.github.discover import (
    parse_codeowners,
    probe_proposals_dir,
    propose_modules,
    resolve_project_repos,
)
from tracker.paths import modules_generated
from tracker.util import parse_since, to_iso

console = Console()


def _signal_for_issue(
    title: str, labels: list[str], project: ProjectConfig
) -> str | None:
    sigs = project.pipeline_signals
    for prefix in sigs.issue_title_prefixes:
        if title.startswith(prefix) or prefix.lower() in title.lower():
            if "roadmap" in prefix.lower() or "roadmap" in title.lower():
                return "roadmap"
            return "rfc"
    label_set = {l.lower() for l in labels}
    for lab in sigs.labels:
        if lab.lower() in label_set:
            if "roadmap" in lab.lower():
                return "roadmap"
            return "rfc"
    if any("rfc" in l.lower() for l in labels) or "[rfc]" in title.lower():
        return "rfc"
    if "roadmap" in title.lower():
        return "roadmap"
    return None


def fetch_project(
    client: GitHubClient,
    db: Database,
    config: RootConfig,
    project_name: str,
    *,
    since: str | None = None,
    workspace=None,
) -> dict[str, Any]:
    project = config.get_project(project_name)
    since_str = since or config.settings.default_since
    since_dt = parse_since(since_str)
    # Also pull a bit more history for activity baselines
    lookback = min(since_dt, datetime.now(timezone.utc) - timedelta(days=90))
    since_iso = to_iso(lookback)

    run_id = db.start_run("fetch", project_name, since=since_str)
    stats: dict[str, Any] = {
        "repos": 0,
        "prs": 0,
        "issues": 0,
        "releases": 0,
        "proposals": 0,
    }

    try:
        repos, findings = resolve_project_repos(
            client,
            project,
            max_repos_per_org=config.settings.max_repos_per_org,
            compute_activity=True,
        )
        for f in findings:
            style = {"ok": "green", "warn": "yellow", "error": "red"}[f.level]
            console.print(f"[{style}]{f.level}[/{style}] {f.subject}: {f.message}")

        generated = load_generated_modules(modules_generated(workspace))
        gen_for_project = generated.projects.get(project_name, {})

        for repo in repos:
            if repo.tier.value == "overflow":
                db.upsert_repo(
                    project_name,
                    repo.full_name,
                    repo.tier.value,
                    description=repo.description,
                    default_branch=repo.default_branch,
                    is_archived=repo.is_archived,
                    stars=repo.stars,
                    pushed_at=repo.pushed_at,
                    activity_90d=repo.activity_90d,
                )
                stats["repos"] += 1
                continue

            console.print(f"[cyan]fetch[/cyan] {repo.full_name} ({repo.tier.value})")
            owner, name = repo.full_name.split("/", 1)

            # Enrich release metadata if missing
            if not repo.latest_release_tag:
                meta = client.get_repo(owner, name)
                if meta and meta.get("latestRelease"):
                    rel = meta["latestRelease"]
                    repo.latest_release_tag = rel.get("tagName")
                    repo.latest_release_at = rel.get("publishedAt")

            repo_id = db.upsert_repo(
                project_name,
                repo.full_name,
                repo.tier.value,
                description=repo.description,
                default_branch=repo.default_branch,
                is_archived=repo.is_archived,
                stars=repo.stars,
                pushed_at=repo.pushed_at,
                latest_release_tag=repo.latest_release_tag,
                latest_release_at=repo.latest_release_at,
                activity_90d=repo.activity_90d,
            )
            stats["repos"] += 1

            # Modules
            modules = list(repo.modules)
            source = repo.modules_source
            if not modules and repo.full_name in gen_for_project:
                modules = gen_for_project[repo.full_name]
                source = "generated"
            if not modules and repo.tier.value == "core":
                modules = propose_modules(
                    client,
                    repo.full_name,
                    codeowners_paths=project.people_signals.codeowners,
                    branch=repo.default_branch or "HEAD",
                )
                source = "generated"
            if modules:
                db.replace_modules(
                    repo_id,
                    [
                        {
                            "name": m.name,
                            "paths": m.paths,
                            "source": source,
                        }
                        for m in modules
                    ],
                )

            # Releases
            for rel in client.list_releases(owner, name):
                if rel.get("published_at") and rel["published_at"] < since_iso:
                    # still store recent-ish; skip very old after first page naturally
                    pass
                db.upsert_release(
                    repo_id,
                    rel["tag"],
                    name=rel.get("name"),
                    body=rel.get("body"),
                    published_at=rel.get("published_at"),
                    url=rel.get("url"),
                )
                stats["releases"] += 1
            db.commit()

            # Merged PRs
            for pr in client.iter_merged_prs(
                owner, name, since_iso=since_iso
            ):
                db.upsert_pr(repo_id, pr)
                stats["prs"] += 1
            # Open PRs (for pipeline)
            for pr in client.iter_open_prs(owner, name):
                db.upsert_pr(repo_id, pr)
                stats["prs"] += 1
            db.commit()

            # Issues (signal-tagged)
            for issue in client.iter_issues(
                owner, name, since_iso=since_iso
            ):
                signal = _signal_for_issue(
                    issue["title"], issue.get("labels") or [], project
                )
                issue["signal"] = signal
                # Keep RFCs/roadmaps even if older signal match; skip noise without signal for closed old
                if signal or issue["state"] == "OPEN":
                    db.upsert_issue(repo_id, issue)
                    stats["issues"] += 1
            db.commit()

            # CODEOWNERS → ownership
            ownership_entries: list[dict[str, Any]] = []
            for path in project.people_signals.codeowners:
                text = client.get_file_text(
                    owner, name, path, branch=repo.default_branch or "HEAD"
                )
                if not text:
                    continue
                for pattern, owners in parse_codeowners(text):
                    ownership_entries.append(
                        {
                            "module_id": None,
                            "path_pattern": pattern,
                            "owners": owners,
                            "source": "codeowners",
                        }
                    )
            if ownership_entries:
                db.replace_ownership(repo_id, ownership_entries)

            db.set_sync(f"{project_name}:{repo.full_name}:fetched", to_iso(
                datetime.now(timezone.utc)
            ))

        # Proposals dirs
        default_repo = next(
            (r.full_name for r in repos if r.tier.value == "core"),
            repos[0].full_name if repos else None,
        )
        for entry in project.pipeline_signals.proposals_dirs:
            full, path, pfindings = probe_proposals_dir(
                client, entry, default_repo=default_repo
            )
            for f in pfindings:
                style = {"ok": "green", "warn": "yellow", "error": "red"}[f.level]
                console.print(
                    f"[{style}]{f.level}[/{style}] {f.subject}: {f.message}"
                )
            if not full or not path:
                continue
            owner, name = full.split("/", 1)
            repo_id = db.get_repo_id(project_name, full)
            if repo_id is None:
                continue
            files = client.list_dir_files(owner, name, path)
            for item in files:
                if item.get("type") == "file":
                    db.upsert_proposal_file(
                        repo_id,
                        item["path"],
                        sha=item.get("sha"),
                        url=item.get("url"),
                    )
                    stats["proposals"] += 1
            db.commit()

        db.finish_run(run_id, "ok", stats)
    except Exception as e:
        db.finish_run(run_id, "error", {**stats, "error": str(e)})
        raise

    return stats

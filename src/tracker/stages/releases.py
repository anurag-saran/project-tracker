"""Release feature lists (shipped) + next community release (planned)."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rich.console import Console

from tracker.config import RootConfig
from tracker.db import Database
from tracker.github.client import GitHubClient, GitHubError
from tracker.llm import get_provider
from tracker.llm.base import LLMProvider, UsageTracker
from tracker.paths import reports_dir
from tracker.prompts_loader import load_prompt
from tracker.render.markdown import render
from tracker.stages.rollup import publish_latest
from tracker.util import content_hash, to_iso, trim_body

console = Console()

_BULLET_RE = re.compile(r"^\s*[-*+]\s+(.+)$")
_HEADING_RE = re.compile(r"^#{1,3}\s+(.+)$")
_FEATURE_HEAD = re.compile(
    r"feature|highlight|what.?s new|tl;?dr|new model|improvement|enhancement|"
    r"announcement|notable|added|changelog",
    re.I,
)
_SKIP_HEAD = re.compile(
    r"fix|bug|chore|ci|doc|dependenc|contributor|thank|before you upgrade|"
    r"breaking|new contributors|installation|python|docker|helm|upgrade",
    re.I,
)
_NOISE_BULLET = re.compile(
    r"^(chore|fix|ci|docs?|test|build|refactor|style|perf)\b|"
    r"dependabot|first contribution|made their first contribution|"
    r"^bump |\(@dependabot",
    re.I,
)
_FEAT_BULLET = re.compile(
    r"^\*\*[^*]+\*\*|^feat\b|^add(?:ed|s)?\b|^new\b|^support\b|^introduce",
    re.I,
)
_BLOG_LINK = re.compile(
    r"\[([^\]]*(?:blog|release notes?|announcement)[^\]]*)\]\((https?://[^)]+)\)",
    re.I,
)


def _is_noise_bullet(text: str) -> bool:
    return bool(_NOISE_BULLET.search(text))


def extract_feature_bullets(body: str | None, *, limit: int = 20) -> list[str]:
    """Pull feature-ish bullets from GitHub release notes markdown."""
    if not body:
        return []
    lines = body.splitlines()
    features: list[str] = []
    in_feature_section = False
    saw_any_heading = False

    # Prefer an explicit release-blog link when notes are thin (common for vSR).
    for m in _BLOG_LINK.finditer(body):
        label = re.sub(r"\s+", " ", m.group(1)).strip() or "Release blog"
        features.append(f"**Release blog:** [{label}]({m.group(2)})")
        break

    for line in lines:
        hm = _HEADING_RE.match(line.strip())
        if hm:
            saw_any_heading = True
            title = hm.group(1).strip()
            if _FEATURE_HEAD.search(title):
                in_feature_section = True
            elif _SKIP_HEAD.search(title):
                in_feature_section = False
            else:
                # Keep collecting under ambiguous headings if we already started
                in_feature_section = in_feature_section or not features
            continue
        bm = _BULLET_RE.match(line)
        if not bm:
            continue
        text = bm.group(1).strip()
        text = re.sub(r"\s+", " ", text)
        if len(text) < 8 or _is_noise_bullet(text):
            continue
        if saw_any_heading and not in_feature_section and features:
            # Still accept clearly feature-shaped bullets outside sections
            if not _FEAT_BULLET.search(text):
                continue
        if saw_any_heading and not in_feature_section and _SKIP_HEAD.search(text):
            continue
        features.append(text)
        if len(features) >= limit:
            break

    if len(features) <= 1:
        # Fallback: prefer feat-shaped bullets, skip chore/contributor noise
        ranked: list[str] = []
        for line in lines:
            bm = _BULLET_RE.match(line)
            if not bm:
                continue
            text = re.sub(r"\s+", " ", bm.group(1).strip())
            if len(text) < 8 or _is_noise_bullet(text):
                continue
            if _FEAT_BULLET.search(text):
                ranked.insert(0, text)
            else:
                ranked.append(text)
            if len(ranked) >= min(limit, 12):
                break
        for text in ranked:
            if text not in features:
                features.append(text)
            if len(features) >= limit:
                break
    return features[:limit]


def _summarize_release(
    llm: LLMProvider,
    usage: UsageTracker,
    db: Database,
    *,
    system: str,
    project: str,
    repo: str,
    tag: str,
    body: str | None,
    bullets: list[str],
    dry_run: bool,
) -> list[str]:
    """Return brief feature descriptions (reuse bullets if dry/null)."""
    if not body and not bullets:
        return []
    source_hash = content_hash(repo, tag, body or "", bullets)
    subject = f"{project}/release/{repo}/{tag}"
    cached = db.get_summary("release_features", subject, source_hash)
    if cached:
        return [ln[2:].strip() for ln in cached.splitlines() if ln.startswith("- ")]

    if dry_run or llm.name == "null" or not body:
        return bullets[:15]

    user = (
        f"Project: {project}\nRepo: {repo}\nRelease: {tag}\n\n"
        f"Release notes (trimmed):\n{trim_body(body, 3500)}\n\n"
        "Extract the user-facing features / highlights as a markdown bullet list. "
        "Each bullet: short feature name — one-sentence description. "
        "Skip pure bugfixes, chores, and contributor shout-outs. Max 12 bullets."
    )
    result = llm.complete(system, user)
    usage.add(result)
    out = []
    for ln in (result.text or "").splitlines():
        s = ln.strip()
        if s.startswith("- "):
            out.append(s[2:].strip())
        elif s.startswith("* "):
            out.append(s[2:].strip())
    if not out:
        out = bullets[:15]
    db.save_summary(
        "release_features",
        subject,
        source_hash,
        "\n".join(f"- {b}" for b in out),
        model=result.model,
        tokens_in=result.tokens_in,
        tokens_out=result.tokens_out,
    )
    return out


def _is_stable_release(tag: str) -> bool:
    t = tag.lower()
    if "rc" in t or "alpha" in t or "beta" in t or "dev" in t:
        return False
    return bool(re.search(r"v?\d+\.\d+", t))


def build_releases(
    db: Database,
    config: RootConfig,
    project_name: str,
    *,
    client: GitHubClient | None = None,
    dry_run: bool = False,
    workspace: Path | None = None,
    llm: LLMProvider | None = None,
    release_limit: int = 6,
) -> Path:
    project = config.get_project(project_name)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if llm is None:
        if dry_run:
            llm = get_provider("null")
        else:
            try:
                llm = get_provider()
            except Exception as e:
                console.print(f"[yellow]LLM unavailable ({e}); using null[/yellow]")
                llm = get_provider("null")

    usage = UsageTracker()
    try:
        system = load_prompt("releases", workspace)
    except FileNotFoundError:
        system = (
            "Extract user-facing features from release notes as short bullets "
            "with one-sentence descriptions."
        )

    run_id = db.start_run("releases", project_name)
    repos_out: list[dict[str, Any]] = []
    tldr: list[str] = []

    try:
        # Ensure explicit core repo sources exist even before a full fetch.
        for src in project.repo_sources():
            db.upsert_repo(
                project_name,
                src.repo,
                (src.tier.value if src.tier else "core"),
            )

        for repo_row in db.list_repos(project_name):
            if repo_row["tier"] not in ("core", "watch"):
                continue
            # Prefer core; include watch only if they have releases stored
            repo_id = repo_row["id"]
            full = repo_row["full_name"]
            owner, name = full.split("/", 1)

            # Refresh releases + milestones when client available
            milestones: list[dict[str, Any]] = []
            if client is not None:
                try:
                    for rel in client.list_releases(owner, name, max_pages=2):
                        db.upsert_release(
                            repo_id,
                            rel["tag"],
                            name=rel.get("name"),
                            body=rel.get("body"),
                            published_at=rel.get("published_at"),
                            url=rel.get("url"),
                        )
                    db.commit()
                    milestones = client.list_milestones(owner, name)
                except GitHubError as e:
                    console.print(f"[yellow]warn[/yellow] {full}: {e}")

            releases = db.list_releases(repo_id, limit=release_limit * 2)
            shipped: list[dict[str, Any]] = []
            upcoming_rcs: list[dict[str, Any]] = []

            for rel in releases:
                tag = rel["tag"] or ""
                bullets = extract_feature_bullets(rel["body"])
                features = _summarize_release(
                    llm,
                    usage,
                    db,
                    system=system,
                    project=project_name,
                    repo=full,
                    tag=tag,
                    body=rel["body"],
                    bullets=bullets,
                    dry_run=dry_run,
                )
                entry = {
                    "tag": tag,
                    "name": rel["name"] or tag,
                    "url": rel["url"],
                    "published_at": rel["published_at"],
                    "features": features,
                    "is_prerelease": not _is_stable_release(tag),
                }
                if _is_stable_release(tag):
                    shipped.append(entry)
                else:
                    upcoming_rcs.append(entry)
                if len(shipped) >= release_limit:
                    break

            # Planned: milestones + roadmap issues + open RFCs (top)
            planned_items: list[dict[str, Any]] = []
            for m in milestones[:5]:
                planned_items.append(
                    {
                        "kind": "milestone",
                        "title": m["title"],
                        "url": m["url"],
                        "detail": (
                            f"due {m['due_on'][:10] if m.get('due_on') else 'TBD'} · "
                            f"{m.get('closed_issues', 0)}/{(m.get('open_issues', 0) or 0) + (m.get('closed_issues', 0) or 0)} issues closed · "
                            f"{m.get('open_prs', 0)} open PRs"
                        ),
                        "summary": trim_body(m.get("description"), 240),
                    }
                )

            for issue in db.list_issues_by_signal(repo_id, signal="roadmap", state="OPEN")[
                :8
            ]:
                planned_items.append(
                    {
                        "kind": "roadmap",
                        "title": f"#{issue['number']} {issue['title']}",
                        "url": issue["url"],
                        "detail": "roadmap",
                        "summary": trim_body(issue["body"], 200),
                    }
                )

            for issue in db.list_issues_by_signal(repo_id, signal="rfc", state="OPEN")[:8]:
                planned_items.append(
                    {
                        "kind": "rfc",
                        "title": f"#{issue['number']} {issue['title']}",
                        "url": issue["url"],
                        "detail": "open RFC/proposal",
                        "summary": trim_body(issue["body"], 200),
                    }
                )

            if not shipped and not upcoming_rcs and not planned_items:
                if repo_row["tier"] != "core":
                    continue

            if shipped:
                latest = shipped[0]
                tldr.append(
                    f"{full} {latest['tag']}: {len(latest['features'])} feature(s)"
                )
            if upcoming_rcs:
                tldr.append(
                    f"{full} next RC/train: {upcoming_rcs[0]['tag']}"
                )
            elif milestones:
                tldr.append(f"{full} next milestone: {milestones[0]['title']}")

            docs = project.docs_urls
            repos_out.append(
                {
                    "full_name": full,
                    "tier": repo_row["tier"],
                    "docs_urls": docs if repo_row["tier"] == "core" else [],
                    "release_url": f"https://github.com/{full}/releases",
                    "shipped": shipped,
                    "upcoming_rcs": upcoming_rcs[:3],
                    "planned": planned_items[:20],
                }
            )

        md = render(
            "releases.md.j2",
            project=project_name,
            date=today,
            generated_at=to_iso(datetime.now(timezone.utc)),
            tldr=tldr[:8],
            repos=repos_out,
            docs_urls=project.docs_urls,
        )
        out_dir = reports_dir(workspace) / project_name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{today}-releases.md"
        out_path.write_text(md)
        publish_latest(out_path, "releases")
        db.finish_run(
            run_id,
            "ok",
            {"path": str(out_path), "repos": len(repos_out), **usage.summary()},
        )
        console.print(f"[green]Wrote[/green] {out_path}")
        return out_path
    except Exception as e:
        db.finish_run(run_id, "error", {"error": str(e)})
        raise

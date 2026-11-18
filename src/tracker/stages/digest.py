"""Change digest: map PRs to modules, LLM summarize, write markdown."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rich.console import Console

from tracker.config import RootConfig, load_overrides
from tracker.db import Database
from tracker.llm import get_provider
from tracker.llm.base import LLMProvider, UsageTracker
from tracker.paths import overrides_dir, reports_dir
from tracker.prompts_loader import load_prompt
from tracker.render.markdown import render
from tracker.util import (
    classify_pr,
    content_hash,
    match_paths,
    parse_since,
    to_iso,
    trim_body,
)

console = Console()


def _pr_files(row) -> list[str]:
    try:
        return [f["path"] for f in json.loads(row["files_json"] or "[]")]
    except (json.JSONDecodeError, TypeError, KeyError):
        return []


def _pr_labels(row) -> list[str]:
    try:
        return json.loads(row["labels_json"] or "[]")
    except json.JSONDecodeError:
        return []


def _map_pr_to_modules(
    files: list[str], modules: list[tuple[str, list[str]]]
) -> list[str]:
    hit = []
    for name, paths in modules:
        if match_paths(files, paths):
            hit.append(name)
    return hit or ["_ungrouped"]


# Keep prompts inside smaller OpenAI-compatible context windows (e.g. ~40k).
_MAX_PRS_PER_MODULE = 35
_MAX_PROMPT_CHARS = 48_000


def _format_pr_line(row) -> str:
    labels = _pr_labels(row)
    lab = f" [{', '.join(labels)}]" if labels else ""
    files = _pr_files(row)[:8]
    file_note = f" files: {', '.join(files)}" if files else ""
    return (
        f"- #{row['number']} {row['title']}{lab} "
        f"(+{row['additions'] or 0}/-{row['deletions'] or 0}) "
        f"by @{row['author'] or '?'}{file_note}\n"
        f"  {trim_body(row['body'], 180)}"
    )


def _select_prs_for_prompt(prs: list) -> list:
    """Prefer largest / newest PRs so the model sees the important changes."""
    ranked = sorted(
        prs,
        key=lambda p: (
            (p["additions"] or 0) + (p["deletions"] or 0),
            p["merged_at"] or "",
        ),
        reverse=True,
    )
    return ranked[:_MAX_PRS_PER_MODULE]


def _summarize_module(
    llm: LLMProvider,
    usage: UsageTracker,
    db: Database,
    *,
    system: str,
    project: str,
    repo: str,
    module: str,
    prs: list,
    dry_run: bool,
) -> str:
    if not prs:
        return "_No merged PRs in this period._"

    # Grounded fallback grouping without LLM claims invention
    buckets: dict[str, list] = defaultdict(list)
    for pr in prs:
        buckets[classify_pr(pr["title"], _pr_labels(pr), pr["body"])].append(pr)

    prompt_prs = _select_prs_for_prompt(prs)
    user_parts = [
        f"Project: {project}",
        f"Repo: {repo}",
        f"Module: {module}",
        f"PR count: {len(prs)} (showing {len(prompt_prs)} for summarization)",
        "",
        "Pull requests:",
    ]
    for pr in prompt_prs:
        user_parts.append(_format_pr_line(pr))
        if sum(len(p) for p in user_parts) >= _MAX_PROMPT_CHARS:
            user_parts.append(
                f"\n… truncated; {len(prs) - len(prompt_prs)} additional PRs omitted."
            )
            break
    user = "\n".join(user_parts)
    source_hash = content_hash(
        [dict(p) if hasattr(p, "keys") else p for p in prs]
    )
    subject = f"{project}/{repo}/{module}"

    cached = db.get_summary("digest_module", subject, source_hash)
    if cached:
        return cached

    if dry_run:
        # Deterministic structured list
        sections = []
        for key in ("breaking", "features", "performance", "fixes", "infra"):
            items = buckets.get(key) or []
            if not items:
                continue
            sections.append(f"**{key.title()}**")
            for pr in items:
                sections.append(f"- {pr['title']} (#{pr['number']})")
        text = "\n".join(sections) or "\n".join(
            f"- {p['title']} (#{p['number']})" for p in prs
        )
        return text

    result = llm.complete(system, user)
    usage.add(result)
    # Ensure PR refs exist; if model returned empty, fall back
    text = result.text.strip()
    if not text:
        text = "\n".join(f"- {p['title']} (#{p['number']})" for p in prs)
    db.save_summary(
        "digest_module",
        subject,
        source_hash,
        text,
        model=result.model,
        tokens_in=result.tokens_in,
        tokens_out=result.tokens_out,
    )
    return text


def build_digest(
    db: Database,
    config: RootConfig,
    project_name: str,
    *,
    since: str | None = None,
    dry_run: bool = False,
    workspace: Path | None = None,
    llm: LLMProvider | None = None,
) -> Path:
    project = config.get_project(project_name)
    since_str = since or config.settings.default_since
    since_dt = parse_since(since_str)
    since_iso = to_iso(since_dt)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if llm is None:
        if dry_run:
            llm = get_provider("null")
        else:
            try:
                llm = get_provider()
            except Exception as e:
                console.print(f"[yellow]LLM unavailable ({e}); using null provider[/yellow]")
                llm = get_provider("null")

    usage = UsageTracker()
    system = load_prompt("digest", workspace)
    run_id = db.start_run("digest", project_name, since=since_str)

    repos_out: list[dict[str, Any]] = []
    tldr_candidates: list[str] = []
    known_authors: dict[str, set[str]] = defaultdict(set)

    try:
        for repo_row in db.list_repos(project_name):
            if repo_row["tier"] == "overflow":
                continue
            repo_id = repo_row["id"]
            full = repo_row["full_name"]

            modules_rows = db.list_modules(repo_id)
            module_defs = [
                (m["name"], json.loads(m["paths_json"])) for m in modules_rows
            ]

            prs = db.list_merged_prs_since(repo_id, since_iso)
            releases = db.list_releases_since(repo_id, since_iso)

            # Historical authors before period (approx: all stored merged PRs earlier)
            prior = db.execute(
                "SELECT DISTINCT author FROM pull_requests WHERE repo_id=? AND state='MERGED' "
                "AND merged_at IS NOT NULL AND merged_at < ? AND author IS NOT NULL",
                (repo_id, since_iso),
            ).fetchall()
            prior_authors = {r["author"] for r in prior}

            by_module: dict[str, list] = defaultdict(list)
            for pr in prs:
                files = _pr_files(pr)
                for mod in _map_pr_to_modules(files, module_defs):
                    by_module[mod].append(pr)

            module_out = []
            for mod_name, mod_prs in sorted(by_module.items()):
                if mod_name == "_ungrouped" and module_defs:
                    # keep for ungrouped_summary
                    continue
                if mod_name == "_ungrouped":
                    continue
                summary = _summarize_module(
                    llm,
                    usage,
                    db,
                    system=system,
                    project=project_name,
                    repo=full,
                    module=mod_name,
                    prs=mod_prs,
                    dry_run=dry_run,
                )
                first_timers = sorted(
                    {
                        p["author"]
                        for p in mod_prs
                        if p["author"] and p["author"] not in prior_authors
                    }
                )
                module_out.append(
                    {
                        "name": mod_name,
                        "summary": summary,
                        "first_timers": first_timers,
                    }
                )
                if mod_prs:
                    tldr_candidates.append(
                        f"{full}/{mod_name}: {len(mod_prs)} PRs merged"
                    )

            ungrouped = by_module.get("_ungrouped") or []
            ungrouped_summary = None
            if ungrouped:
                ungrouped_summary = _summarize_module(
                    llm,
                    usage,
                    db,
                    system=system,
                    project=project_name,
                    repo=full,
                    module="_ungrouped",
                    prs=ungrouped,
                    dry_run=dry_run,
                )

            highlights = []
            for rel in releases:
                highlights.append(
                    f"New release **{rel['tag']}**"
                    + (f" — {rel['name']}" if rel["name"] else "")
                )
                tldr_candidates.insert(
                    0, f"Release {full}@{rel['tag']}"
                )
            for pr in prs:
                labels = [l.lower() for l in _pr_labels(pr)]
                title_l = (pr["title"] or "").lower()
                if any("break" in l for l in labels) or "breaking" in title_l:
                    highlights.append(
                        f"Breaking: #{pr['number']} {pr['title']}"
                    )

            if prs or releases or module_out or ungrouped_summary:
                repos_out.append(
                    {
                        "full_name": full,
                        "tier": repo_row["tier"],
                        "releases": [
                            {
                                "tag": r["tag"],
                                "name": r["name"],
                                "url": r["url"],
                                "published_at": r["published_at"],
                            }
                            for r in releases
                        ],
                        "modules": module_out,
                        "ungrouped_summary": ungrouped_summary,
                        "highlights": highlights,
                    }
                )

        tldr = tldr_candidates[:5]
        md = render(
            "digest.md.j2",
            project=project_name,
            date=today,
            since=since_str,
            generated_at=to_iso(datetime.now(timezone.utc)),
            tldr=tldr,
            repos=repos_out,
        )

        out_dir = reports_dir(workspace) / project_name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{today}-digest.md"
        out_path.write_text(md)
        from tracker.stages.rollup import publish_latest

        latest = publish_latest(out_path, "digest")

        db.finish_run(
            run_id,
            "ok",
            {"path": str(out_path), "latest": str(latest), **usage.summary()},
        )
        console.print(
            f"[green]Wrote[/green] {out_path} · "
            f"tokens in/out={usage.tokens_in}/{usage.tokens_out} · "
            f"est. ${usage.cost_usd:.4f}"
        )
        return out_path
    except Exception as e:
        db.finish_run(run_id, "error", {"error": str(e), **usage.summary()})
        raise

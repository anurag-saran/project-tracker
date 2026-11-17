"""Pipeline: RFCs, proposals, significant PRs, roadmap checklists."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rich.console import Console

from tracker.config import RootConfig
from tracker.db import Database
from tracker.llm import get_provider
from tracker.llm.base import LLMProvider, UsageTracker
from tracker.paths import reports_dir
from tracker.prompts_loader import load_prompt
from tracker.render.markdown import render
from tracker.util import match_paths, parse_since, to_iso, trim_body

console = Console()

CHECKBOX_RE = re.compile(r"^\s*[-*]\s*\[([ xX])\]\s+(.*)$", re.MULTILINE)


def _labels(row) -> list[str]:
    try:
        return json.loads(row["labels_json"] or "[]")
    except json.JSONDecodeError:
        return []


def _files(row) -> list[str]:
    try:
        return [f["path"] for f in json.loads(row["files_json"] or "[]")]
    except (json.JSONDecodeError, TypeError, KeyError):
        return []


def _age_days(created_at: str | None) -> int:
    if not created_at:
        return 0
    try:
        dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - dt).days)
    except ValueError:
        return 0


def _parse_checklist(body: str | None) -> list[dict[str, Any]]:
    if not body:
        return []
    items = []
    for m in CHECKBOX_RE.finditer(body):
        items.append(
            {"done": m.group(1).lower() == "x", "text": m.group(2).strip()}
        )
    return items


def _is_significant(
    pr, project_cfg, module_paths: list[list[str]]
) -> bool:
    sig = project_cfg.pipeline_signals.significant_pr
    labels = {l.lower() for l in _labels(pr)}
    if any(l.lower() in labels for l in sig.labels):
        return True
    if sig.min_files and (pr["changed_files"] or 0) >= sig.min_files:
        return True
    if sig.min_additions and (pr["additions"] or 0) >= sig.min_additions:
        return True
    # defaults if nothing configured
    if not sig.labels and sig.min_files is None and sig.min_additions is None:
        if (pr["changed_files"] or 0) >= 25 or (pr["additions"] or 0) >= 500:
            return True
        if any("rfc" in l or "breaking" in l for l in labels):
            return True
    files = _files(pr)
    for paths in module_paths:
        if match_paths(files, paths):
            if (pr["changed_files"] or 0) >= 15 or (pr["additions"] or 0) >= 300:
                return True
    # high review activity proxy
    return False


def _one_liner(
    llm: LLMProvider,
    usage: UsageTracker,
    system: str,
    title: str,
    body: str | None,
    dry_run: bool,
) -> str:
    if dry_run or llm.name == "null":
        return trim_body(title, 120)
    result = llm.complete(
        system,
        f"Title: {title}\n\nBody:\n{trim_body(body, 600)}",
    )
    usage.add(result)
    return (result.text or title).strip().splitlines()[0][:200]


def build_pipeline(
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
                console.print(f"[yellow]LLM unavailable ({e}); using null[/yellow]")
                llm = get_provider("null")

    usage = UsageTracker()
    system = load_prompt("pipeline", workspace)
    run_id = db.start_run("pipeline", project_name, since=since_str)

    rfcs_new: list[dict] = []
    rfcs_ongoing: list[dict] = []
    roadmaps: list[dict] = []
    significant_prs: list[dict] = []
    proposal_files: list[dict] = []
    tldr: list[str] = []

    try:
        for repo_row in db.list_repos(project_name):
            if repo_row["tier"] == "overflow":
                continue
            repo_id = repo_row["id"]
            modules = db.list_modules(repo_id)
            module_paths = [json.loads(m["paths_json"]) for m in modules]

            for issue in db.list_issues_by_signal(repo_id):
                signal = issue["signal"]
                if not signal:
                    continue
                heat = (issue["comments_count"] or 0) + (
                    issue["reactions_count"] or 0
                )
                summary = _one_liner(
                    llm, usage, system, issue["title"], issue["body"], dry_run
                )
                item = {
                    "title": f"#{issue['number']} {issue['title']}",
                    "url": issue["url"],
                    "summary": summary,
                    "status": issue["state"],
                    "heat": heat,
                }
                created = issue["created_at"] or ""
                if signal == "roadmap":
                    checks = _parse_checklist(issue["body"])
                    done = sum(1 for c in checks if c["done"])
                    roadmaps.append(
                        {
                            "title": item["title"],
                            "url": item["url"],
                            "done": done,
                            "total": len(checks),
                            "items": checks[:20],
                        }
                    )
                elif created >= since_iso:
                    rfcs_new.append(item)
                elif issue["state"] == "OPEN":
                    rfcs_ongoing.append(item)

            for pr in db.list_open_prs(repo_id):
                if not _is_significant(pr, project, module_paths):
                    continue
                summary = _one_liner(
                    llm, usage, system, pr["title"], pr["body"], dry_run
                )
                try:
                    raw_revs = json.loads(pr["reviewers_json"] or "[]")
                except (json.JSONDecodeError, TypeError, KeyError):
                    raw_revs = []
                rev_names = []
                for r in raw_revs:
                    if isinstance(r, dict) and r.get("login"):
                        rev_names.append(r["login"])
                    elif isinstance(r, str):
                        rev_names.append(r)
                significant_prs.append(
                    {
                        "number": pr["number"],
                        "title": pr["title"],
                        "url": pr["url"],
                        "summary": summary,
                        "author": pr["author"],
                        "age_days": _age_days(pr["created_at"]),
                        "reviewers": sorted(set(rev_names)),
                        "updated_at": pr["updated_at"],
                    }
                )

            for pf in db.list_proposal_files(repo_id):
                proposal_files.append(
                    {
                        "path": pf["path"],
                        "url": pf["url"],
                        "last_modified_at": pf["last_modified_at"],
                    }
                )

        if rfcs_new:
            tldr.append(f"{len(rfcs_new)} new RFC/proposal issue(s)")
        if significant_prs:
            tldr.append(f"{len(significant_prs)} significant open PR(s)")
        if roadmaps:
            tldr.append(f"{len(roadmaps)} roadmap issue(s) tracked")
        if proposal_files:
            tldr.append(f"{len(proposal_files)} proposal file(s) in tree")
        if rfcs_ongoing:
            tldr.append(f"{len(rfcs_ongoing)} ongoing RFC(s)")

        md = render(
            "pipeline.md.j2",
            project=project_name,
            date=today,
            generated_at=to_iso(datetime.now(timezone.utc)),
            tldr=tldr[:5],
            rfcs_new=rfcs_new,
            rfcs_ongoing=rfcs_ongoing,
            proposal_files=proposal_files,
            significant_prs=significant_prs,
            roadmaps=roadmaps,
        )
        out_dir = reports_dir(workspace) / project_name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{today}-pipeline.md"
        out_path.write_text(md)
        from tracker.stages.rollup import publish_latest

        publish_latest(out_path, "pipeline")
        db.finish_run(run_id, "ok", {"path": str(out_path), **usage.summary()})
        console.print(f"[green]Wrote[/green] {out_path}")
        return out_path
    except Exception as e:
        db.finish_run(run_id, "error", {"error": str(e)})
        raise

"""People: owners + active authors/reviewers (90d)."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from rich.console import Console

from tracker.config import RootConfig
from tracker.db import Database
from tracker.paths import reports_dir
from tracker.render.markdown import render
from tracker.util import match_paths, to_iso

console = Console()


def _top(counter: Counter, n: int = 8) -> list[dict[str, Any]]:
    return [{"login": k, "count": v} for k, v in counter.most_common(n)]


def build_people(
    db: Database,
    config: RootConfig,
    project_name: str,
    *,
    workspace: Path | None = None,
) -> Path:
    project = config.get_project(project_name)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    since_iso = to_iso(datetime.now(timezone.utc) - timedelta(days=90))
    run_id = db.start_run("people", project_name)

    repos_out: list[dict[str, Any]] = []
    try:
        for repo_row in db.list_repos(project_name):
            if repo_row["tier"] == "overflow":
                continue
            repo_id = repo_row["id"]
            ownership = db.list_ownership(repo_id)
            repo_owners: list[str] = []
            pattern_owners: list[tuple[str, list[str]]] = []
            for o in ownership:
                owners = json.loads(o["owners_json"] or "[]")
                pattern_owners.append((o["path_pattern"], owners))
                if o["path_pattern"] in ("*", "/**", "/"):
                    repo_owners.extend(owners)

            modules = db.list_modules(repo_id)
            prs = db.list_merged_prs_since(repo_id, since_iso)

            # Also pull open PR reviewers from stored data
            all_prs = list(prs) + list(db.list_open_prs(repo_id))

            author_c: Counter = Counter()
            reviewer_c: Counter = Counter()
            mod_authors: dict[str, Counter] = defaultdict(Counter)
            mod_reviewers: dict[str, Counter] = defaultdict(Counter)
            mod_owners: dict[str, list[str]] = defaultdict(list)

            module_defs = [
                (m["name"], json.loads(m["paths_json"])) for m in modules
            ]

            for pattern, owners in pattern_owners:
                for name, paths in module_defs:
                    # crude: if pattern matches any module path prefix
                    clean = pattern.lstrip("/")
                    for p in paths:
                        prefix = p.replace("/**", "").rstrip("/")
                        if clean.startswith(prefix) or prefix.startswith(
                            clean.rstrip("*").rstrip("/")
                        ):
                            mod_owners[name].extend(owners)

            for pr in all_prs:
                author = pr["author"]
                if author:
                    author_c[author] += 1
                try:
                    files = [
                        f["path"]
                        for f in json.loads(pr["files_json"] or "[]")
                    ]
                except (json.JSONDecodeError, TypeError):
                    files = []
                try:
                    reviewers = json.loads(pr["reviewers_json"] or "[]")
                except (json.JSONDecodeError, TypeError, KeyError):
                    reviewers = []
                rev_logins = []
                for r in reviewers:
                    if isinstance(r, dict):
                        login = r.get("login")
                    else:
                        login = r
                    if login:
                        reviewer_c[login] += 1
                        rev_logins.append(login)

                for name, paths in module_defs:
                    if match_paths(files, paths):
                        if author:
                            mod_authors[name][author] += 1
                        for login in rev_logins:
                            mod_reviewers[name][login] += 1

            mod_out = []
            for m in modules:
                name = m["name"]
                mod_out.append(
                    {
                        "name": name,
                        "owners": sorted(set(mod_owners.get(name) or [])),
                        "authors": _top(mod_authors[name]),
                        "reviewers": _top(mod_reviewers[name]),
                    }
                )

            repos_out.append(
                {
                    "full_name": repo_row["full_name"],
                    "owners": sorted(set(repo_owners)),
                    "modules": mod_out,
                    "authors": _top(author_c),
                    "reviewers": _top(reviewer_c),
                }
            )

        md = render(
            "people.md.j2",
            project=project_name,
            date=today,
            generated_at=to_iso(datetime.now(timezone.utc)),
            repos=repos_out,
            governance_urls=project.people_signals.governance_urls,
        )
        out_dir = reports_dir(workspace) / project_name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{today}-people.md"
        out_path.write_text(md)
        from tracker.stages.rollup import publish_latest

        publish_latest(out_path, "people")
        db.finish_run(run_id, "ok", {"path": str(out_path)})
        console.print(f"[green]Wrote[/green] {out_path}")
        return out_path
    except Exception as e:
        db.finish_run(run_id, "error", {"error": str(e)})
        raise

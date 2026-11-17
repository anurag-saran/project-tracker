"""Module map with LLM descriptions, caching, and overrides."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rich.console import Console

from tracker.config import RootConfig, load_overrides
from tracker.db import Database
from tracker.github.client import GitHubClient
from tracker.llm import get_provider
from tracker.llm.base import LLMProvider, UsageTracker
from tracker.paths import overrides_dir, reports_dir
from tracker.prompts_loader import load_prompt
from tracker.render.markdown import render
from tracker.util import content_hash, match_paths, to_iso, trim_body

console = Console()


def _gather_context(
    client: GitHubClient | None,
    full_name: str,
    paths: list[str],
    branch: str | None,
) -> dict[str, Any]:
    if client is None:
        return {"readme": None, "listing": [], "docs": None}
    owner, name = full_name.split("/", 1)
    br = branch or "HEAD"
    readme = None
    for candidate in ("README.md", "README.rst", "README"):
        readme = client.get_file_text(owner, name, candidate, branch=br)
        if readme:
            break
    listing: list[str] = []
    for g in paths[:5]:
        prefix = g.replace("/**", "").rstrip("/")
        if not prefix or "*" in prefix:
            continue
        try:
            entries = client.get_tree_entries(
                owner, name, prefix, branch=br
            )
            for e in entries[:30]:
                listing.append(f"{e.get('path') or e.get('name')} ({e.get('type')})")
        except Exception:
            continue
    return {
        "readme": trim_body(readme, 2500) if readme else None,
        "listing": listing[:40],
        "docs": None,
    }


def build_map(
    db: Database,
    config: RootConfig,
    project_name: str,
    *,
    client: GitHubClient | None = None,
    dry_run: bool = False,
    workspace: Path | None = None,
    llm: LLMProvider | None = None,
) -> Path:
    project = config.get_project(project_name)
    today_iso = to_iso(datetime.now(timezone.utc))
    overrides = load_overrides(overrides_dir(workspace) / f"{project_name}.yaml")

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
    system = load_prompt("module_map", workspace)
    run_id = db.start_run("map", project_name)

    repos_out: list[dict[str, Any]] = []
    overflow: list[dict[str, Any]] = []

    try:
        for repo_row in db.list_repos(project_name):
            if repo_row["tier"] == "overflow":
                overflow.append(
                    {
                        "full_name": repo_row["full_name"],
                        "description": repo_row["description"],
                        "activity_90d": repo_row["activity_90d"],
                    }
                )
                continue

            full = repo_row["full_name"]
            repo_id = repo_row["id"]
            ov_repo = overrides.repos.get(full)

            ownership = db.list_ownership(repo_id)
            owners: list[str] = []
            for o in ownership:
                if o["path_pattern"] in ("*", "/**", "/"):
                    owners.extend(json.loads(o["owners_json"] or "[]"))
            if not owners and ownership:
                # take first few CODEOWNERS entries as indicative
                for o in ownership[:3]:
                    owners.extend(json.loads(o["owners_json"] or "[]"))
            owners = sorted(set(owners))

            # Repo-level purpose
            purpose = None
            if ov_repo and (ov_repo.purpose or ov_repo.description):
                purpose = ov_repo.purpose or ov_repo.description
            else:
                ctx = _gather_context(
                    client,
                    full,
                    ["*"],
                    repo_row["default_branch"],
                )
                source_hash = content_hash(ctx)
                subject = f"{project_name}/{full}"
                cached = db.get_summary("module_map", subject, source_hash)
                if cached:
                    purpose = cached
                elif dry_run or llm.name == "null":
                    purpose = repo_row["description"] or (
                        f"Repository {full}. "
                        + (f"README excerpt available." if ctx["readme"] else "")
                    )
                else:
                    user = (
                        f"Repo: {full}\nDescription: {repo_row['description']}\n\n"
                        f"README:\n{ctx['readme'] or '(none)'}\n\n"
                        f"Top listing:\n" + "\n".join(ctx["listing"][:20])
                    )
                    result = llm.complete(system, user)
                    usage.add(result)
                    purpose = result.text.strip()
                    db.save_summary(
                        "module_map",
                        subject,
                        source_hash,
                        purpose,
                        model=result.model,
                        tokens_in=result.tokens_in,
                        tokens_out=result.tokens_out,
                    )

            modules_out = []
            for m in db.list_modules(repo_id):
                paths = json.loads(m["paths_json"])
                key = f"{full}/{m['name']}"
                ov = overrides.modules.get(key) or overrides.modules.get(
                    m["name"]
                )
                mod_purpose = None
                if ov and (ov.purpose or ov.description):
                    mod_purpose = ov.purpose or ov.description
                else:
                    ctx = _gather_context(
                        client,
                        full,
                        paths,
                        repo_row["default_branch"],
                    )
                    source_hash = content_hash(m["name"], paths, ctx)
                    subject = f"{project_name}/{full}/{m['name']}"
                    cached = db.get_summary("module_map", subject, source_hash)
                    if cached:
                        mod_purpose = cached
                    elif dry_run or llm.name == "null":
                        mod_purpose = (
                            f"Module `{m['name']}` covering "
                            + ", ".join(f"`{p}`" for p in paths)
                            + "."
                        )
                    else:
                        user = (
                            f"Repo: {full}\nModule: {m['name']}\n"
                            f"Paths: {paths}\n\nREADME:\n{ctx['readme'] or '(none)'}\n\n"
                            f"Directory listing:\n"
                            + "\n".join(ctx["listing"][:30])
                        )
                        result = llm.complete(system, user)
                        usage.add(result)
                        mod_purpose = result.text.strip()
                        db.save_summary(
                            "module_map",
                            subject,
                            source_hash,
                            mod_purpose,
                            model=result.model,
                            tokens_in=result.tokens_in,
                            tokens_out=result.tokens_out,
                        )

                # activity: PRs touching module in 90d (from stored)
                activity = 0
                for pr in db.execute(
                    "SELECT files_json FROM pull_requests WHERE repo_id=? AND state='MERGED'",
                    (repo_id,),
                ).fetchall():
                    try:
                        files = [
                            f["path"]
                            for f in json.loads(pr["files_json"] or "[]")
                        ]
                    except (json.JSONDecodeError, TypeError):
                        files = []
                    if match_paths(files, paths):
                        activity += 1

                mod_owners: list[str] = []
                for o in ownership:
                    pattern = o["path_pattern"].lstrip("/")
                    for p in paths:
                        prefix = p.replace("/**", "").rstrip("/")
                        if prefix and (
                            pattern.startswith(prefix)
                            or prefix.startswith(pattern.rstrip("*").rstrip("/"))
                        ):
                            mod_owners.extend(
                                json.loads(o["owners_json"] or "[]")
                            )
                modules_out.append(
                    {
                        "name": m["name"],
                        "paths": paths,
                        "purpose": mod_purpose,
                        "owners": sorted(set(mod_owners)),
                        "activity_90d": activity,
                    }
                )

            entry_points = None
            relations = None
            if ov_repo:
                entry_points = ov_repo.entry_points
                relations = ov_repo.relations

            repos_out.append(
                {
                    "full_name": full,
                    "tier": repo_row["tier"],
                    "description": repo_row["description"],
                    "purpose": purpose,
                    "activity_90d": repo_row["activity_90d"],
                    "stars": repo_row["stars"],
                    "latest_release_tag": repo_row["latest_release_tag"],
                    "latest_release_at": repo_row["latest_release_at"],
                    "owners": owners,
                    "entry_points": entry_points,
                    "relations": relations,
                    "modules": modules_out,
                }
            )

        md = render(
            "module_map.md.j2",
            project=project_name,
            generated_at=today_iso,
            description=project.description,
            repos=repos_out,
            overflow=overflow,
        )
        out_dir = reports_dir(workspace) / project_name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "module-map.md"
        out_path.write_text(md)
        db.finish_run(run_id, "ok", {"path": str(out_path), **usage.summary()})
        console.print(
            f"[green]Wrote[/green] {out_path} · "
            f"est. ${usage.cost_usd:.4f}"
        )
        return out_path
    except Exception as e:
        db.finish_run(run_id, "error", {"error": str(e)})
        raise

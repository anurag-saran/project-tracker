"""Typer CLI entrypoint for OSS Project Tracker."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from tracker import __version__
from tracker.config import (
    GeneratedRepos,
    SEED_PROJECTS_YAML,
    load_config,
    load_generated_modules,
    save_generated_modules,
)
from tracker.db import Database
from tracker.github.client import GitHubClient, GitHubError
from tracker.github.discover import (
    propose_modules,
    probe_proposals_dir,
    resolve_project_repos,
    validate_codeowners,
)
from tracker.paths import (
    db_path,
    find_workspace,
    modules_generated,
    overrides_dir,
    projects_yaml,
    prompts_dir,
    reports_dir,
    site_dir,
)

app = typer.Typer(
    name="tracker",
    help="Track multi-repo open-source projects.",
    no_args_is_help=True,
)
console = Console()


def _root(ctx: typer.Context) -> Path:
    return ctx.obj["root"]


def _db(ctx: typer.Context) -> Database:
    return Database(db_path(_root(ctx)))


def _config(ctx: typer.Context):
    return load_config(projects_yaml(_root(ctx)))


def _client(ctx: typer.Context, db: Database | None = None) -> GitHubClient:
    return GitHubClient(db=db)


def _projects(ctx: typer.Context, project: str) -> list[str]:
    cfg = _config(ctx)
    if project == "all":
        return cfg.project_names()
    cfg.get_project(project)  # validate
    return [project]


@app.callback()
def main(
    ctx: typer.Context,
    root: Optional[Path] = typer.Option(
        None,
        "--root",
        help="Workspace root (default: walk up from cwd)",
    ),
) -> None:
    ctx.ensure_object(dict)
    ctx.obj["root"] = (root or find_workspace()).resolve()


@app.command()
def version() -> None:
    """Print version."""
    console.print(__version__)


@app.command("init")
def init_cmd(
    ctx: typer.Context,
    force: bool = typer.Option(False, "--force", help="Overwrite projects.yaml"),
) -> None:
    """Create projects.yaml, database, and folder layout."""
    root = _root(ctx)
    py = projects_yaml(root)
    if py.exists() and not force:
        console.print(f"[yellow]exists[/yellow] {py} (use --force to overwrite)")
    else:
        py.write_text(SEED_PROJECTS_YAML)
        console.print(f"[green]wrote[/green] {py}")

    for d in (
        root / ".tracker",
        reports_dir(root),
        overrides_dir(root),
        prompts_dir(root),
        site_dir(root),
    ):
        d.mkdir(parents=True, exist_ok=True)
        console.print(f"[green]dir[/green]  {d}")

    # Seed prompts if missing
    pkg_prompts = Path(__file__).resolve().parents[2] / "prompts"
    if pkg_prompts.exists():
        for src in pkg_prompts.glob("*.md"):
            dest = prompts_dir(root) / src.name
            if not dest.exists():
                dest.write_text(src.read_text())
                console.print(f"[green]wrote[/green] {dest}")

    db = Database(db_path(root))
    db.close()
    console.print(f"[green]db[/green]   {db_path(root)}")
    console.print("Done. Set GITHUB_TOKEN (and optionally ANTHROPIC_API_KEY).")


@app.command()
def validate(ctx: typer.Context) -> None:
    """Resolve orgs/repos/paths against GitHub; report problems."""
    root = _root(ctx)
    cfg = _config(ctx)
    db = _db(ctx)
    errors = 0
    try:
        client = _client(ctx, db)
    except GitHubError as e:
        console.print(f"[red]error[/red] {e}")
        raise typer.Exit(2)

    with client:
        for project in cfg.projects:
            console.rule(f"[bold]{project.name}")
            repos, findings = resolve_project_repos(
                client,
                project,
                max_repos_per_org=cfg.settings.max_repos_per_org,
                compute_activity=False,
            )
            for f in findings:
                style = {"ok": "green", "warn": "yellow", "error": "red"}[f.level]
                console.print(f"[{style}]{f.level}[/{style}] {f.subject}: {f.message}")
                if f.level == "error":
                    errors += 1

            table = Table(title="Resolved repos")
            table.add_column("repo")
            table.add_column("tier")
            table.add_column("stars", justify="right")
            for r in repos:
                table.add_row(r.full_name, r.tier.value, str(r.stars))
            console.print(table)

            # CODEOWNERS on core repos
            for r in repos:
                if r.tier.value != "core":
                    continue
                for f in validate_codeowners(
                    client, r.full_name, project.people_signals.codeowners,
                    branch=r.default_branch,
                ):
                    style = {"ok": "green", "warn": "yellow", "error": "red"}[f.level]
                    console.print(
                        f"[{style}]{f.level}[/{style}] {f.subject}: {f.message}"
                    )

            default_repo = next(
                (r.full_name for r in repos if r.tier.value == "core"),
                repos[0].full_name if repos else None,
            )
            for entry in project.pipeline_signals.proposals_dirs:
                _full, _path, pfindings = probe_proposals_dir(
                    client, entry, default_repo=default_repo
                )
                for f in pfindings:
                    style = {"ok": "green", "warn": "yellow", "error": "red"}[f.level]
                    console.print(
                        f"[{style}]{f.level}[/{style}] {f.subject}: {f.message}"
                    )

    db.close()
    if errors:
        console.print(f"[red]{errors} error(s)[/red]")
        raise typer.Exit(1)
    console.print("[green]validate ok[/green]")


@app.command()
def discover(
    ctx: typer.Context,
    project: str = typer.Argument(..., help="Project name"),
) -> None:
    """List repos and propose modules; write modules.generated.yaml."""
    root = _root(ctx)
    cfg = _config(ctx)
    proj = cfg.get_project(project)
    db = _db(ctx)
    try:
        client = _client(ctx, db)
    except GitHubError as e:
        console.print(f"[red]error[/red] {e}")
        raise typer.Exit(2)

    with client:
        repos, findings = resolve_project_repos(
            client,
            proj,
            max_repos_per_org=cfg.settings.max_repos_per_org,
            compute_activity=True,
        )
        for f in findings:
            style = {"ok": "green", "warn": "yellow", "error": "red"}[f.level]
            console.print(f"[{style}]{f.level}[/{style}] {f.subject}: {f.message}")

        generated = load_generated_modules(modules_generated(root))
        project_repos: dict = generated.projects.get(project, {})

        table = Table(title=f"{project} repos")
        table.add_column("repo")
        table.add_column("tier")
        table.add_column("activity_90d", justify="right")
        table.add_column("modules")

        for r in repos:
            mods = list(r.modules)
            source = r.modules_source
            if not mods and r.tier.value == "core":
                # preserve user edits in generated file
                if r.full_name in project_repos and project_repos[r.full_name]:
                    mods = project_repos[r.full_name]
                    source = "generated(existing)"
                else:
                    mods = propose_modules(
                        client,
                        r.full_name,
                        codeowners_paths=proj.people_signals.codeowners,
                        branch=r.default_branch or "HEAD",
                    )
                    source = "generated"
                    project_repos[r.full_name] = mods
            elif mods and source == "config":
                pass
            table.add_row(
                r.full_name,
                r.tier.value,
                str(r.activity_90d),
                f"{len(mods)} ({source})" if mods else "—",
            )
            console.print(
                f"  [dim]{r.full_name}[/dim] modules: "
                + (
                    ", ".join(m.name for m in mods)
                    if mods
                    else "(none)"
                )
            )

            # Persist into SQLite lightly
            repo_id = db.upsert_repo(
                project,
                r.full_name,
                r.tier.value,
                description=r.description,
                default_branch=r.default_branch,
                is_archived=r.is_archived,
                stars=r.stars,
                pushed_at=r.pushed_at,
                latest_release_tag=r.latest_release_tag,
                latest_release_at=r.latest_release_at,
                activity_90d=r.activity_90d,
            )
            if mods:
                db.replace_modules(
                    repo_id,
                    [
                        {
                            "name": m.name,
                            "paths": m.paths,
                            "source": "generated" if "generated" in source else source,
                        }
                        for m in mods
                    ],
                )

        generated.projects[project] = project_repos
        out = modules_generated(root)
        save_generated_modules(out, generated)
        console.print(table)
        console.print(f"[green]wrote[/green] {out}")

        default_repo = next(
            (r.full_name for r in repos if r.tier.value == "core"),
            repos[0].full_name if repos else None,
        )
        for entry in proj.pipeline_signals.proposals_dirs:
            full, path, pfindings = probe_proposals_dir(
                client, entry, default_repo=default_repo
            )
            for f in pfindings:
                style = {"ok": "green", "warn": "yellow", "error": "red"}[f.level]
                console.print(
                    f"[{style}]{f.level}[/{style}] {f.subject}: {f.message}"
                )
            if full and path:
                console.print(
                    f"[cyan]suggestion[/cyan] set proposals_dirs to "
                    f'["{full}:{path}"]'
                )
    db.close()


@app.command()
def fetch(
    ctx: typer.Context,
    project: str = typer.Argument("all", help="Project name or 'all'"),
    since: Optional[str] = typer.Option(
        None, "--since", help="Lookback window, e.g. 7d or 2025-01-01"
    ),
) -> None:
    """Fetch GitHub data into SQLite (deterministic stage)."""
    from tracker.stages.fetch import fetch_project

    root = _root(ctx)
    cfg = _config(ctx)
    db = _db(ctx)
    try:
        client = _client(ctx, db)
    except GitHubError as e:
        console.print(f"[red]error[/red] {e}")
        raise typer.Exit(2)

    with client:
        for name in _projects(ctx, project):
            console.rule(f"[bold]fetch {name}")
            stats = fetch_project(
                client, db, cfg, name, since=since, workspace=root
            )
            console.print(json.dumps(stats, indent=2))
    db.close()


@app.command()
def digest(
    ctx: typer.Context,
    project: str = typer.Argument("all", help="Project name or 'all'"),
    since: Optional[str] = typer.Option(None, "--since"),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Skip LLM; emit grounded PR lists"
    ),
    skip_fetch: bool = typer.Option(
        False, "--skip-fetch", help="Do not fetch before summarizing"
    ),
) -> None:
    """Build change digest markdown reports."""
    from tracker.stages.digest import build_digest
    from tracker.stages.fetch import fetch_project

    root = _root(ctx)
    cfg = _config(ctx)
    db = _db(ctx)
    names = _projects(ctx, project)

    if not skip_fetch:
        try:
            client = _client(ctx, db)
        except GitHubError as e:
            console.print(f"[red]error[/red] {e}")
            raise typer.Exit(2)
        with client:
            for name in names:
                console.rule(f"[bold]fetch {name}")
                fetch_project(
                    client, db, cfg, name, since=since, workspace=root
                )
    for name in names:
        console.rule(f"[bold]digest {name}")
        build_digest(
            db, cfg, name, since=since, dry_run=dry_run, workspace=root
        )
    db.close()


@app.command()
def pipeline(
    ctx: typer.Context,
    project: str = typer.Argument("all"),
    since: Optional[str] = typer.Option(None, "--since"),
    dry_run: bool = typer.Option(False, "--dry-run"),
    skip_fetch: bool = typer.Option(False, "--skip-fetch"),
) -> None:
    """Build pipeline (RFCs / significant PRs / roadmaps) reports."""
    from tracker.stages.fetch import fetch_project
    from tracker.stages.pipeline import build_pipeline

    root = _root(ctx)
    cfg = _config(ctx)
    db = _db(ctx)
    names = _projects(ctx, project)

    if not skip_fetch:
        try:
            client = _client(ctx, db)
        except GitHubError as e:
            console.print(f"[red]error[/red] {e}")
            raise typer.Exit(2)
        with client:
            for name in names:
                console.rule(f"[bold]fetch {name}")
                fetch_project(
                    client, db, cfg, name, since=since, workspace=root
                )
    for name in names:
        console.rule(f"[bold]pipeline {name}")
        build_pipeline(
            db, cfg, name, since=since, dry_run=dry_run, workspace=root
        )
    db.close()


@app.command()
def people(
    ctx: typer.Context,
    project: str = typer.Argument(...),
    skip_fetch: bool = typer.Option(False, "--skip-fetch"),
) -> None:
    """Build people / ownership report for a project."""
    from tracker.stages.fetch import fetch_project
    from tracker.stages.people import build_people

    root = _root(ctx)
    cfg = _config(ctx)
    db = _db(ctx)
    if not skip_fetch:
        try:
            client = _client(ctx, db)
        except GitHubError as e:
            console.print(f"[red]error[/red] {e}")
            raise typer.Exit(2)
        with client:
            console.rule(f"[bold]fetch {project}")
            fetch_project(client, db, cfg, project, workspace=root)
    console.rule(f"[bold]people {project}")
    build_people(db, cfg, project, workspace=root)
    db.close()


@app.command("map")
def map_cmd(
    ctx: typer.Context,
    project: str = typer.Argument(...),
    dry_run: bool = typer.Option(False, "--dry-run"),
    skip_fetch: bool = typer.Option(False, "--skip-fetch"),
) -> None:
    """Build module map with descriptions."""
    from tracker.stages.fetch import fetch_project
    from tracker.stages.map import build_map

    root = _root(ctx)
    cfg = _config(ctx)
    db = _db(ctx)
    client = None
    try:
        client = _client(ctx, db)
    except GitHubError as e:
        console.print(f"[yellow]warn[/yellow] {e} — map without live GitHub context")
        client = None

    if client and not skip_fetch:
        with client:
            console.rule(f"[bold]fetch {project}")
            fetch_project(client, db, cfg, project, workspace=root)
            console.rule(f"[bold]map {project}")
            build_map(
                db,
                cfg,
                project,
                client=client,
                dry_run=dry_run,
                workspace=root,
            )
    else:
        console.rule(f"[bold]map {project}")
        build_map(
            db,
            cfg,
            project,
            client=client,
            dry_run=dry_run,
            workspace=root,
        )
        if client:
            client.close()
    db.close()


@app.command()
def blogs(
    ctx: typer.Context,
    project: str = typer.Argument("all", help="Project name or 'all'"),
    since: Optional[str] = typer.Option(None, "--since"),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Skip LLM; use feed excerpts as summaries"
    ),
    skip_fetch: bool = typer.Option(
        False, "--skip-fetch", help="Summarize from SQLite only"
    ),
) -> None:
    """Fetch project blogs (RSS) and write weekly summaries with post links."""
    from tracker.stages.blogs import build_blogs

    root = _root(ctx)
    cfg = _config(ctx)
    db = _db(ctx)
    for name in _projects(ctx, project):
        console.rule(f"[bold]blogs {name}")
        build_blogs(
            db,
            cfg,
            name,
            since=since,
            dry_run=dry_run,
            workspace=root,
            skip_fetch=skip_fetch,
        )
    db.close()


@app.command()
def releases(
    ctx: typer.Context,
    project: str = typer.Argument("all", help="Project name or 'all'"),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Skip LLM; extract bullets from notes only"
    ),
    skip_fetch: bool = typer.Option(
        False, "--skip-fetch", help="Use SQLite releases only (no GitHub refresh)"
    ),
    limit: int = typer.Option(6, "--limit", help="Stable releases per repo"),
) -> None:
    """List features shipped per release + what's planned for the next drop."""
    from tracker.stages.releases import build_releases

    root = _root(ctx)
    cfg = _config(ctx)
    db = _db(ctx)
    client = None
    if not skip_fetch:
        try:
            client = _client(ctx, db)
        except GitHubError as e:
            console.print(f"[yellow]warn[/yellow] {e} — using cached releases")
            client = None

    try:
        for name in _projects(ctx, project):
            console.rule(f"[bold]releases {name}")
            build_releases(
                db,
                cfg,
                name,
                client=client,
                dry_run=dry_run,
                workspace=root,
                release_limit=limit,
            )
    finally:
        if client:
            client.close()
        db.close()


@app.command()
def rollup(
    ctx: typer.Context,
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Skip LLM; copy extracted digest bullets into WEEKLY",
    ),
) -> None:
    """Write reports/WEEKLY.md + ensure latest-* copies for week-over-week diffs."""
    from tracker.stages.rollup import build_weekly_rollup

    root = _root(ctx)
    cfg = _config(ctx)
    path = build_weekly_rollup(cfg, workspace=root, dry_run=dry_run)
    console.print(
        "Read the rollup, then diff stable paths like "
        "reports/<project>/latest-digest.md against last week."
    )
    console.print(path)


@app.command()
def site(ctx: typer.Context) -> None:
    """Build static HTML site under site/."""
    from tracker.render.site import build_site

    root = _root(ctx)
    cfg = _config(ctx)
    build_site(cfg, workspace=root)


@app.command()
def notify(
    ctx: typer.Context,
    project: str = typer.Argument(...),
    channel: Optional[str] = typer.Option(
        None, "--channel", help="slack,email (comma-separated). Off unless set."
    ),
) -> None:
    """Send the latest digest via optional notifiers (off by default)."""
    from tracker.notify import get_notifiers, notify_all

    root = _root(ctx)
    rdir = reports_dir(root) / project
    digests = sorted(rdir.glob("*-digest.md"), reverse=True) if rdir.exists() else []
    if not digests:
        console.print(f"[red]no digest found for {project}[/red]")
        raise typer.Exit(1)
    body = digests[0].read_text()
    names = [c.strip() for c in (channel or "").split(",") if c.strip()]
    notifiers = get_notifiers(names)
    if not notifiers:
        console.print(
            "[yellow]No notifiers enabled.[/yellow] "
            "Pass --channel slack or set TRACKER_NOTIFIERS."
        )
        raise typer.Exit(0)
    notify_all(notifiers, f"{project} digest", body)
    console.print(f"[green]notified via[/green] {', '.join(n.name for n in notifiers)}")


if __name__ == "__main__":
    app()

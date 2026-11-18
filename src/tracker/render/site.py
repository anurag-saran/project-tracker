"""Build a static HTML site from reports/ for GitHub Pages."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rich.console import Console

from tracker.config import RootConfig
from tracker.paths import reports_dir, site_dir
from tracker.render.markdown import get_env
from tracker.util import to_iso

console = Console()


def _md_to_html(md: str) -> str:
    """Minimal markdown → HTML (headings, lists, links, code, bold)."""
    lines = md.splitlines()
    out: list[str] = []
    in_ul = False

    def close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def inline(s: str) -> str:
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    for line in lines:
        if re.match(r"^### ", line):
            close_ul()
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif re.match(r"^## ", line):
            close_ul()
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif re.match(r"^# ", line):
            close_ul()
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif re.match(r"^[-*] ", line):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(line[2:])}</li>")
        elif line.strip() == "":
            close_ul()
        else:
            close_ul()
            out.append(f"<p>{inline(line)}</p>")
    close_ul()
    return "\n".join(out)


def build_site(
    config: RootConfig,
    *,
    workspace: Path | None = None,
) -> Path:
    env = get_env()
    reports = reports_dir(workspace)
    out = site_dir(workspace)
    out.mkdir(parents=True, exist_ok=True)
    generated_at = to_iso(datetime.now(timezone.utc))

    projects_meta: list[dict[str, Any]] = []
    for p in config.projects:
        pdir = reports / p.name
        digests = []
        pipelines = []
        blogs = []
        releases = []
        people = []
        has_map = False
        if pdir.exists():
            for kind, bucket in (
                ("digest", digests),
                ("pipeline", pipelines),
                ("blogs", blogs),
                ("releases", releases),
                ("people", people),
            ):
                latest = pdir / f"latest-{kind}.md"
                if latest.exists():
                    bucket.append(
                        {
                            "label": f"latest-{kind}",
                            "file": f"latest-{kind}.html",
                            "src": latest,
                        }
                    )
                for f in sorted(pdir.glob(f"*-{kind}.md"), reverse=True):
                    if f.name.startswith("latest-"):
                        continue
                    bucket.append(
                        {
                            "label": f.stem,
                            "file": f.stem + ".html",
                            "src": f,
                        }
                    )
            if (pdir / "module-map.md").exists():
                has_map = True

        projects_meta.append(
            {
                "name": p.name,
                "description": p.description,
                "digests": digests,
                "pipelines": pipelines,
                "blogs": blogs,
                "releases": releases,
                "people": people,
                "has_map": has_map,
            }
        )

        proj_out = out / p.name
        proj_out.mkdir(parents=True, exist_ok=True)
        (proj_out / "index.html").write_text(
            env.get_template("site/project.html.j2").render(
                projects=projects_meta,
                project=projects_meta[-1],
                generated_at=generated_at,
            )
        )

        if has_map:
            body = _md_to_html((pdir / "module-map.md").read_text())
            (proj_out / "module-map.html").write_text(
                env.get_template("site/report.html.j2").render(
                    projects=projects_meta,
                    title=f"{p.name} module map",
                    project_name=p.name,
                    body_html=body,
                    generated_at=generated_at,
                )
            )

        for group in (digests, pipelines, blogs, releases, people):
            for item in group:
                body = _md_to_html(item["src"].read_text())
                (proj_out / item["file"]).write_text(
                    env.get_template("site/report.html.j2").render(
                        projects=projects_meta,
                        title=item["label"],
                        project_name=p.name,
                        body_html=body,
                        generated_at=generated_at,
                    )
                )

    weekly = reports / "WEEKLY.md"
    if weekly.exists():
        (out / "weekly.html").write_text(
            env.get_template("site/report.html.j2").render(
                projects=projects_meta,
                title="Weekly tracker",
                project_name=".",
                body_html=_md_to_html(weekly.read_text()),
                generated_at=generated_at,
            )
        )

    (out / "index.html").write_text(
        env.get_template("site/index.html.j2").render(
            projects=projects_meta,
            generated_at=generated_at,
            has_weekly=weekly.exists(),
        )
    )
    console.print(f"[green]Site built at[/green] {out}")
    return out

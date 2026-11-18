"""Weekly rollup: stable latest-* copies + reports/WEEKLY.md for PR reading."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from rich.console import Console

from tracker.config import RootConfig
from tracker.paths import reports_dir
from tracker.util import to_iso

console = Console()

_TLDR_RE = re.compile(
    r"##\s+TL;DR[^\n]*\n+(.*?)(?=\n##\s|\Z)",
    re.DOTALL | re.IGNORECASE,
)


def publish_latest(dated_path: Path, kind: str) -> Path:
    """Copy a dated report to reports/<project>/latest-<kind>.md."""
    latest = dated_path.parent / f"latest-{kind}.md"
    latest.write_text(dated_path.read_text())
    return latest


def _extract_tldr(md: str) -> list[str]:
    m = _TLDR_RE.search(md)
    if not m:
        return []
    bullets = []
    for line in m.group(1).splitlines():
        s = line.strip()
        if s.startswith("- "):
            bullets.append(s[2:].strip())
    return bullets


def _latest(project_dir: Path, kind: str) -> Path | None:
    p = project_dir / f"latest-{kind}.md"
    if p.exists():
        return p
    # fall back to newest dated file
    dated = sorted(project_dir.glob(f"*-{kind}.md"), reverse=True)
    return dated[0] if dated else None


def build_weekly_rollup(
    config: RootConfig,
    *,
    workspace: Path | None = None,
    date: str | None = None,
) -> Path:
    """Build reports/WEEKLY.md with per-project TL;DRs and links to latest reports."""
    root = reports_dir(workspace)
    root.mkdir(parents=True, exist_ok=True)
    day = date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    generated = to_iso(datetime.now(timezone.utc))

    parts: list[str] = [
        f"# Weekly tracker — {day}",
        "",
        f"_Generated {generated}_",
        "",
        "Open the **Files changed** tab on the weekly PR to diff each project's "
        "`latest-digest.md` / `latest-pipeline.md` section against last week.",
        "",
        "## Projects",
        "",
    ]

    for project in config.projects:
        pdir = root / project.name
        parts.append(f"### {project.name}")
        if project.description:
            parts.append("")
            parts.append(project.description)
        parts.append("")

        digest = _latest(pdir, "digest")
        pipeline = _latest(pdir, "pipeline")
        blogs = _latest(pdir, "blogs")
        people = _latest(pdir, "people")
        mmap = pdir / "module-map.md"

        if blogs and blogs.exists():
            if blogs.name != "latest-blogs.md":
                publish_latest(blogs, "blogs")
                blogs = pdir / "latest-blogs.md"
            btldr = _extract_tldr(blogs.read_text())
            parts.append("**New blogs**")
            parts.append("")
            if btldr:
                for b in btldr:
                    parts.append(f"- {b}")
            else:
                parts.append("- _(none this period)_")
            parts.append("")
            parts.append(
                f"→ [`reports/{project.name}/latest-blogs.md`]({project.name}/latest-blogs.md)"
            )
            parts.append("")

        if digest and digest.exists():
            # ensure stable latest path exists for diffs
            if digest.name != "latest-digest.md":
                publish_latest(digest, "digest")
                digest = pdir / "latest-digest.md"
            tldr = _extract_tldr(digest.read_text())
            parts.append("**Digest TL;DR**")
            parts.append("")
            if tldr:
                for b in tldr:
                    parts.append(f"- {b}")
            else:
                parts.append("- _(no TL;DR bullets)_")
            parts.append("")
            parts.append(f"→ [`reports/{project.name}/latest-digest.md`]({project.name}/latest-digest.md)")
            parts.append("")
        else:
            parts.append("_No digest yet._")
            parts.append("")

        if pipeline and pipeline.exists():
            if pipeline.name != "latest-pipeline.md":
                publish_latest(pipeline, "pipeline")
                pipeline = pdir / "latest-pipeline.md"
            ptldr = _extract_tldr(pipeline.read_text())
            parts.append("**Pipeline TL;DR**")
            parts.append("")
            if ptldr:
                for b in ptldr:
                    parts.append(f"- {b}")
            else:
                parts.append("- _(no TL;DR bullets)_")
            parts.append("")
            parts.append(
                f"→ [`reports/{project.name}/latest-pipeline.md`]({project.name}/latest-pipeline.md)"
            )
            parts.append("")

        links = []
        if people and people.exists():
            if people.name != "latest-people.md":
                publish_latest(people, "people")
            links.append(f"[people]({project.name}/latest-people.md)")
        if mmap.exists():
            links.append(f"[module map]({project.name}/module-map.md)")
        if links:
            parts.append("Also: " + " · ".join(links))
            parts.append("")

        parts.append("---")
        parts.append("")

    out = root / "WEEKLY.md"
    out.write_text("\n".join(parts).rstrip() + "\n")
    # Dated archive of the rollup too
    (root / f"{day}-WEEKLY.md").write_text(out.read_text())
    console.print(f"[green]Wrote[/green] {out}")
    return out

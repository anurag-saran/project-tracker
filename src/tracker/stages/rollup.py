"""Weekly rollup: stable latest-* copies + reports/WEEKLY.md for PR reading."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from rich.console import Console

from tracker.config import RootConfig
from tracker.db import Database
from tracker.llm import get_provider
from tracker.llm.base import LLMProvider, UsageTracker
from tracker.paths import db_path, reports_dir
from tracker.prompts_loader import load_prompt
from tracker.util import content_hash, to_iso, trim_body

console = Console()

_TLDR_RE = re.compile(
    r"##\s+TL;DR[^\n]*\n+(.*?)(?=\n##\s|\Z)",
    re.DOTALL | re.IGNORECASE,
)
_MAX_SECTION_CHARS = 14_000

# prompt file stem → (cache kind, max bullets, empty fallback)
_SECTION_META = {
    "digest": ("weekly_digest_tldr", 6, ["_(no TL;DR bullets)_"]),
    "releases": ("weekly_releases_tldr", 6, ["_(see latest-releases.md)_"]),
    "blogs": ("weekly_blogs_tldr", 5, ["_(none this period)_"]),
    "pipeline": ("weekly_pipeline_tldr", 6, ["_(no TL;DR bullets)_"]),
}


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


def _parse_bullet_list(text: str) -> list[str]:
    out: list[str] = []
    for ln in (text or "").splitlines():
        s = ln.strip()
        if s.startswith("- "):
            out.append(s[2:].strip())
        elif s.startswith("* "):
            out.append(s[2:].strip())
    return out


def _latest(project_dir: Path, kind: str) -> Path | None:
    p = project_dir / f"latest-{kind}.md"
    if p.exists():
        return p
    dated = sorted(project_dir.glob(f"*-{kind}.md"), reverse=True)
    return dated[0] if dated else None


def _llm_section_tldr(
    *,
    section: str,
    project: str,
    description: str | None,
    report_md: str,
    fallback: list[str],
    llm: LLMProvider,
    usage: UsageTracker,
    db: Database | None,
    system: str,
    dry_run: bool,
) -> list[str]:
    """Narrative TL;DR for a WEEKLY section; falls back to extracted bullets."""
    cache_kind, max_bullets, empty = _SECTION_META[section]
    if not report_md.strip():
        return list(empty)

    if dry_run or llm.name == "null":
        return (fallback or empty)[:max_bullets]

    source_hash = content_hash(section, project, report_md)
    subject = f"weekly/{project}/{section}_tldr"
    if db is not None:
        cached = db.get_summary(cache_kind, subject, source_hash)
        if cached:
            parsed = _parse_bullet_list(cached)
            if parsed:
                return parsed[:max_bullets]

    user = (
        f"Section: {section}\n"
        f"Project: {project}\n"
        f"Description: {description or ''}\n\n"
        f"Existing extracted bullets (optional context):\n"
        + ("\n".join(f"- {b}" for b in fallback) if fallback else "- (none)")
        + f"\n\nFull {section} report markdown (trimmed):\n"
        + trim_body(report_md, _MAX_SECTION_CHARS)
    )
    try:
        result = llm.complete(system, user)
        usage.add(result)
    except Exception as e:
        console.print(
            f"[yellow]weekly {section} TL;DR LLM failed for {project} ({e}); "
            "using extracted bullets[/yellow]"
        )
        return (fallback or empty)[:max_bullets]

    bullets = _parse_bullet_list(result.text)
    if not bullets:
        return (fallback or empty)[:max_bullets]
    bullets = bullets[:max_bullets]
    if db is not None:
        db.save_summary(
            cache_kind,
            subject,
            source_hash,
            "\n".join(f"- {b}" for b in bullets),
            model=result.model,
            tokens_in=result.tokens_in,
            tokens_out=result.tokens_out,
        )
    return bullets


def _append_section(
    parts: list[str],
    *,
    title: str,
    bullets: list[str],
    link_label: str,
    link_href: str,
) -> None:
    parts.append(f"**{title}**")
    parts.append("")
    for b in bullets:
        parts.append(f"- {b}")
    parts.append("")
    parts.append(f"→ [`{link_label}`]({link_href})")
    parts.append("")


def build_weekly_rollup(
    config: RootConfig,
    *,
    workspace: Path | None = None,
    date: str | None = None,
    dry_run: bool = False,
    llm: LLMProvider | None = None,
    db: Database | None = None,
) -> Path:
    """Build reports/WEEKLY.md with per-project TL;DRs and links to latest reports."""
    root = reports_dir(workspace)
    root.mkdir(parents=True, exist_ok=True)
    day = date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    generated = to_iso(datetime.now(timezone.utc))

    own_db = False
    if db is None and not dry_run:
        try:
            db = Database(db_path(workspace))
            own_db = True
        except Exception:
            db = None

    if llm is None:
        if dry_run:
            llm = get_provider("null")
        else:
            try:
                llm = get_provider()
            except Exception as e:
                console.print(
                    f"[yellow]LLM unavailable ({e}); WEEKLY section TL;DRs "
                    "will use extracted bullets[/yellow]"
                )
                llm = get_provider("null")

    usage = UsageTracker()
    prompts = {
        section: load_prompt(f"weekly_{section}_tldr", workspace)
        for section in _SECTION_META
    }

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

    try:
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
            releases = _latest(pdir, "releases")
            people = _latest(pdir, "people")
            mmap = pdir / "module-map.md"

            def _ensure_latest(path: Path | None, kind: str) -> Path | None:
                if not path or not path.exists():
                    return None
                if path.name != f"latest-{kind}.md":
                    publish_latest(path, kind)
                    return pdir / f"latest-{kind}.md"
                return path

            releases = _ensure_latest(releases, "releases")
            if releases:
                md = releases.read_text()
                bullets = _llm_section_tldr(
                    section="releases",
                    project=project.name,
                    description=project.description,
                    report_md=md,
                    fallback=_extract_tldr(md),
                    llm=llm,
                    usage=usage,
                    db=db,
                    system=prompts["releases"],
                    dry_run=dry_run,
                )
                _append_section(
                    parts,
                    title="Releases (shipped + next)",
                    bullets=bullets,
                    link_label=f"reports/{project.name}/latest-releases.md",
                    link_href=f"{project.name}/latest-releases.md",
                )

            blogs = _ensure_latest(blogs, "blogs")
            if blogs:
                md = blogs.read_text()
                bullets = _llm_section_tldr(
                    section="blogs",
                    project=project.name,
                    description=project.description,
                    report_md=md,
                    fallback=_extract_tldr(md),
                    llm=llm,
                    usage=usage,
                    db=db,
                    system=prompts["blogs"],
                    dry_run=dry_run,
                )
                _append_section(
                    parts,
                    title="New blogs",
                    bullets=bullets,
                    link_label=f"reports/{project.name}/latest-blogs.md",
                    link_href=f"{project.name}/latest-blogs.md",
                )

            digest = _ensure_latest(digest, "digest")
            if digest:
                md = digest.read_text()
                bullets = _llm_section_tldr(
                    section="digest",
                    project=project.name,
                    description=project.description,
                    report_md=md,
                    fallback=_extract_tldr(md),
                    llm=llm,
                    usage=usage,
                    db=db,
                    system=prompts["digest"],
                    dry_run=dry_run,
                )
                _append_section(
                    parts,
                    title="Digest TL;DR",
                    bullets=bullets,
                    link_label=f"reports/{project.name}/latest-digest.md",
                    link_href=f"{project.name}/latest-digest.md",
                )
            else:
                parts.append("_No digest yet._")
                parts.append("")

            pipeline = _ensure_latest(pipeline, "pipeline")
            if pipeline:
                md = pipeline.read_text()
                bullets = _llm_section_tldr(
                    section="pipeline",
                    project=project.name,
                    description=project.description,
                    report_md=md,
                    fallback=_extract_tldr(md),
                    llm=llm,
                    usage=usage,
                    db=db,
                    system=prompts["pipeline"],
                    dry_run=dry_run,
                )
                _append_section(
                    parts,
                    title="Pipeline TL;DR",
                    bullets=bullets,
                    link_label=f"reports/{project.name}/latest-pipeline.md",
                    link_href=f"{project.name}/latest-pipeline.md",
                )

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
    finally:
        if own_db and db is not None:
            db.close()

    out = root / "WEEKLY.md"
    out.write_text("\n".join(parts).rstrip() + "\n")
    (root / f"{day}-WEEKLY.md").write_text(out.read_text())
    console.print(
        f"[green]Wrote[/green] {out}"
        + (
            f" · tokens in/out={usage.tokens_in}/{usage.tokens_out}"
            if usage.calls
            else ""
        )
    )
    return out

"""Fetch project blogs via RSS and write monthly summaries with links."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rich.console import Console

from tracker.blog.rss import fetch_feed
from tracker.config import RootConfig
from tracker.db import Database
from tracker.llm import get_provider
from tracker.llm.base import LLMProvider, UsageTracker
from tracker.paths import reports_dir
from tracker.prompts_loader import load_prompt
from tracker.render.markdown import render
from tracker.stages.rollup import publish_latest
from tracker.util import content_hash, parse_since, to_iso, trim_body

console = Console()


def _summarize_post(
    llm: LLMProvider,
    usage: UsageTracker,
    db: Database,
    *,
    system: str,
    project: str,
    title: str,
    url: str,
    summary_src: str,
    dry_run: bool,
) -> str:
    source_hash = content_hash(title, url, summary_src)
    subject = f"{project}/blog/{url}"
    cached = db.get_summary("blog_post", subject, source_hash)
    if cached:
        return cached

    if dry_run or llm.name == "null":
        text = trim_body(summary_src, 400) or f"New post: {title}"
        db.save_summary(
            "blog_post", subject, source_hash, text, model="null"
        )
        return text

    user = (
        f"Project: {project}\nTitle: {title}\nURL: {url}\n\n"
        f"Excerpt / description:\n{trim_body(summary_src, 1800)}\n\n"
        "Write 2–4 sentences summarizing what this post is about and why it "
        "matters. Do not invent facts beyond the excerpt. Do not include the "
        "URL in the summary text."
    )
    result = llm.complete(system, user)
    usage.add(result)
    text = (result.text or "").strip() or trim_body(summary_src, 400)
    db.save_summary(
        "blog_post",
        subject,
        source_hash,
        text,
        model=result.model,
        tokens_in=result.tokens_in,
        tokens_out=result.tokens_out,
    )
    return text


def fetch_and_store_blogs(
    db: Database,
    config: RootConfig,
    project_name: str,
) -> int:
    """Pull RSS feeds into SQLite. Returns number of posts upserted."""
    project = config.get_project(project_name)
    blogs = project.resolved_blog_urls()
    if not blogs:
        console.print(f"[dim]{project_name}: no blog_urls configured[/dim]")
        return 0

    count = 0
    for blog_url in blogs:
        try:
            feed_url, posts = fetch_feed(blog_url)
        except Exception as e:
            console.print(f"[yellow]warn[/yellow] {blog_url}: {e}")
            continue
        console.print(
            f"[cyan]blog[/cyan] {project_name}: {len(posts)} items from {feed_url}"
        )
        for p in posts:
            db.upsert_blog_post(
                project_name,
                {
                    "feed_url": feed_url,
                    "guid": p.guid,
                    "title": p.title,
                    "url": p.url,
                    "published_at": p.published_at,
                    "author": p.author,
                    "summary_src": p.summary_src,
                    "summary": None,
                },
            )
            count += 1
        db.commit()
    return count


def build_blogs(
    db: Database,
    config: RootConfig,
    project_name: str,
    *,
    since: str | None = None,
    dry_run: bool = False,
    workspace: Path | None = None,
    llm: LLMProvider | None = None,
    skip_fetch: bool = False,
) -> Path:
    """Fetch blogs (unless skipped), summarize new posts, write report."""
    project = config.get_project(project_name)
    since_str = since or config.settings.default_since
    since_iso = to_iso(parse_since(since_str))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    blog_index = project.resolved_blog_urls()[:1]
    blog_home = blog_index[0] if blog_index else None

    if not skip_fetch:
        fetch_and_store_blogs(db, config, project_name)

    if llm is None:
        if dry_run:
            llm = get_provider("null")
        else:
            try:
                llm = get_provider()
            except Exception as e:
                console.print(
                    f"[yellow]LLM unavailable ({e}); using null[/yellow]"
                )
                llm = get_provider("null")

    usage = UsageTracker()
    try:
        system = load_prompt("blog", workspace)
    except FileNotFoundError:
        system = (
            "Summarize blog posts for an open-source project tracker. "
            "Be concise and grounded in the provided excerpt only."
        )

    run_id = db.start_run("blogs", project_name, since=since_str)
    posts_out: list[dict[str, Any]] = []
    tldr: list[str] = []

    try:
        rows = db.list_blog_posts_since(project_name, since_iso)
        for row in rows:
            summary = row["summary"]
            if not summary:
                summary = _summarize_post(
                    llm,
                    usage,
                    db,
                    system=system,
                    project=project_name,
                    title=row["title"],
                    url=row["url"],
                    summary_src=row["summary_src"] or "",
                    dry_run=dry_run,
                )
                db.update_blog_summary(project_name, row["guid"], summary)
            posts_out.append(
                {
                    "title": row["title"],
                    "url": row["url"],
                    "published_at": row["published_at"],
                    "author": row["author"],
                    "summary": summary,
                }
            )
            tldr.append(f"[{row['title']}]({row['url']})")

        md = render(
            "blogs.md.j2",
            project=project_name,
            date=today,
            since=since_str,
            generated_at=to_iso(datetime.now(timezone.utc)),
            blog_home=blog_home,
            tldr=tldr[:8],
            posts=posts_out,
        )
        out_dir = reports_dir(workspace) / project_name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{today}-blogs.md"
        out_path.write_text(md)
        publish_latest(out_path, "blogs")
        db.finish_run(
            run_id,
            "ok",
            {"path": str(out_path), "posts": len(posts_out), **usage.summary()},
        )
        console.print(
            f"[green]Wrote[/green] {out_path} ({len(posts_out)} post(s))"
        )
        return out_path
    except Exception as e:
        db.finish_run(run_id, "error", {"error": str(e)})
        raise

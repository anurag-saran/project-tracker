"""Blog RSS parse + weekly blog report tests."""

from __future__ import annotations

from pathlib import Path

import httpx

from tracker.blog.rss import fetch_feed, parse_feed
from tracker.config import load_config
from tracker.db import Database
from tracker.stages.blogs import build_blogs


FIXTURE = Path(__file__).parent / "fixtures" / "blog" / "vllm_rss.xml"


def test_parse_rss_fixture():
    posts = parse_feed(FIXTURE.read_text(), "https://vllm.ai/blog/rss.xml")
    assert len(posts) == 2
    assert posts[0].title == "DeepSeek on Vera Rubin"
    assert posts[0].url.endswith("/2026-11-12-deepseek")
    assert posts[0].published_at and posts[0].published_at.startswith("2026-11-12")
    assert "throughput" in posts[0].summary_src.lower()


def test_fetch_feed_with_transport():
    xml = FIXTURE.read_text()

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/rss.xml"):
            return httpx.Response(200, text=xml, headers={"content-type": "application/xml"})
        return httpx.Response(404)

    transport = httpx.MockTransport(handler)
    with httpx.Client(transport=transport) as client:
        feed_url, posts = fetch_feed("https://vllm.ai/blog", client=client)
    assert feed_url.endswith("/rss.xml")
    assert len(posts) == 2


def test_build_blogs_report(tmp_workspace: Path, db: Database):
    root = Path(__file__).resolve().parents[1]
    cfg = load_config(root / "projects.yaml")
    xml = FIXTURE.read_text()

    def handler(request: httpx.Request) -> httpx.Response:
        if str(request.url).endswith("rss.xml"):
            return httpx.Response(
                200, text=xml, headers={"content-type": "application/xml"}
            )
        return httpx.Response(404)

    # Monkeypatch fetch_feed used by stage via httpx in fetch_feed — inject posts directly
    from tracker.stages import blogs as blogs_mod

    def fake_fetch(url: str, **kwargs):
        return "https://vllm.ai/blog/rss.xml", parse_feed(xml, "https://vllm.ai/blog/rss.xml")

    blogs_mod.fetch_feed = fake_fetch  # type: ignore[attr-defined]

    out = build_blogs(
        db,
        cfg,
        "vllm",
        since="2026-11-01",
        dry_run=True,
        workspace=tmp_workspace,
    )
    text = out.read_text()
    assert "DeepSeek on Vera Rubin" in text
    assert "Read the full post" in text
    assert "https://vllm.ai/blog/2026-11-12-deepseek" in text
    assert "Old post" not in text  # filtered by --since
    assert (tmp_workspace / "reports" / "vllm" / "latest-blogs.md").exists()

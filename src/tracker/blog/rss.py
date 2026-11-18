"""Fetch and parse project blog RSS/Atom feeds."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from urllib.parse import urlparse

import httpx

_TAG_RE = re.compile(r"<[^>]+>")
_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


@dataclass
class BlogPost:
    guid: str
    title: str
    url: str
    published_at: str | None
    author: str | None
    summary_src: str
    feed_url: str


def resolve_feed_url(blog_url: str) -> list[str]:
    """Candidate feed URLs for a blog index page."""
    base = blog_url.rstrip("/")
    # Prefer explicit rss.xml under /blog
    return [
        f"{base}/rss.xml",
        f"{base}/atom.xml",
        f"{base}/feed.xml",
        f"{base}/feed",
    ]


def _strip_html(text: str | None, limit: int = 2000) -> str:
    if not text:
        return ""
    text = unescape(_TAG_RE.sub(" ", text))
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        return text[: limit - 3] + "..."
    return text


def _local(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[-1]
    return tag


def _child_text(el: ET.Element, *names: str) -> str | None:
    want = set(names)
    for child in list(el):
        if _local(child.tag) not in want:
            continue
        if (child.text or "").strip():
            return (child.text or "").strip()
        raw = "".join(child.itertext()).strip()
        if raw:
            return raw
    return None


def _parse_date(raw: str | None) -> str | None:
    if not raw:
        return None
    raw = raw.strip()
    try:
        dt = parsedate_to_datetime(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace(
            "+00:00", "Z"
        )
    except (TypeError, ValueError, IndexError):
        pass
    try:
        # Atom often uses ISO-8601
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace(
            "+00:00", "Z"
        )
    except ValueError:
        return None


def parse_feed(xml_text: str, feed_url: str) -> list[BlogPost]:
    root = ET.fromstring(xml_text)
    root_local = _local(root.tag)
    posts: list[BlogPost] = []

    if root_local == "rss" or root.find("channel") is not None:
        channel = root.find("channel")
        if channel is None:
            channel = root
        for item in channel.findall("item"):
            title = _child_text(item, "title") or "(untitled)"
            link = _child_text(item, "link") or ""
            guid = _child_text(item, "guid") or link or title
            pub = _parse_date(_child_text(item, "pubDate", "published", "date"))
            author = _child_text(item, "creator", "author")
            # description / content:encoded
            desc = None
            for child in list(item):
                loc = _local(child.tag)
                if loc in ("description", "encoded", "summary", "content"):
                    raw = "".join(child.itertext()).strip() or (child.text or "")
                    if raw and (desc is None or len(raw) > len(desc)):
                        desc = raw
            if not link:
                continue
            posts.append(
                BlogPost(
                    guid=guid,
                    title=_strip_html(title, 300),
                    url=link,
                    published_at=pub,
                    author=_strip_html(author, 200) if author else None,
                    summary_src=_strip_html(desc, 2500),
                    feed_url=feed_url,
                )
            )
        return posts

    # Atom
    if root_local == "feed":
        for entry in root.findall("atom:entry", _NS) or root.findall(
            "{http://www.w3.org/2005/Atom}entry"
        ):
            title = _child_text(entry, "title") or "(untitled)"
            link = ""
            for child in list(entry):
                if _local(child.tag) == "link":
                    href = child.attrib.get("href") or ""
                    rel = child.attrib.get("rel", "alternate")
                    if href and rel in ("alternate", ""):
                        link = href
                        break
            if not link:
                link = _child_text(entry, "id") or ""
            guid = _child_text(entry, "id") or link or title
            pub = _parse_date(
                _child_text(entry, "published", "updated", "pubDate")
            )
            author_el = None
            for child in list(entry):
                if _local(child.tag) == "author":
                    author_el = _child_text(child, "name") or "".join(
                        child.itertext()
                    ).strip()
                    break
            desc = None
            for child in list(entry):
                if _local(child.tag) in ("summary", "content"):
                    raw = "".join(child.itertext()).strip()
                    if raw:
                        desc = raw
                        break
            if not link:
                continue
            posts.append(
                BlogPost(
                    guid=guid,
                    title=_strip_html(title, 300),
                    url=link,
                    published_at=pub,
                    author=_strip_html(author_el, 200) if author_el else None,
                    summary_src=_strip_html(desc, 2500),
                    feed_url=feed_url,
                )
            )
    return posts


def fetch_feed(
    blog_or_feed_url: str,
    *,
    client: httpx.Client | None = None,
    timeout: float = 30.0,
) -> tuple[str, list[BlogPost]]:
    """Fetch first working feed for a blog URL. Returns (feed_url, posts)."""
    owns = client is None
    client = client or httpx.Client(
        timeout=timeout,
        follow_redirects=True,
        headers={"User-Agent": "oss-project-tracker/0.1"},
    )
    candidates: list[str] = []
    parsed = urlparse(blog_or_feed_url)
    path = parsed.path.rstrip("/")
    if path.endswith((".xml", "/feed", "/rss", "/atom")):
        candidates.append(blog_or_feed_url)
    else:
        candidates.extend(resolve_feed_url(blog_or_feed_url))

    last_err: Exception | None = None
    try:
        for url in candidates:
            try:
                resp = client.get(url)
                if resp.status_code == 404:
                    continue
                resp.raise_for_status()
                ctype = (resp.headers.get("content-type") or "").lower()
                text = resp.text
                if "html" in ctype and "<rss" not in text[:500].lower() and "<feed" not in text[:500].lower():
                    continue
                posts = parse_feed(text, url)
                if posts:
                    return url, posts
            except Exception as e:  # noqa: BLE001 — try next candidate
                last_err = e
                continue
    finally:
        if owns:
            client.close()

    if last_err:
        raise RuntimeError(
            f"Could not fetch blog feed for {blog_or_feed_url}: {last_err}"
        )
    raise RuntimeError(f"No blog feed items found for {blog_or_feed_url}")

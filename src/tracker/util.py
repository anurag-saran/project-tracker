"""Shared utilities."""

from __future__ import annotations

import fnmatch
import hashlib
import json
import re
from datetime import datetime, timedelta, timezone
from typing import Any


def parse_since(value: str) -> datetime:
    """Parse '7d', '2w', ISO date, or datetime into aware UTC datetime."""
    value = value.strip()
    m = re.fullmatch(r"(\d+)([dhmsw])", value)
    if m:
        n = int(m.group(1))
        unit = m.group(2)
        delta = {
            "s": timedelta(seconds=n),
            "m": timedelta(minutes=n),
            "h": timedelta(hours=n),
            "d": timedelta(days=n),
            "w": timedelta(weeks=n),
        }[unit]
        return datetime.now(timezone.utc) - delta
    # date only
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        dt = datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return dt
    # ISO
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def to_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def content_hash(*parts: Any) -> str:
    payload = json.dumps(parts, sort_keys=True, default=str)
    return hashlib.sha256(payload.encode()).hexdigest()[:16]


def match_paths(file_paths: list[str], globs: list[str]) -> bool:
    for fp in file_paths:
        for g in globs:
            # support ** globs via fnmatch after normalizing
            pattern = g
            if fnmatch.fnmatch(fp, pattern):
                return True
            # also try without leading **/
            if pattern.startswith("**/") and fnmatch.fnmatch(fp, pattern[3:]):
                return True
            # directory prefix: foo/** matches foo/bar/baz
            if pattern.endswith("/**"):
                prefix = pattern[:-3]
                if fp == prefix or fp.startswith(prefix + "/"):
                    return True
    return False


def classify_pr(title: str, labels: list[str], body: str | None = None) -> str:
    """Heuristic bucket: features|performance|fixes|breaking|infra."""
    text = f"{title} {' '.join(labels)} {body or ''}".lower()
    if any(
        k in text
        for k in ("break", "deprecat", "移除", "incompatible", "migration")
    ):
        return "breaking"
    if any(k in text for k in ("perf", "performance", "latency", "throughput", "optim")):
        return "performance"
    if any(k in text for k in ("fix", "bug", "hotfix", "revert")):
        return "fixes"
    if any(
        k in text
        for k in ("ci", "infra", "build", "chore", "dependabot", "docker", "helm")
    ):
        return "infra"
    if any(k in text for k in ("feat", "feature", "add ", "support", "implement")):
        return "features"
    return "features"


def trim_body(body: str | None, limit: int = 800) -> str:
    if not body:
        return ""
    body = body.strip()
    if len(body) <= limit:
        return body
    return body[: limit - 3] + "..."

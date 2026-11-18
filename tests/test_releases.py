"""Release feature extraction + report tests."""

from __future__ import annotations

from pathlib import Path

from tracker.config import load_config
from tracker.db import Database
from tracker.stages.releases import build_releases, extract_feature_bullets


SAMPLE_NOTES = """
# v0.34.0

## TL;DR
- 10 new models (Mistral Large 4 and more)
- Extensible KV cache is on by default
- Model Runner V2 is now the only GPU runner

## Features
- Blackwell speedups up to 1.95× decode
- Default block size is now 64

## Bug Fixes
- Fix crash on empty batch
"""


def test_extract_feature_bullets():
    bullets = extract_feature_bullets(SAMPLE_NOTES)
    assert any("new models" in b.lower() for b in bullets)
    assert any("kv cache" in b.lower() for b in bullets)
    assert not any("empty batch" in b.lower() for b in bullets)


def test_build_releases_report(tmp_workspace: Path, db: Database):
    root = Path(__file__).resolve().parents[1]
    cfg = load_config(root / "projects.yaml")
    repo_id = db.upsert_repo(
        "vllm",
        "vllm-project/vllm",
        "core",
        description="engine",
        stars=1,
    )
    db.upsert_release(
        repo_id,
        "v0.34.0",
        name="v0.34.0",
        body=SAMPLE_NOTES,
        published_at="2026-11-16T00:00:00Z",
        url="https://github.com/vllm-project/vllm/releases/tag/v0.34.0",
    )
    db.upsert_release(
        repo_id,
        "v0.35.0-rc1",
        name="v0.35.0-rc1",
        body="## Features\n- Upcoming flash attention path\n",
        published_at="2026-11-17T00:00:00Z",
        url="https://github.com/vllm-project/vllm/releases/tag/v0.35.0-rc1",
    )
    db.upsert_issue(
        repo_id,
        {
            "id": 99,
            "number": 51,
            "title": "[Roadmap] Q4 goals",
            "body": "- [ ] Multimodal",
            "state": "OPEN",
            "author": "x",
            "labels": ["roadmap"],
            "url": "https://github.com/vllm-project/vllm/issues/51",
            "signal": "roadmap",
        },
    )
    db.commit()

    out = build_releases(
        db,
        cfg,
        "vllm",
        client=None,
        dry_run=True,
        workspace=tmp_workspace,
        release_limit=3,
    )
    text = out.read_text()
    assert "v0.34.0" in text
    assert "Shipped" in text
    assert "Next community release" in text
    assert "docs.vllm.ai" in text
    assert "v0.35.0-rc1" in text or "Roadmap" in text
    assert (tmp_workspace / "reports" / "vllm" / "latest-releases.md").exists()

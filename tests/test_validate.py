"""Validate / util / digest dry-run tests."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from tracker.config import load_config
from tracker.db import Database
from tracker.stages.digest import build_digest
from tracker.stages.pipeline import build_pipeline
from tracker.stages.people import build_people
from tracker.util import classify_pr, match_paths, parse_since


def test_parse_since():
    dt = parse_since("7d")
    assert dt.tzinfo is not None
    assert (datetime.now(timezone.utc) - dt).days >= 6


def test_match_paths():
    assert match_paths(["vllm/v1/core/scheduler.py"], ["vllm/v1/core/**"])
    assert not match_paths(["docs/index.md"], ["vllm/v1/core/**"])


def test_classify_pr():
    assert classify_pr("fix: crash", ["bug"], None) == "fixes"
    assert classify_pr("feat: new API", [], None) == "features"


def test_digest_and_pipeline_from_sqlite(tmp_workspace: Path, db: Database):
    # Seed config
    root = Path(__file__).resolve().parents[1]
    cfg = load_config(root / "projects.yaml")

    repo_id = db.upsert_repo(
        "vllm",
        "vllm-project/vllm",
        "core",
        description="engine",
        default_branch="main",
        stars=1,
        activity_90d=2,
        latest_release_tag="v0.6.0",
        latest_release_at="2025-10-15T00:00:00Z",
    )
    db.replace_modules(
        repo_id,
        [
            {
                "name": "v1-core",
                "paths": ["vllm/v1/core/**"],
                "source": "config",
            }
        ],
    )
    db.upsert_release(
        repo_id,
        "v0.6.0",
        name="v0.6.0",
        published_at="2025-10-15T00:00:00Z",
        url="https://example.com/r",
    )
    db.upsert_pr(
        repo_id,
        {
            "id": 1,
            "number": 100,
            "title": "feat: faster scheduler",
            "body": "Improves throughput",
            "state": "MERGED",
            "author": "alice",
            "labels": ["performance"],
            "merged_at": "2025-10-30T00:00:00Z",
            "updated_at": "2025-10-30T00:00:00Z",
            "created_at": "2025-10-28T00:00:00Z",
            "additions": 120,
            "deletions": 40,
            "changed_files": 5,
            "files": [
                {
                    "path": "vllm/v1/core/scheduler.py",
                    "additions": 80,
                    "deletions": 20,
                }
            ],
            "url": "https://github.com/vllm-project/vllm/pull/100",
        },
    )
    db.upsert_issue(
        repo_id,
        {
            "id": 10,
            "number": 50,
            "title": "[RFC] Pluggable scheduler",
            "body": "- [x] Design\n- [ ] Impl",
            "state": "OPEN",
            "author": "erin",
            "labels": ["RFC"],
            "created_at": "2025-10-20T00:00:00Z",
            "updated_at": "2025-11-01T00:00:00Z",
            "comments_count": 8,
            "reactions_count": 5,
            "url": "https://github.com/vllm-project/vllm/issues/50",
            "signal": "rfc",
        },
    )
    db.upsert_pr(
        repo_id,
        {
            "id": 3,
            "number": 200,
            "title": "[RFC] New KV cache layout",
            "body": "Large redesign",
            "state": "OPEN",
            "author": "carol",
            "labels": ["RFC"],
            "updated_at": "2025-11-01T00:00:00Z",
            "created_at": "2025-10-01T00:00:00Z",
            "additions": 800,
            "deletions": 100,
            "changed_files": 40,
            "files": [{"path": "vllm/v1/core/kv.py"}],
            "reviewers": [{"login": "alice", "state": "COMMENTED"}],
            "url": "https://github.com/vllm-project/vllm/pull/200",
        },
    )
    db.replace_ownership(
        repo_id,
        [
            {
                "path_pattern": "*",
                "owners": ["@vllm-project/maintainers"],
                "source": "codeowners",
            },
            {
                "path_pattern": "vllm/v1/core/**",
                "owners": ["@alice"],
                "source": "codeowners",
            },
        ],
    )
    db.commit()

    digest_path = build_digest(
        db,
        cfg,
        "vllm",
        since="2025-01-01",
        dry_run=True,
        workspace=tmp_workspace,
    )
    assert digest_path.exists()
    text = digest_path.read_text()
    assert "TL;DR" in text
    assert "v1-core" in text or "#100" in text

    pipe_path = build_pipeline(
        db,
        cfg,
        "vllm",
        since="2025-01-01",
        dry_run=True,
        workspace=tmp_workspace,
    )
    assert pipe_path.exists()
    ptext = pipe_path.read_text()
    assert "RFC" in ptext or "Pluggable" in ptext

    people_path = build_people(db, cfg, "vllm", workspace=tmp_workspace)
    assert people_path.exists()
    assert "alice" in people_path.read_text()

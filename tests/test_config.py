"""Config schema tests."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from tracker.config import (
    OrgSource,
    RootConfig,
    Tier,
    effective_tier,
    load_config,
    parse_proposals_dir,
)


def test_load_seed_projects_yaml():
    root = Path(__file__).resolve().parents[1]
    cfg = load_config(root / "projects.yaml")
    assert isinstance(cfg, RootConfig)
    assert cfg.settings.max_repos_per_org == 25
    names = cfg.project_names()
    assert "vllm" in names
    assert "llm-d" in names
    vllm = cfg.get_project("vllm")
    assert any(isinstance(s, OrgSource) and s.org == "vllm-project" for s in vllm.sources)
    repos = vllm.repo_sources()
    assert repos[0].repo == "vllm-project/vllm"
    assert repos[0].tier == Tier.CORE


def test_effective_tier_inheritance():
    assert effective_tier(repo_tier=Tier.CORE, org_tier=Tier.WATCH, project_tier=None) == Tier.CORE
    assert effective_tier(repo_tier=None, org_tier=Tier.WATCH, project_tier=None) == Tier.WATCH
    assert effective_tier(repo_tier=None, org_tier=None, project_tier=None) == Tier.WATCH


def test_org_include_exclude():
    src = OrgSource(org="acme", include=["*"], exclude=["*-archived"])
    assert src.matches("foo")
    assert not src.matches("foo-archived")


def test_parse_proposals_dir():
    assert parse_proposals_dir("llm-d/llm-d:<discover>") == (
        "llm-d/llm-d",
        "<discover>",
    )
    assert parse_proposals_dir("docs/proposals") == (None, "docs/proposals")


def test_invalid_project_name(tmp_path: Path):
    p = tmp_path / "projects.yaml"
    p.write_text(
        yaml.safe_dump(
            {
                "projects": [
                    {
                        "name": "Bad Name",
                        "sources": [{"repo": "a/b"}],
                    }
                ]
            }
        )
    )
    with pytest.raises(Exception):
        load_config(p)

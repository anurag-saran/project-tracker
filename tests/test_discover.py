"""Discover / resolve / module proposal tests."""

from __future__ import annotations

from tracker.config import ProjectConfig, OrgSource, RepoSource, Tier
from tracker.github.client import GitHubClient
from tracker.github.discover import (
    parse_codeowners,
    propose_modules,
    resolve_project_repos,
)


def test_resolve_skips_archived_and_marks_core(gh_client: GitHubClient):
    project = ProjectConfig(
        name="vllm",
        sources=[
            OrgSource(org="vllm-project", skip_archived=True),
            RepoSource(repo="vllm-project/vllm", tier=Tier.CORE),
        ],
    )
    repos, findings = resolve_project_repos(
        gh_client, project, max_repos_per_org=25, compute_activity=True
    )
    assert any(f.level == "ok" and "org:vllm-project" in f.subject for f in findings)
    by_name = {r.full_name: r for r in repos}
    assert "vllm-project/old-thing" not in by_name
    assert by_name["vllm-project/vllm"].tier == Tier.CORE
    assert "vllm-project/docs" in by_name
    assert by_name["vllm-project/docs"].tier == Tier.WATCH


def test_propose_modules(gh_client: GitHubClient):
    mods = propose_modules(gh_client, "vllm-project/vllm")
    names = {m.name for m in mods}
    assert "vllm" in names or any(n.startswith("vllm") for n in names)
    # v1 submodules expected from tree fixtures
    assert any("v1" in n for n in names)


def test_parse_codeowners():
    text = """
# comment
* @team
/vllm/engine/** @alice @bob
"""
    entries = parse_codeowners(text)
    assert entries[0] == ("*", ["@team"])
    assert entries[1][0] == "/vllm/engine/**"
    assert "@alice" in entries[1][1]

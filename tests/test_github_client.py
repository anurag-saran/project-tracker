"""GitHub client tests against recorded fixtures (no network)."""

from __future__ import annotations

from tracker.github.client import GitHubClient


def test_list_org_repos(gh_client: GitHubClient):
    repos = gh_client.list_org_repos("vllm-project")
    names = {r["nameWithOwner"] for r in repos}
    assert "vllm-project/vllm" in names
    assert "vllm-project/docs" in names


def test_get_repo_meta(gh_client: GitHubClient):
    meta = gh_client.get_repo("vllm-project", "vllm")
    assert meta is not None
    assert meta["latestRelease"]["tagName"] == "v0.6.0"


def test_iter_merged_prs(gh_client: GitHubClient):
    prs = list(gh_client.iter_merged_prs("vllm-project", "vllm"))
    assert len(prs) == 2
    assert prs[0]["number"] == 100
    assert prs[0]["state"] == "MERGED"
    assert any(f["path"].endswith("scheduler.py") for f in prs[0]["files"])


def test_iter_open_prs_includes_reviewers(gh_client: GitHubClient):
    prs = list(gh_client.iter_open_prs("vllm-project", "vllm"))
    assert len(prs) == 1
    assert prs[0]["number"] == 200
    logins = {r["login"] for r in prs[0]["reviewers"]}
    assert "alice" in logins


def test_get_file_text_codeowners(gh_client: GitHubClient):
    text = gh_client.get_file_text(
        "vllm-project", "vllm", ".github/CODEOWNERS"
    )
    assert text is not None
    assert "@vllm-project/maintainers" in text


def test_cache_roundtrip(gh_client: GitHubClient, db):
    gh_client.list_org_repos("vllm-project")
    # second call should hit cache path (still works)
    repos = gh_client.list_org_repos("vllm-project")
    assert repos
    assert db.execute("SELECT COUNT(*) AS c FROM cache_entries").fetchone()["c"] >= 1

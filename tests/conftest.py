"""Shared fixtures."""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

from tracker.db import Database
from tracker.github.client import GitHubClient

FIXTURES = Path(__file__).parent / "fixtures" / "github"


class FixtureTransport(httpx.BaseTransport):
    """Map GitHub API calls to recorded JSON fixtures (no network)."""

    def __init__(self, mapping: dict[str, Path] | None = None):
        self.mapping = mapping or {}
        self.calls: list[tuple[str, str]] = []

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.calls.append((request.method, str(request.url)))
        if request.url.path.endswith("/graphql"):
            body = json.loads(request.content.decode())
            query = body.get("query", "")
            variables = body.get("variables") or {}
            name = self._graphql_fixture_name(query, variables)
            path = FIXTURES / f"{name}.json"
            if not path.exists():
                return httpx.Response(
                    200,
                    json={"data": {}},
                    request=request,
                )
            return httpx.Response(
                200, json=json.loads(path.read_text()), request=request
            )

        # REST
        key = request.url.path.strip("/")
        # normalize /repos/owner/name/contents/...
        safe = key.replace("/", "_")
        path = FIXTURES / f"rest_{safe}.json"
        if path.exists():
            data = json.loads(path.read_text())
            return httpx.Response(200, json=data, request=request)
        return httpx.Response(404, json={"message": "Not Found"}, request=request)

    @staticmethod
    def _graphql_fixture_name(query: str, variables: dict) -> str:
        q = " ".join(query.split())
        if "organization(login" in q and "repositories" in q:
            return f"org_repos_{variables.get('org', 'unknown')}"
        if "latestRelease" in q:
            return f"repo_meta_{variables.get('owner')}_{variables.get('name')}"
        if "mergedRecent" in q:
            return f"repo_activity_{variables.get('owner')}_{variables.get('name')}"
        if "states: MERGED" in q.replace("\n", " ") and "files(" in q:
            return f"merged_prs_{variables.get('owner')}_{variables.get('name')}"
        if "states: OPEN" in q.replace("\n", " "):
            return f"open_prs_{variables.get('owner')}_{variables.get('name')}"
        if "issues(" in q:
            return f"issues_{variables.get('owner')}_{variables.get('name')}"
        if "releases(" in q:
            return f"releases_{variables.get('owner')}_{variables.get('name')}"
        if "expression" in q and "entries" in q:
            expr = variables.get("expression", "")
            safe = expr.replace(":", "_").replace("/", "_").replace(".", "_")
            return f"tree_{variables.get('owner')}_{variables.get('name')}_{safe}"
        if "expression" in q:
            expr = variables.get("expression", "")
            safe = expr.replace(":", "_").replace("/", "_").replace(".", "_")
            return f"path_{variables.get('owner')}_{variables.get('name')}_{safe}"
        return "graphql_default"


@pytest.fixture
def tmp_workspace(tmp_path: Path) -> Path:
    (tmp_path / "prompts").mkdir()
    for name in ("digest.md", "module_map.md", "pipeline.md"):
        src = Path(__file__).resolve().parents[1] / "prompts" / name
        if src.exists():
            (tmp_path / "prompts" / name).write_text(src.read_text())
        else:
            (tmp_path / "prompts" / name).write_text(f"# {name}\nYou are a helper.\n")
    return tmp_path


@pytest.fixture
def db(tmp_workspace: Path) -> Database:
    return Database(tmp_workspace / ".tracker" / "tracker.db")


@pytest.fixture
def gh_transport() -> FixtureTransport:
    return FixtureTransport()


@pytest.fixture
def gh_client(gh_transport: FixtureTransport, db: Database) -> GitHubClient:
    return GitHubClient(
        token="test-token",
        db=db,
        transport=gh_transport,
        sleep_fn=lambda _s: None,
        max_retries=2,
    )

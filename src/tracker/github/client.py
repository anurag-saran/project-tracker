"""GitHub GraphQL + REST client with pagination, backoff, and ETag cache."""

from __future__ import annotations

import hashlib
import json
import os
import time
from typing import Any, Callable

import httpx

from tracker.db import Database
from tracker.github import queries as Q


class GitHubError(RuntimeError):
    pass


class GitHubClient:
    GRAPHQL_URL = "https://api.github.com/graphql"
    REST_URL = "https://api.github.com"

    def __init__(
        self,
        token: str | None = None,
        *,
        db: Database | None = None,
        transport: httpx.BaseTransport | None = None,
        sleep_fn: Callable[[float], None] | None = None,
        max_retries: int = 8,
    ):
        self.token = token or os.environ.get("GITHUB_TOKEN")
        if not self.token:
            raise GitHubError(
                "GITHUB_TOKEN is required. Export a personal access token."
            )
        self.db = db
        self.max_retries = max_retries
        self._sleep = sleep_fn or time.sleep
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "oss-project-tracker",
        }
        self._client = httpx.Client(
            headers=headers,
            timeout=60.0,
            transport=transport,
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> GitHubClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    # --- low-level ---

    def _cache_key(self, kind: str, payload: str) -> str:
        digest = hashlib.sha256(payload.encode()).hexdigest()
        return f"{kind}:{digest}"

    def _request_with_backoff(
        self,
        method: str,
        url: str,
        *,
        json_body: dict | None = None,
        headers: dict | None = None,
        use_etag_key: str | None = None,
    ) -> tuple[int, dict[str, str], bytes]:
        extra = dict(headers or {})
        if use_etag_key and self.db:
            cached = self.db.get_cache(use_etag_key)
            if cached and cached[0]:
                extra["If-None-Match"] = cached[0]

        delay = 1.0
        last_exc: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                resp = self._client.request(
                    method, url, json=json_body, headers=extra
                )
            except httpx.HTTPError as e:
                last_exc = e
                self._sleep(delay)
                delay = min(delay * 2, 60)
                continue

            if resp.status_code == 304 and use_etag_key and self.db:
                cached = self.db.get_cache(use_etag_key)
                if cached:
                    return 304, dict(resp.headers), cached[1]

            if resp.status_code in (403, 429):
                reset = resp.headers.get("X-RateLimit-Reset")
                retry_after = resp.headers.get("Retry-After")
                if retry_after:
                    wait = float(retry_after)
                elif reset:
                    wait = max(float(reset) - time.time(), delay)
                else:
                    wait = delay
                self._sleep(min(wait, 120))
                delay = min(delay * 2, 60)
                continue

            if resp.status_code >= 500:
                self._sleep(delay)
                delay = min(delay * 2, 60)
                continue

            body = resp.content
            if use_etag_key and self.db and resp.status_code == 200:
                self.db.set_cache(
                    use_etag_key, body, etag=resp.headers.get("ETag")
                )
            return resp.status_code, dict(resp.headers), body

        raise GitHubError(
            f"GitHub request failed after retries: {method} {url} ({last_exc})"
        )

    def graphql(
        self, query: str, variables: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        variables = variables or {}
        cache_payload = json.dumps(
            {"q": query, "v": variables}, sort_keys=True
        )
        key = self._cache_key("graphql", cache_payload)
        status, _headers, body = self._request_with_backoff(
            "POST",
            self.GRAPHQL_URL,
            json_body={"query": query, "variables": variables},
            use_etag_key=key,
        )
        data = json.loads(body)
        if "errors" in data and not data.get("data"):
            raise GitHubError(f"GraphQL errors: {data['errors']}")
        return data.get("data") or {}

    def rest_get(
        self, path: str, *, params: dict | None = None
    ) -> tuple[int, Any]:
        url = path if path.startswith("http") else f"{self.REST_URL}{path}"
        if params:
            q = "&".join(f"{k}={v}" for k, v in params.items())
            url = f"{url}?{q}"
        key = self._cache_key("rest", url)
        status, _headers, body = self._request_with_backoff(
            "GET", url, use_etag_key=key
        )
        if status == 404:
            return 404, None
        if status == 304:
            return 304, json.loads(body) if body else None
        if status >= 400:
            raise GitHubError(f"REST {status}: {body[:200]!r}")
        return status, json.loads(body) if body else None

    # --- high-level helpers ---

    def list_org_repos(self, org: str) -> list[dict[str, Any]]:
        repos: list[dict[str, Any]] = []
        cursor = None
        while True:
            data = self.graphql(
                Q.ORG_REPOS, {"org": org, "cursor": cursor}
            )
            organization = data.get("organization")
            if organization is None:
                raise GitHubError(f"organization not found: {org}")
            conn = organization["repositories"]
            for node in conn["nodes"] or []:
                if node:
                    repos.append(node)
            if not conn["pageInfo"]["hasNextPage"]:
                break
            cursor = conn["pageInfo"]["endCursor"]
        return repos

    def get_repo(self, owner: str, name: str) -> dict[str, Any] | None:
        data = self.graphql(Q.REPO_META, {"owner": owner, "name": name})
        return data.get("repository")

    def count_merged_since(
        self, owner: str, name: str, since_iso: str
    ) -> int:
        """Approximate activity: count merged PRs with mergedAt >= since among recent page."""
        data = self.graphql(
            Q.REPO_ACTIVITY,
            {"owner": owner, "name": name, "since": since_iso},
        )
        repo = data.get("repository")
        if not repo:
            return 0
        count = 0
        for n in (repo.get("mergedRecent") or {}).get("nodes") or []:
            merged = (n or {}).get("mergedAt")
            if merged and merged >= since_iso:
                count += 1
        return count

    def iter_merged_prs(
        self,
        owner: str,
        name: str,
        *,
        since_iso: str | None = None,
        max_pages: int = 20,
    ):
        cursor = None
        for _ in range(max_pages):
            data = self.graphql(
                Q.MERGED_PRS, {"owner": owner, "name": name, "cursor": cursor}
            )
            repo = data.get("repository")
            if not repo:
                return
            conn = repo["pullRequests"]
            stop = False
            for node in conn["nodes"] or []:
                if not node:
                    continue
                if since_iso and node.get("mergedAt") and node["mergedAt"] < since_iso:
                    stop = True
                    break
                yield self._normalize_pr(node)
            if stop or not conn["pageInfo"]["hasNextPage"]:
                return
            cursor = conn["pageInfo"]["endCursor"]

    def iter_open_prs(
        self, owner: str, name: str, *, max_pages: int = 10
    ):
        cursor = None
        for _ in range(max_pages):
            data = self.graphql(
                Q.OPEN_PRS, {"owner": owner, "name": name, "cursor": cursor}
            )
            repo = data.get("repository")
            if not repo:
                return
            conn = repo["pullRequests"]
            for node in conn["nodes"] or []:
                if node:
                    yield self._normalize_pr(node, include_reviews=True)
            if not conn["pageInfo"]["hasNextPage"]:
                return
            cursor = conn["pageInfo"]["endCursor"]

    def iter_issues(
        self,
        owner: str,
        name: str,
        *,
        since_iso: str | None = None,
        max_pages: int = 15,
    ):
        cursor = None
        for _ in range(max_pages):
            data = self.graphql(
                Q.REPO_ISSUES, {"owner": owner, "name": name, "cursor": cursor}
            )
            repo = data.get("repository")
            if not repo:
                return
            conn = repo["issues"]
            stop = False
            for node in conn["nodes"] or []:
                if not node:
                    continue
                if since_iso and node.get("updatedAt") and node["updatedAt"] < since_iso:
                    stop = True
                    break
                yield self._normalize_issue(node)
            if stop or not conn["pageInfo"]["hasNextPage"]:
                return
            cursor = conn["pageInfo"]["endCursor"]

    def list_releases(
        self, owner: str, name: str, *, max_pages: int = 3
    ) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        cursor = None
        for _ in range(max_pages):
            data = self.graphql(
                Q.RELEASES, {"owner": owner, "name": name, "cursor": cursor}
            )
            repo = data.get("repository")
            if not repo:
                break
            conn = repo["releases"]
            for node in conn["nodes"] or []:
                if node and not node.get("isDraft"):
                    out.append(
                        {
                            "tag": node.get("tagName"),
                            "name": node.get("name"),
                            "body": node.get("description"),
                            "published_at": node.get("publishedAt"),
                            "url": node.get("url"),
                            "is_prerelease": bool(node.get("isPrerelease")),
                        }
                    )
            if not conn["pageInfo"]["hasNextPage"]:
                break
            cursor = conn["pageInfo"]["endCursor"]
        return out

    def list_milestones(self, owner: str, name: str) -> list[dict[str, Any]]:
        data = self.graphql(Q.MILESTONES, {"owner": owner, "name": name})
        repo = data.get("repository") or {}
        nodes = ((repo.get("milestones") or {}).get("nodes")) or []
        out: list[dict[str, Any]] = []
        for n in nodes:
            if not n:
                continue
            out.append(
                {
                    "title": n.get("title"),
                    "description": n.get("description"),
                    "due_on": n.get("dueOn"),
                    "url": n.get("url"),
                    "open_issues": (n.get("openIssueCount") or {}).get(
                        "totalCount", 0
                    ),
                    "closed_issues": (n.get("closedIssueCount") or {}).get(
                        "totalCount", 0
                    ),
                    "open_prs": (n.get("openPrCount") or {}).get("totalCount", 0),
                }
            )
        return out

    def get_tree_entries(
        self, owner: str, name: str, path: str = "", branch: str = "HEAD"
    ) -> list[dict[str, Any]]:
        expr = f"{branch}:{path}" if path else f"{branch}:"
        data = self.graphql(
            Q.TREE_ENTRIES,
            {"owner": owner, "name": name, "expression": expr},
        )
        repo = data.get("repository") or {}
        obj = repo.get("object")
        if not obj or "entries" not in obj:
            return []
        return obj["entries"] or []

    def path_exists(
        self, owner: str, name: str, path: str, branch: str = "HEAD"
    ) -> bool:
        data = self.graphql(
            Q.PATH_EXISTS,
            {
                "owner": owner,
                "name": name,
                "expression": f"{branch}:{path}",
            },
        )
        repo = data.get("repository") or {}
        return repo.get("object") is not None

    def get_file_text(
        self, owner: str, name: str, path: str, branch: str = "HEAD"
    ) -> str | None:
        data = self.graphql(
            Q.TREE_ENTRIES,
            {
                "owner": owner,
                "name": name,
                "expression": f"{branch}:{path}",
            },
        )
        repo = data.get("repository") or {}
        obj = repo.get("object")
        if not obj:
            return None
        if "text" in obj and obj.get("text") is not None:
            return obj["text"]
        # directory — not a file
        return None

    def list_dir_files(
        self, owner: str, name: str, path: str, branch: str = "HEAD"
    ) -> list[dict[str, Any]]:
        """List files under a directory via REST contents API (recursive shallow)."""
        status, body = self.rest_get(
            f"/repos/{owner}/{name}/contents/{path}",
            params={"ref": branch} if branch != "HEAD" else None,
        )
        if status == 404 or body is None:
            return []
        if isinstance(body, dict):
            return [
                {
                    "path": body.get("path"),
                    "sha": body.get("sha"),
                    "url": body.get("html_url"),
                    "type": body.get("type"),
                }
            ]
        out = []
        for item in body:
            out.append(
                {
                    "path": item.get("path"),
                    "sha": item.get("sha"),
                    "url": item.get("html_url"),
                    "type": item.get("type"),
                }
            )
            if item.get("type") == "dir":
                out.extend(
                    self.list_dir_files(
                        owner, name, item["path"], branch=branch
                    )
                )
        return out

    @staticmethod
    def _normalize_pr(
        node: dict[str, Any], *, include_reviews: bool = False
    ) -> dict[str, Any]:
        labels = [
            n["name"]
            for n in ((node.get("labels") or {}).get("nodes") or [])
            if n
        ]
        files = [
            {
                "path": f["path"],
                "additions": f.get("additions"),
                "deletions": f.get("deletions"),
            }
            for f in ((node.get("files") or {}).get("nodes") or [])
            if f
        ]
        out: dict[str, Any] = {
            "id": node.get("databaseId"),
            "number": node["number"],
            "title": node["title"],
            "body": (node.get("body") or "")[:4000],
            "state": "MERGED"
            if node.get("mergedAt")
            else (node.get("state") or "OPEN"),
            "author": ((node.get("author") or {}) or {}).get("login"),
            "labels": labels,
            "merged_at": node.get("mergedAt"),
            "closed_at": node.get("closedAt"),
            "updated_at": node.get("updatedAt"),
            "created_at": node.get("createdAt"),
            "additions": node.get("additions"),
            "deletions": node.get("deletions"),
            "changed_files": node.get("changedFiles"),
            "files": files,
            "url": node.get("url"),
        }
        if include_reviews:
            reviewers = []
            for r in ((node.get("reviews") or {}).get("nodes") or []):
                login = ((r.get("author") or {}) or {}).get("login")
                if login:
                    reviewers.append(
                        {"login": login, "state": r.get("state")}
                    )
            out["reviewers"] = reviewers
            out["comments_count"] = (node.get("comments") or {}).get(
                "totalCount", 0
            )
        return out

    @staticmethod
    def _normalize_issue(node: dict[str, Any]) -> dict[str, Any]:
        labels = [
            n["name"]
            for n in ((node.get("labels") or {}).get("nodes") or [])
            if n
        ]
        return {
            "id": node.get("databaseId"),
            "number": node["number"],
            "title": node["title"],
            "body": (node.get("body") or "")[:4000],
            "state": node.get("state") or "OPEN",
            "author": ((node.get("author") or {}) or {}).get("login"),
            "labels": labels,
            "created_at": node.get("createdAt"),
            "updated_at": node.get("updatedAt"),
            "closed_at": node.get("closedAt"),
            "comments_count": (node.get("comments") or {}).get(
                "totalCount", 0
            ),
            "reactions_count": (node.get("reactions") or {}).get(
                "totalCount", 0
            ),
            "url": node.get("url"),
        }

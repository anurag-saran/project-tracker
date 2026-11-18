"""SQLite schema and helpers."""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

SCHEMA_VERSION = 2

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS runs (
  id INTEGER PRIMARY KEY,
  command TEXT NOT NULL,
  project TEXT NOT NULL,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  since TEXT,
  status TEXT NOT NULL,
  stats_json TEXT
);

CREATE TABLE IF NOT EXISTS repos (
  id INTEGER PRIMARY KEY,
  project TEXT NOT NULL,
  full_name TEXT NOT NULL,
  tier TEXT NOT NULL,
  description TEXT,
  default_branch TEXT,
  is_archived INTEGER NOT NULL DEFAULT 0,
  stars INTEGER DEFAULT 0,
  pushed_at TEXT,
  latest_release_tag TEXT,
  latest_release_at TEXT,
  activity_90d INTEGER DEFAULT 0,
  UNIQUE(project, full_name)
);

CREATE TABLE IF NOT EXISTS modules (
  id INTEGER PRIMARY KEY,
  repo_id INTEGER NOT NULL REFERENCES repos(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  paths_json TEXT NOT NULL,
  source TEXT NOT NULL,
  UNIQUE(repo_id, name)
);

CREATE TABLE IF NOT EXISTS cache_entries (
  key TEXT PRIMARY KEY,
  etag TEXT,
  fetched_at TEXT NOT NULL,
  body BLOB NOT NULL
);

CREATE TABLE IF NOT EXISTS releases (
  id INTEGER PRIMARY KEY,
  repo_id INTEGER NOT NULL REFERENCES repos(id) ON DELETE CASCADE,
  tag TEXT NOT NULL,
  name TEXT,
  body TEXT,
  published_at TEXT,
  url TEXT,
  UNIQUE(repo_id, tag)
);

CREATE TABLE IF NOT EXISTS pull_requests (
  id INTEGER PRIMARY KEY,
  repo_id INTEGER NOT NULL REFERENCES repos(id) ON DELETE CASCADE,
  number INTEGER NOT NULL,
  title TEXT NOT NULL,
  body TEXT,
  state TEXT NOT NULL,
  author TEXT,
  labels_json TEXT,
  merged_at TEXT,
  closed_at TEXT,
  updated_at TEXT,
  created_at TEXT,
  additions INTEGER,
  deletions INTEGER,
  changed_files INTEGER,
  files_json TEXT,
  reviewers_json TEXT,
  url TEXT,
  UNIQUE(repo_id, number)
);

CREATE TABLE IF NOT EXISTS issues (
  id INTEGER PRIMARY KEY,
  repo_id INTEGER NOT NULL REFERENCES repos(id) ON DELETE CASCADE,
  number INTEGER NOT NULL,
  title TEXT NOT NULL,
  body TEXT,
  state TEXT NOT NULL,
  author TEXT,
  labels_json TEXT,
  created_at TEXT,
  updated_at TEXT,
  closed_at TEXT,
  comments_count INTEGER DEFAULT 0,
  reactions_count INTEGER DEFAULT 0,
  url TEXT,
  signal TEXT,
  UNIQUE(repo_id, number)
);

CREATE TABLE IF NOT EXISTS proposal_files (
  id INTEGER PRIMARY KEY,
  repo_id INTEGER NOT NULL REFERENCES repos(id) ON DELETE CASCADE,
  path TEXT NOT NULL,
  sha TEXT,
  last_modified_at TEXT,
  url TEXT,
  UNIQUE(repo_id, path)
);

CREATE TABLE IF NOT EXISTS ownership (
  id INTEGER PRIMARY KEY,
  repo_id INTEGER NOT NULL REFERENCES repos(id) ON DELETE CASCADE,
  module_id INTEGER REFERENCES modules(id) ON DELETE SET NULL,
  path_pattern TEXT NOT NULL,
  owners_json TEXT NOT NULL,
  source TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS summaries (
  id INTEGER PRIMARY KEY,
  kind TEXT NOT NULL,
  subject_key TEXT NOT NULL,
  source_hash TEXT NOT NULL,
  model TEXT,
  content TEXT NOT NULL,
  created_at TEXT NOT NULL,
  tokens_in INTEGER,
  tokens_out INTEGER,
  UNIQUE(kind, subject_key, source_hash)
);

CREATE TABLE IF NOT EXISTS sync_state (
  key TEXT PRIMARY KEY,
  cursor TEXT,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS blog_posts (
  id INTEGER PRIMARY KEY,
  project TEXT NOT NULL,
  feed_url TEXT NOT NULL,
  guid TEXT NOT NULL,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  published_at TEXT,
  author TEXT,
  summary_src TEXT,
  summary TEXT,
  UNIQUE(project, guid)
);

CREATE INDEX IF NOT EXISTS idx_prs_repo_merged ON pull_requests(repo_id, merged_at);
CREATE INDEX IF NOT EXISTS idx_issues_repo_signal ON issues(repo_id, signal);
CREATE INDEX IF NOT EXISTS idx_repos_project ON repos(project);
CREATE INDEX IF NOT EXISTS idx_blog_posts_project_pub
  ON blog_posts(project, published_at);
"""


def utcnow() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class Database:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(path))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA foreign_keys = ON")
        self.init_schema()

    def init_schema(self) -> None:
        version = self._conn.execute("PRAGMA user_version").fetchone()[0]
        if version < SCHEMA_VERSION:
            self._conn.executescript(SCHEMA_SQL)
            self._conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
            self._conn.commit()
        # Lightweight forward-compatible column adds / new tables
        cols = {
            r["name"]
            for r in self.execute("PRAGMA table_info(pull_requests)").fetchall()
        }
        if "reviewers_json" not in cols:
            self.execute(
                "ALTER TABLE pull_requests ADD COLUMN reviewers_json TEXT"
            )
            self.commit()
        tables = {
            r[0]
            for r in self.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        }
        if "blog_posts" not in tables:
            self._conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS blog_posts (
                  id INTEGER PRIMARY KEY,
                  project TEXT NOT NULL,
                  feed_url TEXT NOT NULL,
                  guid TEXT NOT NULL,
                  title TEXT NOT NULL,
                  url TEXT NOT NULL,
                  published_at TEXT,
                  author TEXT,
                  summary_src TEXT,
                  summary TEXT,
                  UNIQUE(project, guid)
                );
                CREATE INDEX IF NOT EXISTS idx_blog_posts_project_pub
                  ON blog_posts(project, published_at);
                """
            )
            self._conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
            self.commit()

    def close(self) -> None:
        self._conn.close()

    @contextmanager
    def transaction(self) -> Iterator[sqlite3.Connection]:
        try:
            yield self._conn
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise

    def execute(self, sql: str, params: tuple | dict = ()) -> sqlite3.Cursor:
        return self._conn.execute(sql, params)

    def executemany(self, sql: str, seq: list) -> sqlite3.Cursor:
        return self._conn.executemany(sql, seq)

    def commit(self) -> None:
        self._conn.commit()

    # --- runs ---

    def start_run(
        self, command: str, project: str, since: str | None = None
    ) -> int:
        cur = self.execute(
            "INSERT INTO runs (command, project, started_at, since, status) "
            "VALUES (?, ?, ?, ?, ?)",
            (command, project, utcnow(), since, "running"),
        )
        self.commit()
        return int(cur.lastrowid)

    def finish_run(
        self,
        run_id: int,
        status: str = "ok",
        stats: dict[str, Any] | None = None,
    ) -> None:
        self.execute(
            "UPDATE runs SET finished_at = ?, status = ?, stats_json = ? WHERE id = ?",
            (utcnow(), status, json.dumps(stats or {}), run_id),
        )
        self.commit()

    # --- cache ---

    def get_cache(self, key: str) -> tuple[str | None, bytes] | None:
        row = self.execute(
            "SELECT etag, body FROM cache_entries WHERE key = ?", (key,)
        ).fetchone()
        if not row:
            return None
        return row["etag"], row["body"]

    def set_cache(self, key: str, body: bytes, etag: str | None = None) -> None:
        self.execute(
            "INSERT INTO cache_entries (key, etag, fetched_at, body) VALUES (?, ?, ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET etag=excluded.etag, fetched_at=excluded.fetched_at, body=excluded.body",
            (key, etag, utcnow(), body),
        )
        self.commit()

    # --- sync state ---

    def get_sync(self, key: str) -> str | None:
        row = self.execute(
            "SELECT cursor FROM sync_state WHERE key = ?", (key,)
        ).fetchone()
        return row["cursor"] if row else None

    def set_sync(self, key: str, cursor: str) -> None:
        self.execute(
            "INSERT INTO sync_state (key, cursor, updated_at) VALUES (?, ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET cursor=excluded.cursor, updated_at=excluded.updated_at",
            (key, cursor, utcnow()),
        )
        self.commit()

    # --- repos ---

    def upsert_repo(
        self,
        project: str,
        full_name: str,
        tier: str,
        *,
        description: str | None = None,
        default_branch: str | None = None,
        is_archived: bool = False,
        stars: int = 0,
        pushed_at: str | None = None,
        latest_release_tag: str | None = None,
        latest_release_at: str | None = None,
        activity_90d: int = 0,
    ) -> int:
        self.execute(
            """
            INSERT INTO repos (
              project, full_name, tier, description, default_branch,
              is_archived, stars, pushed_at, latest_release_tag,
              latest_release_at, activity_90d
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(project, full_name) DO UPDATE SET
              tier=excluded.tier,
              description=excluded.description,
              default_branch=excluded.default_branch,
              is_archived=excluded.is_archived,
              stars=excluded.stars,
              pushed_at=excluded.pushed_at,
              latest_release_tag=COALESCE(excluded.latest_release_tag, repos.latest_release_tag),
              latest_release_at=COALESCE(excluded.latest_release_at, repos.latest_release_at),
              activity_90d=excluded.activity_90d
            """,
            (
                project,
                full_name,
                tier,
                description,
                default_branch,
                int(is_archived),
                stars,
                pushed_at,
                latest_release_tag,
                latest_release_at,
                activity_90d,
            ),
        )
        self.commit()
        row = self.execute(
            "SELECT id FROM repos WHERE project = ? AND full_name = ?",
            (project, full_name),
        ).fetchone()
        return int(row["id"])

    def get_repo_id(self, project: str, full_name: str) -> int | None:
        row = self.execute(
            "SELECT id FROM repos WHERE project = ? AND full_name = ?",
            (project, full_name),
        ).fetchone()
        return int(row["id"]) if row else None

    def list_repos(self, project: str) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM repos WHERE project = ? ORDER BY "
                "CASE tier WHEN 'core' THEN 0 WHEN 'watch' THEN 1 ELSE 2 END, "
                "activity_90d DESC",
                (project,),
            ).fetchall()
        )

    def replace_modules(
        self, repo_id: int, modules: list[dict[str, Any]]
    ) -> None:
        self.execute("DELETE FROM modules WHERE repo_id = ?", (repo_id,))
        for m in modules:
            self.execute(
                "INSERT INTO modules (repo_id, name, paths_json, source) VALUES (?, ?, ?, ?)",
                (
                    repo_id,
                    m["name"],
                    json.dumps(m["paths"]),
                    m.get("source", "config"),
                ),
            )
        self.commit()

    def list_modules(self, repo_id: int) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM modules WHERE repo_id = ? ORDER BY name",
                (repo_id,),
            ).fetchall()
        )

    # --- releases / PRs / issues ---

    def upsert_release(
        self,
        repo_id: int,
        tag: str,
        *,
        name: str | None = None,
        body: str | None = None,
        published_at: str | None = None,
        url: str | None = None,
    ) -> None:
        self.execute(
            """
            INSERT INTO releases (repo_id, tag, name, body, published_at, url)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(repo_id, tag) DO UPDATE SET
              name=excluded.name, body=excluded.body,
              published_at=excluded.published_at, url=excluded.url
            """,
            (repo_id, tag, name, body, published_at, url),
        )

    def upsert_pr(self, repo_id: int, pr: dict[str, Any]) -> None:
        reviewers = pr.get("reviewers") or []
        self.execute(
            """
            INSERT INTO pull_requests (
              id, repo_id, number, title, body, state, author, labels_json,
              merged_at, closed_at, updated_at, created_at,
              additions, deletions, changed_files, files_json, reviewers_json, url
            ) VALUES (
              ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            ON CONFLICT(repo_id, number) DO UPDATE SET
              title=excluded.title, body=excluded.body, state=excluded.state,
              author=excluded.author, labels_json=excluded.labels_json,
              merged_at=excluded.merged_at, closed_at=excluded.closed_at,
              updated_at=excluded.updated_at, created_at=excluded.created_at,
              additions=excluded.additions, deletions=excluded.deletions,
              changed_files=excluded.changed_files, files_json=excluded.files_json,
              reviewers_json=excluded.reviewers_json,
              url=excluded.url
            """,
            (
                pr.get("id"),
                repo_id,
                pr["number"],
                pr["title"],
                pr.get("body"),
                pr["state"],
                pr.get("author"),
                json.dumps(pr.get("labels") or []),
                pr.get("merged_at"),
                pr.get("closed_at"),
                pr.get("updated_at"),
                pr.get("created_at"),
                pr.get("additions"),
                pr.get("deletions"),
                pr.get("changed_files"),
                json.dumps(pr.get("files") or []),
                json.dumps(reviewers),
                pr.get("url"),
            ),
        )

    def upsert_issue(self, repo_id: int, issue: dict[str, Any]) -> None:
        self.execute(
            """
            INSERT INTO issues (
              id, repo_id, number, title, body, state, author, labels_json,
              created_at, updated_at, closed_at, comments_count,
              reactions_count, url, signal
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(repo_id, number) DO UPDATE SET
              title=excluded.title, body=excluded.body, state=excluded.state,
              author=excluded.author, labels_json=excluded.labels_json,
              created_at=excluded.created_at, updated_at=excluded.updated_at,
              closed_at=excluded.closed_at, comments_count=excluded.comments_count,
              reactions_count=excluded.reactions_count, url=excluded.url,
              signal=excluded.signal
            """,
            (
                issue.get("id"),
                repo_id,
                issue["number"],
                issue["title"],
                issue.get("body"),
                issue["state"],
                issue.get("author"),
                json.dumps(issue.get("labels") or []),
                issue.get("created_at"),
                issue.get("updated_at"),
                issue.get("closed_at"),
                issue.get("comments_count", 0),
                issue.get("reactions_count", 0),
                issue.get("url"),
                issue.get("signal"),
            ),
        )

    def upsert_proposal_file(
        self,
        repo_id: int,
        path: str,
        *,
        sha: str | None = None,
        last_modified_at: str | None = None,
        url: str | None = None,
    ) -> None:
        self.execute(
            """
            INSERT INTO proposal_files (repo_id, path, sha, last_modified_at, url)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(repo_id, path) DO UPDATE SET
              sha=excluded.sha, last_modified_at=excluded.last_modified_at, url=excluded.url
            """,
            (repo_id, path, sha, last_modified_at, url),
        )

    def replace_ownership(
        self, repo_id: int, entries: list[dict[str, Any]]
    ) -> None:
        self.execute("DELETE FROM ownership WHERE repo_id = ?", (repo_id,))
        for e in entries:
            self.execute(
                "INSERT INTO ownership (repo_id, module_id, path_pattern, owners_json, source) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    repo_id,
                    e.get("module_id"),
                    e["path_pattern"],
                    json.dumps(e["owners"]),
                    e["source"],
                ),
            )
        self.commit()

    def get_summary(
        self, kind: str, subject_key: str, source_hash: str
    ) -> str | None:
        row = self.execute(
            "SELECT content FROM summaries WHERE kind=? AND subject_key=? AND source_hash=?",
            (kind, subject_key, source_hash),
        ).fetchone()
        return row["content"] if row else None

    def save_summary(
        self,
        kind: str,
        subject_key: str,
        source_hash: str,
        content: str,
        *,
        model: str | None = None,
        tokens_in: int | None = None,
        tokens_out: int | None = None,
    ) -> None:
        self.execute(
            """
            INSERT INTO summaries (
              kind, subject_key, source_hash, model, content, created_at, tokens_in, tokens_out
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(kind, subject_key, source_hash) DO UPDATE SET
              content=excluded.content, model=excluded.model,
              tokens_in=excluded.tokens_in, tokens_out=excluded.tokens_out,
              created_at=excluded.created_at
            """,
            (
                kind,
                subject_key,
                source_hash,
                model,
                content,
                utcnow(),
                tokens_in,
                tokens_out,
            ),
        )
        self.commit()

    def list_merged_prs_since(
        self, repo_id: int, since_iso: str
    ) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM pull_requests WHERE repo_id = ? AND state = 'MERGED' "
                "AND merged_at IS NOT NULL AND merged_at >= ? ORDER BY merged_at DESC",
                (repo_id, since_iso),
            ).fetchall()
        )

    def list_releases_since(
        self, repo_id: int, since_iso: str
    ) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM releases WHERE repo_id = ? AND published_at IS NOT NULL "
                "AND published_at >= ? ORDER BY published_at DESC",
                (repo_id, since_iso),
            ).fetchall()
        )

    def list_releases(
        self, repo_id: int, *, limit: int = 12
    ) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM releases WHERE repo_id = ? "
                "ORDER BY published_at DESC NULLS LAST, tag DESC LIMIT ?",
                (repo_id, limit),
            ).fetchall()
        )

    def list_issues_by_signal(
        self, repo_id: int, signal: str | None = None, state: str | None = None
    ) -> list[sqlite3.Row]:
        clauses = ["repo_id = ?"]
        params: list[Any] = [repo_id]
        if signal:
            clauses.append("signal = ?")
            params.append(signal)
        if state:
            clauses.append("state = ?")
            params.append(state)
        sql = f"SELECT * FROM issues WHERE {' AND '.join(clauses)} ORDER BY updated_at DESC"
        return list(self.execute(sql, tuple(params)).fetchall())

    def list_open_prs(self, repo_id: int) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM pull_requests WHERE repo_id = ? AND state = 'OPEN' "
                "ORDER BY updated_at DESC",
                (repo_id,),
            ).fetchall()
        )

    def list_ownership(self, repo_id: int) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM ownership WHERE repo_id = ?", (repo_id,)
            ).fetchall()
        )

    def list_proposal_files(self, repo_id: int) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM proposal_files WHERE repo_id = ? ORDER BY path",
                (repo_id,),
            ).fetchall()
        )

    def upsert_blog_post(self, project: str, post: dict[str, Any]) -> None:
        self.execute(
            """
            INSERT INTO blog_posts (
              project, feed_url, guid, title, url, published_at,
              author, summary_src, summary
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(project, guid) DO UPDATE SET
              feed_url=excluded.feed_url,
              title=excluded.title,
              url=excluded.url,
              published_at=excluded.published_at,
              author=excluded.author,
              summary_src=excluded.summary_src,
              summary=COALESCE(excluded.summary, blog_posts.summary)
            """,
            (
                project,
                post["feed_url"],
                post["guid"],
                post["title"],
                post["url"],
                post.get("published_at"),
                post.get("author"),
                post.get("summary_src"),
                post.get("summary"),
            ),
        )

    def update_blog_summary(
        self, project: str, guid: str, summary: str
    ) -> None:
        self.execute(
            "UPDATE blog_posts SET summary = ? WHERE project = ? AND guid = ?",
            (summary, project, guid),
        )
        self.commit()

    def list_blog_posts_since(
        self, project: str, since_iso: str
    ) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM blog_posts WHERE project = ? "
                "AND published_at IS NOT NULL AND published_at >= ? "
                "ORDER BY published_at DESC, title",
                (project, since_iso),
            ).fetchall()
        )

    def list_blog_posts(self, project: str, limit: int = 50) -> list[sqlite3.Row]:
        return list(
            self.execute(
                "SELECT * FROM blog_posts WHERE project = ? "
                "ORDER BY published_at DESC, title LIMIT ?",
                (project, limit),
            ).fetchall()
        )

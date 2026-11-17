"""Database + init helpers."""

from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from tracker.cli import app
from tracker.db import SCHEMA_VERSION, Database


def test_schema_version(tmp_path: Path):
    db = Database(tmp_path / "t.db")
    ver = db.execute("PRAGMA user_version").fetchone()[0]
    assert ver == SCHEMA_VERSION
    db.close()


def test_init_cli(tmp_path: Path):
    runner = CliRunner()
    result = runner.invoke(app, ["--root", str(tmp_path), "init"])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "projects.yaml").exists()
    assert (tmp_path / ".tracker" / "tracker.db").exists()
    assert (tmp_path / "reports").is_dir()
    assert (tmp_path / "overrides").is_dir()

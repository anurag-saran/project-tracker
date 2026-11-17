"""Weekly rollup / latest-* helpers."""

from __future__ import annotations

from pathlib import Path

from tracker.config import load_config
from tracker.stages.rollup import build_weekly_rollup, publish_latest


def test_publish_latest(tmp_path: Path):
    pdir = tmp_path / "reports" / "vllm"
    pdir.mkdir(parents=True)
    dated = pdir / "2025-11-10-digest.md"
    dated.write_text("# digest\n\n## TL;DR for this week\n\n- hello\n")
    latest = publish_latest(dated, "digest")
    assert latest.name == "latest-digest.md"
    assert latest.read_text() == dated.read_text()


def test_build_weekly_rollup(tmp_workspace: Path):
    root = Path(__file__).resolve().parents[1]
    cfg = load_config(root / "projects.yaml")
    pdir = tmp_workspace / "reports" / "vllm"
    pdir.mkdir(parents=True)
    (pdir / "2025-11-10-digest.md").write_text(
        "# vllm digest\n\n## TL;DR for this week\n\n"
        "- Faster scheduler (#100)\n- New release v0.6.0\n\n"
        "## Details\n\nok\n"
    )
    (pdir / "2025-11-10-pipeline.md").write_text(
        "# pipeline\n\n## TL;DR for this week\n\n- 1 new RFC\n"
    )
    out = build_weekly_rollup(cfg, workspace=tmp_workspace, date="2025-11-10")
    assert out.name == "WEEKLY.md"
    text = out.read_text()
    assert "Weekly tracker — 2025-11-10" in text
    assert "### vllm" in text
    assert "Faster scheduler" in text
    assert "1 new RFC" in text
    assert (pdir / "latest-digest.md").exists()
    assert (tmp_workspace / "reports" / "2025-11-10-WEEKLY.md").exists()

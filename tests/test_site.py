"""Static site builder smoke test."""

from __future__ import annotations

from pathlib import Path

from tracker.config import load_config
from tracker.render.site import build_site


def test_build_site(tmp_workspace: Path):
    root = Path(__file__).resolve().parents[1]
    cfg = load_config(root / "projects.yaml")
    reports = tmp_workspace / "reports" / "vllm"
    reports.mkdir(parents=True)
    (reports / "module-map.md").write_text("# vllm module map\n\nHello.\n")
    (reports / "2025-11-01-digest.md").write_text(
        "# digest\n\n## TL;DR for this month\n\n- one\n"
    )
    (tmp_workspace / "LEARNING.md").write_text(
        "# Learning\n\n- [Quickstart](https://example.com)\n"
    )
    out = build_site(cfg, workspace=tmp_workspace)
    assert (out / "index.html").exists()
    assert (out / "vllm" / "index.html").exists()
    assert (out / "vllm" / "module-map.html").exists()
    assert (out / "vllm" / "2025-11-01-digest.html").exists()
    assert (out / "learning.html").exists()
    html = (out / "index.html").read_text()
    assert "vllm" in html
    assert "learning.html" in html

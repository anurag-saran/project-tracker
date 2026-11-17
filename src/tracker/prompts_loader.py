"""Load prompt markdown files."""

from __future__ import annotations

from pathlib import Path

from tracker.paths import prompts_dir


def load_prompt(name: str, root: Path | None = None) -> str:
    """Load prompts/<name>.md (name without extension ok)."""
    base = prompts_dir(root)
    path = base / name
    if not path.suffix:
        path = path.with_suffix(".md")
    if not path.exists():
        # fall back to package-relative default next to cwd prompts
        packaged = Path(__file__).resolve().parents[2] / "prompts" / path.name
        if packaged.exists():
            path = packaged
        else:
            raise FileNotFoundError(f"prompt not found: {path}")
    text = path.read_text()
    # Strip leading markdown title lines for system prompt use — keep body
    lines = text.splitlines()
    if lines and lines[0].startswith("#"):
        lines = lines[1:]
    return "\n".join(lines).strip()

"""LLM provider interface and implementations."""

from __future__ import annotations

import os
from typing import Literal

from tracker.llm.base import LLMProvider, LLMResult, NullProvider


def get_provider(
    name: Literal["anthropic", "openai", "null"] | None = None,
) -> LLMProvider:
    choice = (name or os.environ.get("TRACKER_LLM_PROVIDER") or "anthropic").lower()
    if choice in ("null", "none", "dry"):
        return NullProvider()
    if choice == "openai":
        from tracker.llm.openai_compat import OpenAICompatProvider

        return OpenAICompatProvider()
    from tracker.llm.anthropic import AnthropicProvider

    return AnthropicProvider()


__all__ = ["LLMProvider", "LLMResult", "NullProvider", "get_provider"]

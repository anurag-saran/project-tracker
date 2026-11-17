"""Anthropic Claude provider."""

from __future__ import annotations

import os

from tracker.llm.base import LLMProvider, LLMResult

# Approximate Claude Sonnet pricing per 1M tokens
_IN_COST = 3.0 / 1_000_000
_OUT_COST = 15.0 / 1_000_000


class AnthropicProvider(LLMProvider):
    name = "anthropic"

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
    ):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model or os.environ.get(
            "TRACKER_ANTHROPIC_MODEL", "claude-sonnet-4-20250514"
        )
        if not self.api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is required for the anthropic provider "
                "(or set TRACKER_LLM_PROVIDER=null / openai)."
            )

    def complete(self, system: str, user: str) -> LLMResult:
        import anthropic

        client = anthropic.Anthropic(api_key=self.api_key)
        msg = client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        text = "".join(
            block.text for block in msg.content if hasattr(block, "text")
        )
        tin = getattr(msg.usage, "input_tokens", 0) or 0
        tout = getattr(msg.usage, "output_tokens", 0) or 0
        cost = tin * _IN_COST + tout * _OUT_COST
        return LLMResult(
            text=text,
            model=self.model,
            tokens_in=tin,
            tokens_out=tout,
            cost_usd=cost,
        )

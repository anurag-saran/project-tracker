"""OpenAI / OpenAI-compatible (e.g. local vLLM) provider."""

from __future__ import annotations

import os

from tracker.llm.base import LLMProvider, LLMResult

_IN_COST = 2.5 / 1_000_000
_OUT_COST = 10.0 / 1_000_000


class OpenAICompatProvider(LLMProvider):
    name = "openai"

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
    ):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY") or "EMPTY"
        self.base_url = base_url or os.environ.get(
            "OPENAI_BASE_URL", "https://api.openai.com/v1"
        )
        self.model = model or os.environ.get(
            "TRACKER_OPENAI_MODEL", "gpt-4o-mini"
        )

    def complete(self, system: str, user: str) -> LLMResult:
        from openai import OpenAI

        client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        # Qwen3 thinking burns context; disable unless TRACKER_OPENAI_THINKING=1
        extra: dict = {}
        if os.environ.get("TRACKER_OPENAI_THINKING", "").lower() not in (
            "1",
            "true",
            "yes",
        ):
            extra["chat_template_kwargs"] = {"enable_thinking": False}
        resp = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            max_tokens=2048,
            extra_body=extra or None,
        )
        text = resp.choices[0].message.content or ""
        # Qwen3 / reasoning models often wrap scratchpad in <think>…</think>
        if "</think>" in text:
            text = text.split("</think>", 1)[-1].strip()
        elif text.lstrip().startswith("<think>"):
            text = ""
        usage = resp.usage
        tin = getattr(usage, "prompt_tokens", 0) or 0
        tout = getattr(usage, "completion_tokens", 0) or 0
        # Local endpoints: cost estimate only when hitting OpenAI
        cost = 0.0
        if "openai.com" in (self.base_url or ""):
            cost = tin * _IN_COST + tout * _OUT_COST
        return LLMResult(
            text=text,
            model=self.model,
            tokens_in=tin,
            tokens_out=tout,
            cost_usd=cost,
        )

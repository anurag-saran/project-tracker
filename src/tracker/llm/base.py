"""LLM provider base types."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class LLMResult:
    text: str
    model: str
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0


@dataclass
class UsageTracker:
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0
    calls: int = 0

    def add(self, result: LLMResult) -> None:
        self.tokens_in += result.tokens_in
        self.tokens_out += result.tokens_out
        self.cost_usd += result.cost_usd
        self.calls += 1

    def summary(self) -> dict:
        return {
            "calls": self.calls,
            "tokens_in": self.tokens_in,
            "tokens_out": self.tokens_out,
            "cost_usd": round(self.cost_usd, 4),
        }


class LLMProvider(ABC):
    name: str = "base"

    @abstractmethod
    def complete(self, system: str, user: str) -> LLMResult:
        ...


class NullProvider(LLMProvider):
    """Deterministic fallback when no API key / dry-run."""

    name = "null"

    def complete(self, system: str, user: str) -> LLMResult:
        # Extract PR lines if present for a grounded stub
        lines = [ln.strip() for ln in user.splitlines() if ln.strip()]
        bullets = [ln for ln in lines if ln.startswith("-") or ln.startswith("*")]
        if not bullets:
            bullets = lines[:5]
        text = "Summary unavailable (null LLM). Source items:\n" + "\n".join(
            bullets[:12]
        )
        return LLMResult(text=text, model="null", tokens_in=0, tokens_out=0)

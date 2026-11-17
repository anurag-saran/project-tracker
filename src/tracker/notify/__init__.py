"""Optional notifiers (Slack webhook, SMTP email). Off by default."""

from __future__ import annotations

import os
import smtplib
from abc import ABC, abstractmethod
from email.message import EmailMessage
from typing import Iterable

import httpx


class Notifier(ABC):
    name: str

    @abstractmethod
    def send(self, subject: str, body: str) -> None:
        ...


class NullNotifier(Notifier):
    name = "null"

    def send(self, subject: str, body: str) -> None:
        return


class SlackNotifier(Notifier):
    name = "slack"

    def __init__(self, webhook_url: str | None = None):
        self.webhook_url = webhook_url or os.environ.get("SLACK_WEBHOOK_URL")
        if not self.webhook_url:
            raise RuntimeError("SLACK_WEBHOOK_URL is required for slack notifier")

    def send(self, subject: str, body: str) -> None:
        text = f"*{subject}*\n{body}"
        # Slack hard limit ~40k; trim
        if len(text) > 35000:
            text = text[:35000] + "\n…(truncated)"
        resp = httpx.post(self.webhook_url, json={"text": text}, timeout=30)
        resp.raise_for_status()


class EmailNotifier(Notifier):
    name = "email"

    def __init__(
        self,
        *,
        host: str | None = None,
        port: int | None = None,
        user: str | None = None,
        password: str | None = None,
        mail_from: str | None = None,
        mail_to: str | None = None,
    ):
        self.host = host or os.environ.get("SMTP_HOST")
        self.port = port or int(os.environ.get("SMTP_PORT", "587"))
        self.user = user or os.environ.get("SMTP_USER")
        self.password = password or os.environ.get("SMTP_PASSWORD")
        self.mail_from = mail_from or os.environ.get("SMTP_FROM")
        self.mail_to = mail_to or os.environ.get("SMTP_TO")
        missing = [
            k
            for k, v in {
                "SMTP_HOST": self.host,
                "SMTP_FROM": self.mail_from,
                "SMTP_TO": self.mail_to,
            }.items()
            if not v
        ]
        if missing:
            raise RuntimeError(
                f"email notifier missing env: {', '.join(missing)}"
            )

    def send(self, subject: str, body: str) -> None:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.mail_from
        msg["To"] = self.mail_to
        msg.set_content(body)
        with smtplib.SMTP(self.host, self.port, timeout=30) as smtp:
            smtp.starttls()
            if self.user and self.password:
                smtp.login(self.user, self.password)
            smtp.send_message(msg)


def get_notifiers(enabled: Iterable[str] | None = None) -> list[Notifier]:
    """Return configured notifiers. Empty unless explicitly enabled."""
    names = list(enabled or [])
    env = os.environ.get("TRACKER_NOTIFIERS", "")
    if env and not names:
        names = [n.strip() for n in env.split(",") if n.strip()]
    out: list[Notifier] = []
    for n in names:
        if n == "slack":
            out.append(SlackNotifier())
        elif n == "email":
            out.append(EmailNotifier())
        elif n in ("null", "none"):
            out.append(NullNotifier())
    return out


def notify_all(
    notifiers: list[Notifier], subject: str, body: str
) -> None:
    for n in notifiers:
        n.send(subject, body)

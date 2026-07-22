import logging

import requests

from src.core.models.deal import Deal
from src.notifications.base.notifier import NotificationService

logger = logging.getLogger(__name__)


class DiscordNotifier(NotificationService):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send(self, deal: Deal) -> None:
        content = (
            f"🔥 **Nowy Deal!** 🔥\n"
            f"**{deal.title}**\n"
            f"Cena: {deal.price} zł\n"
            f"[Link do oferty]({deal.url})"
        )
        payload = {"content": content}
        response = requests.post(self.webhook_url, json=payload)

        if response.status_code == 204:
            logger.info(f"Powiadomienie wysłane na Discorda: {deal.title}")
        else:
            logger.error(
                f"Błąd wysyłania na Discorda: {response.status_code} - {response.text}"
            )

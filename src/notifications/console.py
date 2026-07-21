import logging

from src.core.models.deal import Deal
from src.notifications.base.notifier import NotificationService

logger = logging.getLogger(__name__)


class ConsoleNotifier(NotificationService):
    def send(self, deal: Deal) -> None:
        logger.info(f"Wysyłam powiadomienie o: {deal.title}")

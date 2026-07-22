import logging

from src.marketplaces.base.provider import MarketplaceProvider
from src.notifications.base.notifier import NotificationService

logger = logging.getLogger(__name__)


class DealHunterApp:
    def __init__(
        self, providers: list[MarketplaceProvider], notifier: NotificationService
    ):
        self.providers = providers
        self.notifier = notifier

    def hunt(self, query: str, max_price: float = None) -> None:
        logger.info(f"Rozpoczynam wyszukiwanie dla: {query} {max_price}zł")
        for provider in self.providers:
            deals = provider.search(query, max_price)
            for deal in deals:
                self.notifier.send(deal)

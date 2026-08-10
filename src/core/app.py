import logging

from src.core.models.search import SearchCriteria
from src.marketplaces.base.provider import MarketplaceProvider
from src.notifications.base.notifier import NotificationService

logger = logging.getLogger(__name__)


class DealHunterApp:
    def __init__(self, providers: list[MarketplaceProvider], notifier: NotificationService):
        self.providers = providers
        self.notifier = notifier

    def hunt(self, criteria: SearchCriteria) -> None:
        logger.info(f"Rozpoczynam wyszukiwanie dla: {criteria.query} {criteria.max_price}zł")
        for provider in self.providers:
            deals = provider.search(criteria)
            for deal in deals:
                self.notifier.send(deal)

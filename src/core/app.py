import logging

from sqlalchemy import select

from src.core.database import SessionLocal
from src.core.models.search import SearchCriteria
from src.core.models.sent_deal import SentDealModel
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
            with SessionLocal() as session:
                for deal in deals:
                    stmt = select(SentDealModel).where(SentDealModel.url == deal.url)
                    existing_deal = session.scalar(stmt)
                    if not existing_deal:
                        self.notifier.send(deal)
                        logger.info(f"Wysłałem powiadomienie o: {deal.title}")
                        new_sent = SentDealModel(url=deal.url)
                        session.add(new_sent)
                        session.commit()
                    else:
                        logger.info(f"Omijam ofertę (już wysłana): {deal.title}")

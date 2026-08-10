from abc import ABC, abstractmethod

from src.core.models.deal import Deal
from src.core.models.search import SearchCriteria


class MarketplaceProvider(ABC):
    @abstractmethod
    def search(self, criteria: SearchCriteria) -> list[Deal]:
        pass

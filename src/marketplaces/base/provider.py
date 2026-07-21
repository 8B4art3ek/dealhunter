from abc import ABC, abstractmethod

from src.core.models.deal import Deal


class MarketplaceProvider(ABC):
    @abstractmethod
    def search(self, query: str) -> list[Deal]:
        pass

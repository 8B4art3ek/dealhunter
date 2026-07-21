from src.core.models.deal import Deal
from src.marketplaces.base.provider import MarketplaceProvider


class DummyProvider(MarketplaceProvider):
    def search(self, query: str) -> list[Deal]:
        fejkowy_deal = Deal(
            title="Testowy But", price=100.0, url="https://fake-link.pl", source="dummy"
        )
        return [fejkowy_deal]

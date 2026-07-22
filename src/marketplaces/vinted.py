import logging

from curl_cffi import requests

from src.core.models.deal import Deal
from src.marketplaces.base.provider import MarketplaceProvider

logger = logging.getLogger(__name__)


class VintedProvider(MarketplaceProvider):
    def __init__(self):
        self.session = requests.Session(impersonate="chrome")

    def _get_session_cookie(self) -> None:
        url = "https://www.vinted.pl"
        logger.info("Pobieram token sesyjny Vinted...")

        response = self.session.get(url)

        if response.status_code == 200:
            logger.info("Ciastka pobrane pomyślnie!")
        else:
            logger.error(f"Błąd pobierania ciastek: {response.status_code}")

    def search(self, query: str, max_price: float = None) -> list[Deal]:
        self._get_session_cookie()

        api_url = "https://www.vinted.pl/api/v2/catalog/items"
        params = {"search_text": query, "order": "newest_first"}

        if max_price is not None:
            params["price_to"] = str(max_price)

        logger.info(f"Szukam ofert na Vinted dla: {query}")
        headers = {"Accept": "application/json, text/plain, */*"}
        response = self.session.get(api_url, params=params, headers=headers)

        if response.status_code != 200:
            logger.error(f"Błąd API Vinted: {response.status_code} - {response.text}")
            return []

        data = response.json()
        items = data.get("items", [])

        deals = []
        for item in items[:3]:  # ograniczenie do 3
            price_data = item.get("price", {})
            price_amount = price_data.get("amount", 0.0)
            deal = Deal(
                title=item.get("title", "Brak tytułu"),
                price=float(price_amount),
                url=item.get("url", ""),
                source="vinted",
            )
            deals.append(deal)
        return deals

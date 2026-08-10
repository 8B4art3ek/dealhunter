import logging

from curl_cffi import requests
from playwright.sync_api import sync_playwright

from src.core.models.deal import Deal
from src.core.models.search import SearchCriteria
from src.marketplaces.base.provider import MarketplaceProvider

logger = logging.getLogger(__name__)


class VintedProvider(MarketplaceProvider):
    def __init__(self):
        self.session = requests.Session(impersonate="chrome124")
        self.session.headers.update(
            {
                "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            }
        )
        self._get_session_cookie()

    def _get_session_cookie(self) -> None:
        logger.info("Odpalam przeglądarkę w tle po ciastka...")
        with sync_playwright() as p:
            chromium = p.chromium
            browser = chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
            page = browser.new_page()
            page.goto("https://www.vinted.pl")
            page.wait_for_timeout(5000)
            cookies = page.context.cookies()
            browser.close()
            for cookie in cookies:
                self.session.cookies.set(cookie["name"], cookie["value"], domain=cookie["domain"])
            logger.info("Ciastka wstrzyknięte do sesji!")

    def search(self, criteria: SearchCriteria) -> list[Deal]:
        api_url = "https://www.vinted.pl/api/v2/catalog/items"
        params = {"search_text": criteria.query, "order": "newest_first"}

        if criteria.max_price is not None:
            params["price_to"] = str(criteria.max_price)

        logger.info(f"Szukam ofert na Vinted dla: {criteria.query}")
        response = self.session.get(api_url, params=params)

        if response.status_code != 200:
            logger.error(f"Błąd API Vinted: {response.status_code} - {response.text}")
            return []

        data = response.json()
        items = data.get("items", [])

        deals = []
        for item in items[: criteria.limit]:  # ograniczenie do limitu z search.py
            price_data = item.get("price", {})
            price_amount = price_data.get("amount", 0.0)
            deal = Deal(
                title=item.get("title", "Brak tytułu"),
                price=float(price_amount),
                url=item.get("url", ""),
                source="vinted",
                condition=item.get("status", "Nieznany"),
            )
            deals.append(deal)
        return deals

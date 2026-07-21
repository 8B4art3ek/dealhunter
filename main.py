import logging

from src.core.app import DealHunterApp
from src.marketplaces.dummy import DummyProvider
from src.notifications.console import ConsoleNotifier

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    moj_provider = DummyProvider()
    moj_notifier = ConsoleNotifier()
    app = DealHunterApp(providers=[moj_provider], notifier=moj_notifier)
    app.hunt("Nike Tech Fleece do 80 zł")

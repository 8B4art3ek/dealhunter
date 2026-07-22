import logging
import os

from dotenv import load_dotenv

from src.core.app import DealHunterApp
from src.marketplaces.vinted import VintedProvider
from src.notifications.discord import DiscordNotifier

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    my_provider = VintedProvider()
    discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
    if not discord_webhook:
        logger.error("Brak linku do webhooka! Sprawdź plik .env")
        exit(1)
    my_notifier = DiscordNotifier(webhook_url=discord_webhook)

    app = DealHunterApp(providers=[my_provider], notifier=my_notifier)
    app.hunt("Nike Tech Fleece", max_price=80.0)

from abc import ABC, abstractmethod

from src.core.models.deal import Deal


class NotificationService(ABC):
    @abstractmethod
    def send(self, deal: Deal) -> None:
        pass

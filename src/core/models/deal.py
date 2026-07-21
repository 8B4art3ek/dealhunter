from dataclasses import dataclass
from datetime import datetime, field


@dataclass
class Deal:
    title: str
    price: float
    url: str
    source: str
    created_at: datetime = field(default_factory=datetime.now)

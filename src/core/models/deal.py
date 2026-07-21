from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Deal:
    title: str
    price: float
    url: str
    source: str
    created_at: datetime = field(default_factory=datetime.now)

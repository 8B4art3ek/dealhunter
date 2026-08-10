from dataclasses import dataclass


@dataclass
class SearchCriteria:
    query: str
    max_price: float | None = None
    limit: int = 10

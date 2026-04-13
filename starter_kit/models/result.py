from dataclasses import dataclass


@dataclass
class OrderResult:
    status: str
    exchange: str
    symbol: str
    side: str
    order_type: str
    qty: float
    price: float | None = None
    message: str = ""
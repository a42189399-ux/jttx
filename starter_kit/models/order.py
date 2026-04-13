from dataclasses import dataclass


@dataclass
class OrderRequest:
    symbol: str
    side: str
    order_type: str
    qty: float
    price: float | None = None
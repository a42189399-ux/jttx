from starter_kit.models.order import OrderRequest
from starter_kit.models.result import OrderResult


class FakeExchangeAdapter:
    def __init__(self, exchange_name: str = "fake_binance"):
        self.exchange_name = exchange_name

    def place_order(self, order: OrderRequest) -> OrderResult:
        print(f"[fake adapter] received order: {order}")

        return OrderResult(
            status="submitted",
            exchange=self.exchange_name,
            symbol=order.symbol,
            side=order.side,
            order_type=order.order_type,
            qty=order.qty,
            price=order.price,
            message="order was simulated successfully",
        )
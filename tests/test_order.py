import unittest
from starter_kit.models.order import OrderRequest


class TestOrderRequest(unittest.TestCase):
    def test_order_creation(self):
        order = OrderRequest(symbol="BTCUSDT", side="buy", order_type="limit", qty=50, price=60000)
        self.assertEqual(order.symbol, "BTCUSDT")
        self.assertEqual(order.side, "buy")
        self.assertEqual(order.order_type, "limit")
        self.assertEqual(order.qty, 50)
        self.assertEqual(order.price, 60000)


if __name__ == "__main__":
    unittest.main()
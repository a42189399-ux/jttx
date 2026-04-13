import unittest
from starter_kit.models.order import OrderRequest
from starter_kit.exchanges.fake_adapter import FakeExchangeAdapter


class TestFakeExchangeAdapter(unittest.TestCase):
    def test_place_order(self):
        adapter = FakeExchangeAdapter()
        order = OrderRequest(symbol="BTCUSDT", side="buy", order_type="limit", qty=50, price=60000)
        result = adapter.place_order(order)
        self.assertEqual(result.status, "submitted")
        self.assertEqual(result.symbol, "BTCUSDT")
        self.assertEqual(result.message, "order was simulated successfully")


if __name__ == "__main__":
    unittest.main()
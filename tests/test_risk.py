import unittest
from starter_kit.risk.checks import check_risk


class TestRiskChecks(unittest.TestCase):
    def test_check_risk_pass(self):
        config = {
            "allowed_symbols": ["BTCUSDT", "ETHUSDT"],
            "max_order_qty": 100,
            "dry_run": True,
        }
        try:
            check_risk("BTCUSDT", 50, config)
        except ValueError:
            self.fail("check_risk raised ValueError unexpectedly!")

    def test_check_risk_fail(self):
        config = {
            "allowed_symbols": ["BTCUSDT", "ETHUSDT"],
            "max_order_qty": 100,
            "dry_run": True,
        }
        with self.assertRaises(ValueError):
            check_risk("DOGEUSDT", 50, config)


if __name__ == "__main__":
    unittest.main()
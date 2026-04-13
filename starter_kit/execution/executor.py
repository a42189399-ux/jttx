from starter_kit.risk.checks import check_risk


class OrderExecutor:
    def __init__(self, adapter, config: dict):
        self.adapter = adapter
        self.config = config

    def execute(self, order):
        check_risk(order.symbol, order.qty, self.config)
        return self.adapter.place_order(order)
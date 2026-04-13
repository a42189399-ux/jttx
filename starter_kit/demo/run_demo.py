from starter_kit import __version__
from starter_kit.config.loader import load_config
from starter_kit.models.order import OrderRequest
from starter_kit.exchanges.fake_adapter import FakeExchangeAdapter
from starter_kit.execution.executor import OrderExecutor


def main():
    print("starter-kit demo is running")
    print(f"version: {__version__}")

    config = load_config()
    print(f"Loaded config: {config}")

    order = OrderRequest(
        symbol="BTCUSDT",
        side="buy",
        order_type="limit",
        qty=50,
        price=60000,
    )

    print(f"Created order: {order}")

    adapter = FakeExchangeAdapter()
    executor = OrderExecutor(adapter=adapter, config=config)

    try:
        result = executor.execute(order)
        print(f"Order result: {result}")
    except ValueError as e:
        print(f"Execution failed: {e}")


if __name__ == "__main__":
    main()
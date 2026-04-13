def check_risk(order_symbol, order_qty, config):
    # 检查交易对是否在白名单
    if order_symbol not in config.get("allowed_symbols", []):
        raise ValueError(f"Symbol {order_symbol} is not allowed.")
    
    # 检查数量是否超限
    if order_qty > config.get("max_order_qty", 0):
        raise ValueError(f"Order quantity {order_qty} exceeds the maximum limit.")
    
    # 模拟模式提示
    if config.get("dry_run"):
        print("Dry-run mode is enabled. No real orders will be placed.")
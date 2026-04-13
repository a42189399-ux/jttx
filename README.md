# Multi-Exchange Order Execution Starter Kit

一个面向工程型用户的最小下单执行 Starter Kit，包含统一订单结构、最小风控检查、fake adapter 和可运行 demo。

## 当前支持范围

- 统一订单对象 OrderRequest
- 最小风控检查：symbol 白名单、最大下单数量、dry-run
- fake adapter 模拟下单
- 统一执行器 OrderExecutor
- 本地可运行 demo

## 当前明确不包含

- 真实交易所 API 接入
- 策略逻辑
- 回测系统
- 可视化 UI
- 高级风控引擎
- 多账户管理
- 监控告警平台

## 如何贡献

欢迎提交 issues 和 pull requests。

1. Fork 本仓库。
2. 创建你的功能分支 (git checkout -b feature/your-feature).
3. 提交你的更改 (git commit -am 'Add new feature').
4. 推送到分支 (git push origin feature/your-feature).
5. 提交 pull request。

所有贡献将根据 MIT 许可证许可。

## 安装步骤

1. 创建虚拟环境
   `python -m venv .venv`

2. 激活虚拟环境（Windows PowerShell）
   `.venv\Scripts\Activate`

3. 安装依赖
   `pip install -r requirements.txt`


## 付费交付版额外包含
- INSTALL.md：更完整的安装与配置手册。
- config/settings.paid.example.yaml：更完整的示例配置文件。
- TROUBLESHOOTING.md：常见报错排查与解决方案。

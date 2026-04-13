# 安装与配置手册

## 1. 环境要求

- 操作系统：Windows 10 / Windows 11
- Python 版本：3.11 及以上
- 依赖安装方式：pip install -r requirements.txt
- 当前默认运行模式：dry-run（模拟执行，不会真实下单）

## 2. 安装步骤

### 2.1 创建虚拟环境
在项目根目录执行：

python -m venv .venv
### 2.2 激活虚拟环境（Windows PowerShell）

.venv\Scripts\Activate
### 2.3 安装依赖

pip install -r requirements.txt

## 3. 常见问题
- 问题1：如何修改交易所适配器？
  解答：可以在 starter_kit\exchanges 目录下修改或新增适配器文件。

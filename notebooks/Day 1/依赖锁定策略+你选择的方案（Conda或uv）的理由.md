# 依赖锁定策略+你选择的方案（Conda或uv）的理由

## **工程模板**

project\_root/
├─ README.md
├─ pyproject.toml / setup.py
├─ requirements.txt / environment.yml
├─ src/
│  └─ package\_name/
│     ├─ \_\_init\_\_.py
│     ├─ core/
│     ├─ utils/
│     └─ cli.py
├─ tests/
├─ data/        (可选，通常不进 git)
├─ scripts/
└─ .gitignore

## requirements.txt vs environment.yml

|维度|requirements.txt|environment.yml|
| ----------| -------------------| ---------------------------------|
|依赖范围|仅 Python 包|Python + 非 Python（如 CUDA、MKL）|
|解析工具|pip|conda|
|可移植性|高（但脆弱）|强（但平台相关）|
|锁定能力|弱（除非 freeze）|强（环境级）|
|工程定位|轻量工程 / 库|科学计算 / 研究型项目|

## 可复现通常包含三层：

1. ​**代码可复现**（git 版本）
2. ​**依赖可复现**（版本、二进制、底层库）
3. ​**运行环境可复现**（Python 版本、系统差异）

- requirements.txt **只能覆盖第 2 层的一部分**
- environment.yml 可以覆盖 **第 2 + 第 3 层**

## Conda or uv(i choose Conda,but it false in pycharm,sad)

####  **Conda**

- 项目目标是**可复现而不是极致轻量**
- 依赖可能涉及 **NumPy / SciPy / CUDA / BLAS**
- Conda 能管理 **非 Python 依赖**
- environment.yml 明确记录 Python 版本与通道来源

👉 适合：科研 / 工程原型 / 数据分析

####  **uv**

你可以这样立论：

- uv 提供 **更快的解析速度**
- 支持 **lock file（类似 poetry）**
- 更接近现代 Python 工程（pyproject.toml）

👉 说明：

> uv 对非 Python 依赖支持有限，可复现依赖于系统一致性

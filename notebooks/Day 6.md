# Day 6

### Day 6: 工程卫生：格式化/静态检查/预提交钩子（为后续目标铺路）

#### 今日任务

1. **学习：Python工程常用工具链（ruff/black/pre-commit）各自解决什么问题**

   为什么学习这个，因为团队协作需要风格统一。

   - 类型：`学习` | 时长：1.0小时 | 优先级：中
   - 交付成果：docs/[tooling_overview](Day%206/tooling_overview.md).md（ruff/black/isort/pre-commit对照表）
2. **实践：在仓库配置ruff与black（pyproject.toml）；本地运行并修复现有代码风格问题**

   - 类型：`实践` | 时长：2.0小时 | 优先级：高
   - 交付成果：[pyproject.toml](assets/pyproject-20260107161100-ib5y2vz.toml) + 通过ruff/black的终端输出
3. **实践：配置**​[pre-commit](Day%206/pre-commit.md)​ **（至少包含ruff与black钩子），安装并在一次提交中触发检查**

   - 类型：`实践` | 时长：2.0小时 | 优先级：高
   - 交付成果：[.pre-commit-config.yaml](assets/.pre-commit-config-20260107170854-okzt1za.yaml) + 1次“pre-commit通过”的提交记录
4. **复盘：把“新电脑/新服务器上如何一键开始开发”的步骤更新到reproduce.md（含pre-commit安装）**

   - 类型：`复盘` | 时长：0.5小时 | 优先级：高
   - 交付成果：更新后的docs/[reproduce](Day%206/reproduce.md).md（步骤可按序执行）

#### ✅ 成功标准

> 仓库具备ruff/black/pre-commit；可在本地成功运行并通过；commit次数累计≥8

---

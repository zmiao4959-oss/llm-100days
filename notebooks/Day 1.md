# Day 1

1. **确定主工作环境（优先WSL2 Ubuntu 22.04或原生Linux）；完成系统更新、基础工具安装（build-essential, curl, wget, unzip, htop, tree, jq）并记录版本信息**

    - 类型：`实践` | 时长：2.0小时 | 优先级：高
    - 交付成果：一份[环境基线报告](Day%201/环境基线报告.md)：OS版本、内核、关键工具版本清单（含命令输出）
2. **安装并配置Python环境管理（Conda或uv二选一；推荐：Miniconda+conda-forge 或 uv+python）；创建项目专用虚拟环境（命名如 llm-100d）**

    - 类型：`实践` | 时长：2.0小时 | 优先级：高
    - 交付成果：可激活的虚拟环境（conda env list/uv venv可证明）
3. **学习：Python工程常用目录结构与依赖管理基础（requirements.txt vs environment.yml；可复现原则）**

    - 类型：`学习` | 时长：1.5小时 | 优先级：中
    - 交付成果：[依赖锁定策略+你选择的方案（Conda或uv）的理由](Day%201/依赖锁定策略+你选择的方案（Conda或uv）的理由.md)
4. **复盘：建立每日记录模板（今日目标/完成情况/卡点/明日计划/耗时统计）并写Day1记录**

    - 类型：`复盘` | 时长：0.5小时 | 优先级：高
    - 交付成果：Day1复盘条目（Notion/Obsidian/Trello任一，我选用思源笔记）

#### ✅ 成功标准

> 能在终端中新建并激活虚拟环境；输出环境基线.md；完成Day1复盘

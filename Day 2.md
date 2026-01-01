# Day 2

### Day 2: GPU/CUDA（如需）与Python依赖落地；导出可复现文件初版

#### 今日任务

1. **（如有NVIDIA GPU且计划后续训练）安装/验证CUDA链路：nvidia-smi可用；在WSL下验证**​**GPU透传**​ **；记录驱动/CUDA版本**

    - 类型：`实践` | 时长：1.5小时 | 优先级：中
    - 交付成果：一份[gpu_check.md](Day%202/gpu_check.md.md)：nvidia-smi输出截图/文本 + 版本号
2. **安装项目基础依赖（建议：python-dotenv, requests, numpy, pandas, matplotlib, ipykernel, jupyter, rich）；运行一个最小脚本验证import与版本**

    - 类型：`实践` | 时长：2.0小时 | 优先级：高
    - 交付成果：scripts/[verify_env.py](assets/verify_env-20251218170139-f9zdaja.py)（打印Python与关键包版本；运行成功的终端输出）[输出](Day%202/输出.md)
3. **导出可复现依赖文件初版（Conda导出environment.yml；pip导出requirements.txt），并写清导出命令与恢复命令**

    - 类型：`实践` | 时长：1.5小时 | 优先级：高
    - [交付成果](Day%202/交付成果.md)：environment.yml + requirements.txt + docs/reproduce.md（含创建/安装/运行步骤）
4. **学习：阅读1篇“可复现实验/工程环境”最佳实践材料（随机种子、依赖锁定、配置文件）并提炼要点**

    - 类型：`学习` | 时长：1.5小时 | 优先级：中
    - 交付成果：[笔记](Day%202/笔记.md)：可复现清单（≥8条）
5. **复盘：更新卡点与解决方案；列出仍不确定项（如CUDA是否必须、选Conda还是uv）并做决定**

    - 类型：`复盘` | 时长：0.5小时 | 优先级：高
    - 交付成果：Day2复盘条目（含“已决策事项/待决策事项”）

#### ✅ 成功标准

> 能用verify_env.py验证环境；生成environment.yml与requirements.txt初版；有可复现步骤文档

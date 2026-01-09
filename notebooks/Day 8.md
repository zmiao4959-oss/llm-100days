# Day 8

# 有点抽象了这一天的任务，放到下一天结合案例一起做

### Day 8: 从“环境”走向“工程”：加入最小Python包结构与CLI脚本

#### 今日任务

1. **学习：src布局、可导入模块、入口脚本（python -m）、配置与日志的最小实践**

   - 类型：`学习` | 时长：1.5小时 | 优先级：中
   - 交付成果：[笔记](Day%208/笔记.md)：你项目采用的结构与原因（≥200字）
2. **实践：建立src/llm_bootstrap/包；新增一个CLI(Command-line interface)脚本（如scripts/hello_cli.py）支持参数（--name/--times）并用argparse实现**​[argparse.html](assets/argparse-20260109123235-wu8c5s2.html)

   - 类型：`实践` | 时长：2.5小时 | 优先级：高
   - 交付成果：可运行命令示例写入README（含输出示例）
3. **实践：加入基础日志（logging）与配置文件样例（config.yaml或.env示例），并在脚本中读取**

   <div>
   【Python基础之标准库logging 你还在用print来调试程序吗，OUT啦】 https://www.bilibili.com/video/BV1sK4y1x7e1/?share_source=copy_web&vd_source=acbae6759800f394aa40173bf2bc43f9
   </div>

   - 类型：`实践` | 时长：2.0小时 | 优先级：中
   - 交付成果：config示例文件 + 脚本支持读取配置的实现
4. **复盘：记录“今天新增的工程要素（包/CLI/日志/配置）在LLM项目中的对应位置”**

   - 类型：`复盘` | 时长：0.5小时 | 优先级：中
   - 交付成果：docs/engineering_mapping.md（≥6条对应关系）

#### ✅ 成功标准

> 仓库具备可导入包与可运行CLI；README包含运行命令；提交次数继续增加（≥12更佳）

---

# Day 9

### Day 9: 小型可验证Demo：HTTP调用 + 结构化输出 + 文档化

#### 今日任务

1. **学习：HTTP请求基础（GET/POST、headers、超时、重试），以及把请求结果保存成JSON/CSV的常见模式**

   - 类型：`学习` | 时长：1.5小时 | 优先级：中
   - 交付成果：docs/http_notes.md [test.ipynb](assets/test-20260109213904-t4a6rk5.ipynb)（含timeout/retry最佳实践）
2. **实践：写一个可复现的小Demo（不依赖LLM也可）：调用公开API（如GitHub API或天气API），保存响应到data/并做简单统计（如字段计数）**

   - 类型：`实践` | 时长：3.0小时 | 优先级：高
   - 交付成果：scripts/[translate_cli.py](assets/translate_cli-20260109214013-rdzhf18.py) + 输出文件（data/sample.json）+ 统计输出示例
3. **实践：为Demo补齐文档与“从0到运行”步骤（依赖、命令、预期输出、常见报错）**

   - 类型：`实践` | 时长：1.5小时 | 优先级：高
   - 交付成果：README新增“Demo：translate_cli”章节
4. **复盘：把Demo拆成“输入-处理-输出-失败情形”四段，列出至少5条失败情形与处理方式**

   - 类型：`复盘` | 时长：0.5小时 | 优先级：中
   - 交付成果：docs/[failure_modes](Day%209/failure_modes.md).md（≥5条）

#### ✅ 成功标准

> 任何人按README可运行Demo并产出文件；你能解释超时/重试/异常处理策略

---

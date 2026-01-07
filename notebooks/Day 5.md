# Day 5

### Day 5: rebase/冲突处理/回滚：让版本历史可控

#### 今日任务

推荐优先学习Git基础，看完git讲义再进行以下任务完成。

[Git讲义.pdf](assets/Git讲义-20260106094921-vhh7j39.pdf)

1. **学习：rebase交互式用法（reword/squash/fixup）、冲突解决、reset与revert区别**

   - 类型：`学习` | 时长：1.5小时 | 优先级：中
   - 交付成果：docs/[git_rewrite_and_recover](Day%205/git_rewrite_and_recover.md)（含3种场景：改提交信息/合并提交/误提交回滚）
2. **实践：刻意制造一次冲突（同一文件不同分支修改），用rebase解决并保留清晰历史；随后用revert演练回滚一次提交**

   - 类型：`实践` | 时长：2.5小时 | 优先级：高
   - 交付成果：仓库中可追溯的冲突解决记录（commit/PR）；revert后的状态正确
3. **实践：加入**​[CHANGELOG](Day%205/CHANGELOG.md)​ **.md（简版）与版本标记策略（tag v0.1.0）**

   - 类型：`实践` | 时长：1.0小时 | 优先级：低
   - 交付成果：CHANGELOG.md + 一个git tag
4. **复盘：总结“什么时候用merge，什么时候用rebase”，写进git_cheatsheet**

   - 类型：`复盘` | 时长：0.5小时 | 优先级：中
   - 交付成果：更新后的docs/git_cheatsheet.md

#### ✅ 成功标准

> 能独立完成一次rebase冲突解决与一次revert回滚；commit次数累计≥6

---

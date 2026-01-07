# commit_convention

# Git 提交与分支规范

本规范基于“约定式提交”和通用分支管理实践制定，旨在保持项目历史清晰、可读。

## 提交信息规范

### 格式

### 常用提交类型

|类型|说明|示例|
| :-----| :-----------------| :-----|
|​`feat`|新增功能|​`feat: 新增思源笔记看板集成功能`|
|​`fix`|修复错误|​`fix(sync): 修复数据同步冲突问题`|
|​`docs`|文档更新|​`docs(commit_convention): 添加分支命名示例`|
|​`style`|代码格式调整|​`style: 按照 ESLint 规则格式化代码`|
|​`refactor`|代码重构|​`refactor(task): 优化看板任务状态计算逻辑`|
|​`test`|测试相关|​`test: 为 Git 工具函数添加测试用例`|
|​`chore`|构建或工具链变动|​`chore: 更新项目依赖包版本`|

### 提交示例

1. **feat**: `feat(board): 在看板视图中支持拖拽排序任务`
2. **fix (带范围)** : `fix(auth): 修复登录令牌过期时间计算错误`
3. **docs**: `docs: 更新项目 quick start 指南`
4. **style**: `style: 调整所有 .md 文件的换行符一致性`
5. **chore (关联issue)** : `chore: 升级 TypeScript 到 5.0\n\nCloses #45`
6. **带破坏性变更**: `feat(api)!: 重构用户列表接口，返回字段变更\n\nBREAKING CHANGE: /users 接口不再返回 'phone' 字段`

## 分支命名规范

### 格式

### 常用分支类别

|类别|用途|示例|
| :-----| :-------------| :-----|
|​`feature/*`|新功能开发|​`feature/add-llm-chat-module`|
|​`fix/*`|Bug修复|​`fix/readme-typo`|
|​`docs/*`|文档工作|​`docs/add-commit-spec`|
|​`chore/*`|维护任务|​`chore/setup-ci-pipeline`|
|​`hotfix/*`|紧急线上修复|​`hotfix/critical-data-loss`|
|​`release/*`|版本发布|​`release/v1.0.0`|

### 分支命名示例

1. ​`feature/user-dashboard`
2. ​`fix/export-csv-encoding`
3. ​`docs/update-api-documentation`
4. ​`chore/upgrade-dependencies`
5. ​`hotfix/payment-amount-display`
6. ​`release/v2.1.0-rc`

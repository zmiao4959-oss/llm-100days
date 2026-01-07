# dev_workflow

# 第一步：克隆

```
# 新建一个文件夹用来测试
# 假设要克隆的项目地址(最好是自己的，便于操作)
git clone https://github.com/YourGithubName/YourRepositoryName

# 进入项目目录
cd YourRepositoryName

# 查看当前分支（通常是main或master）
git branch -a
```

# 第二步：新建分支(分支是一个仓库的复印本，不影响主仓库)并在当前分支进行修改或功能开发，合并上传

```
# 创建并切换分支
git checkout -b feature/awesome-feature

# 切换回主分支
git checkout main

# 合并分支（将feature合并到main）
git checkout main
git merge feature/awesome-feature

# 删除本地分支
git branch -d feature/awesome-feature

# 删除远程分支
git push origin --delete feature/awesome-feature
```

分支命名规范

```
feature/    # 新功能
bugfix/     # bug修复  
hotfix/     # 紧急修复
docs/       # 文档更新
test/       # 测试相关
refactor/   # 代码重构
```

# 第三步：创建GitHub PR模板/Issue模板并使用（注意windows里touch命令不可用，使用ni也就是New-Item来创建文件）

## 📁 **第一步：创建模板文件结构**

### 1.1 在项目根目录创建`.github`文件夹

bash

```
# 进入你的项目
cd your-project

# 创建.github目录
mkdir -p .github/ISSUE_TEMPLATE

# 创建PULL_REQUEST_TEMPLATE.md（可选但推荐）
touch .github/PULL_REQUEST_TEMPLATE.md

# 查看结构
ls -la .github/
# 应该看到：
# ISSUE_TEMPLATE/
# PULL_REQUEST_TEMPLATE.md
```

### 1.2 创建配置文件（可选但有用）

bash

```
# 创建配置文件
touch .github/CONTRIBUTING.md    # 贡献指南
touch .github/CODE_OF_CONDUCT.md # 行为准则
```

---

## 📋 **第二步：创建Issue模板**

### 2.1 Bug报告模板（必选）

创建文件：`.github/ISSUE_TEMPLATE/bug_report.md`

markdown

```
---
name: "🐛 Bug 报告"
about: 报告一个错误或问题
title: "[BUG] "
labels: ["bug", "needs-triage"]
assignees: ""
---

## 📝 问题描述
<!-- 清晰描述你遇到的问题 -->

## 🐞 复现步骤
1. 访问 '...'
2. 点击 '....'
3. 滚动到 '....'
4. 看到错误

### 期望行为
<!-- 你期望发生什么 -->

### 实际行为
<!-- 实际发生了什么 -->

## 📸 截图/日志
<!-- 如果适用，添加截图或日志 -->

## 💻 环境信息
- **操作系统**: Windows 10 / macOS 11 / Ubuntu 20.04
- **浏览器**: Chrome 90 / Firefox 88 / Safari 14
- **项目版本**: v1.2.3
- **Node版本**: 14.17.0 (如果适用)

## 📦 附加信息
<!-- 任何其他相关信息 -->
```

### 2.2 功能请求模板（必选）

创建文件：`.github/ISSUE_TEMPLATE/feature_request.md`

markdown

```
---
name: "✨ 功能请求"
about: 为这个项目提出一个新想法
title: "[FEATURE] "
labels: ["enhancement"]
assignees: ""
---

## 📋 需求描述
<!-- 清晰描述你想要的功能 -->

## 🤔 这个功能解决了什么问题？
<!-- 描述你遇到的问题或痛点 -->

## 🎯 解决方案
<!-- 描述你想要的解决方案 -->

## 🔄 替代方案
<!-- 描述你考虑过的替代方案 -->

## 📚 附加信息
<!-- 截图、链接或其他相关信息 -->
```

### 2.3 文档改进模板（可选）

创建文件：`.github/ISSUE_TEMPLATE/documentation.md`

markdown

```
---
name: "📚 文档改进"
about: 报告文档问题或建议改进
title: "[DOCS] "
labels: ["documentation"]
assignees: ""
---

## 📝 文档位置
<!-- 哪个页面的文档需要改进？ -->

## 🔍 当前情况
<!-- 当前文档有什么问题？ -->

## ✨ 建议改进
<!-- 你建议如何改进？ -->

## 🌐 相关链接
<!-- 相关文档的链接 -->
```

---

## 🔄 **第三步：创建PR模板**

创建文件：`.github/PULL_REQUEST_TEMPLATE.md`

markdown

```
# PR 描述
<!-- 描述这个PR做了什么 -->

## 🔗 相关Issue
<!-- 使用关键字关联Issue，如：Closes #123, Fixes #456 -->
- Closes #ISSUE_NUMBER

## 📝 修改类型
<!-- 勾选所有适用的选项 -->

- [ ] Bug修复 (不兼容的修改)
- [ ] 新功能 (不兼容的修改)
- [ ] 代码重构 (不改变功能)
- [ ] 文档更新
- [ ] 测试用例
- [ ] 配置变更
- [ ] 其他...请描述:

## 📋 检查清单
<!-- 在提交PR前确认以下事项 -->

- [ ] 我的代码遵循项目的代码规范
- [ ] 我已经自测了这些更改
- [ ] 我已经更新了相关文档
- [ ] 我已经添加了必要的测试用例
- [ ] 所有测试都通过

## 🧪 测试步骤
<!-- 如何测试这个PR？ -->

1. 运行 `npm test`
2. 访问页面 `http://localhost:3000`
3. 点击按钮 "..."

## 📸 截图
<!-- 如果适用，添加UI变化的截图 -->

| 修改前 | 修改后 |
|--------|--------|
| <img src="" width="300"> | <img src="" width="300"> |

## 🔍 备注
<!-- 任何其他需要说明的事项 -->
```

---

## 🚀 **第四步：创建并关联Issue**

### 4.1 使用模板创建Issue

**在GitHub上操作：**

1. 进入仓库页面
2. 点击  **"Issues"**  标签
3. 点击  **"New issue"**
4. **看到模板选择界面！**  🎉

   - 选择  **"🐛 Bug 报告"**
   - 或  **"✨ 功能请求"**
5. 填写模板内容

**示例创建一个Bug报告：**

markdown

```
标题: [BUG] 登录按钮点击无响应

## 📝 问题描述
在登录页面，点击登录按钮没有任何反应。

## 🐞 复现步骤
1. 访问登录页面 http://example.com/login
2. 输入用户名和密码
3. 点击"登录"按钮
4. 页面无响应，控制台显示错误

### 期望行为
点击后跳转到首页

### 实际行为
页面卡住，无任何反应

## 📸 截图/日志
控制台错误：
```

Uncaught TypeError: Cannot read property 'submit' of null

text

```
## 💻 环境信息
- **操作系统**: macOS 11.2.3
- **浏览器**: Chrome 91
- **项目版本**: v1.0.0
```

### 4.2 提交并获取Issue编号

创建Issue后，GitHub会自动分配一个编号，比如 `#15`

---

## 💻 **第五步：在本地开发中关联Issue**

### 5.1 在commit message中引用Issue

bash

```
# 方法1：在提交信息中直接引用
git commit -m "Fix: 修复登录按钮点击问题

- 修复submit事件监听
- 添加错误处理
- 更新相关测试

Closes #15"

# 方法2：使用关键字（会自动关闭Issue）
git commit -m "fix: 修复登录按钮点击问题, closes #15"

# 方法3：只关联不关闭
git commit -m "refactor: 重构登录模块，related to #15"
```

### 5.2 使用智能提交消息

bash

```
# 常用的GitHub关键字：
# closes #15
# fixes #15
# resolves #15
# related to #15
# see also #15
```

---

## 🔄 **第六步：创建PR并关联关闭Issue**

### 6.1 推送分支

bash

```
# 创建修复分支
git checkout -b fix/login-button-issue

# 进行修复...
# 提交代码（关联Issue）
git add .
git commit -m "fix: 修复登录按钮点击事件监听

- 修复事件绑定问题
- 添加表单验证
- 更新单元测试

Closes #15"

# 推送到远程
git push -u origin fix/login-button-issue
```

### 6.2 创建PR时使用模板

**在GitHub上：**

1. 你会看到提示： **"Compare & pull request"**
2. 点击后自动使用PR模板
3. **填写关键信息：**

markdown

```
# PR 描述
修复登录按钮点击无响应的问题

## 🔗 相关Issue
- Closes #15  <!-- 这个会自动关闭Issue！ -->

## 📝 修改类型
1. [x] Bug修复 (不兼容的修改)

## 📋 检查清单
- [x] 我的代码遵循项目的代码规范
- [x] 我已经自测了这些更改
- [x] 我已经更新了相关文档
- [x] 我已经添加了必要的测试用例
- [x] 所有测试都通过

## 🧪 测试步骤
1. 运行 `npm run test:login`
2. 访问登录页面
3. 输入测试账号
4. 点击登录按钮
5. 验证跳转到首页
```

### 6.3 验证自动关闭机制

**当PR合并时：**

1. GitHub会自动检测到 `Closes #15`
2. **自动关闭Issue #15**
3. 在Issue页面添加评论：

   > "Closed by #16" (PR编号)
   >
4. Issue状态变为  **"Closed"**  ✅

---

## 🎯 **第七步：验证成果**

### 7.1 检查模板是否生效

bash

```
# 确认文件结构
find .github -type f

# 应该看到：
# .github/ISSUE_TEMPLATE/bug_report.md
# .github/ISSUE_TEMPLATE/feature_request.md
# .github/PULL_REQUEST_TEMPLATE.md
```

### 7.2 验证Issue被关闭

1. 访问 `https://github.com/你的用户名/仓库名/issues/15`
2. 应该看到状态为  **"Closed"**
3. 应该看到评论："Closed by #16"

### 7.3 查看关闭记录

bash

```
# 在本地查看提交历史
git log --oneline --grep="#15"

# 或者查看所有与Issue相关的提交
git log --all --grep="#[0-9]*" --oneline
```

‍

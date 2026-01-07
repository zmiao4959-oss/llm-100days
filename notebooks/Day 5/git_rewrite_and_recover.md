# git_rewrite_and_recover

# Git 进阶操作详解

## 1. 交互式 Rebase 用法

### 基本语法

bash

```
git rebase -i <commit>
# 或
git rebase -i HEAD~3  # 编辑最近3个提交
```

### 主要操作命令

|命令|说明|示例|
| ------| --------------------------------| ------|
|**pick**|保留该提交（不做修改）|​`pick a1b2c3d 原提交信息`|
|**reword**|修改提交信息|​`reword a1b2c3d 修改提交信息`|
|**edit**|暂停并修改提交内容|​`edit a1b2c3d 原提交信息`|
|**squash**|合并到前一个提交，保留提交信息|​`squash a1b2c3d 原提交信息`|
|**fixup**|合并到前一个提交，丢弃提交信息|​`fixup a1b2c3d 原提交信息`|
|**drop**|删除该提交|​`drop a1b2c3d 原提交信息`|

### 使用示例

#### 示例1：修改提交信息 (reword)

bash

```
# 修改最近3个提交中的第二个提交信息
git rebase -i HEAD~3
# 编辑界面中，将第二行的 pick 改为 reword
pick e4d5f6g First commit
reword a1b2c3d Second commit  # 修改此提交信息
pick b2c3d4e Third commit
```

#### 示例2：合并提交 (squash/fixup)

bash

```
# 将多个小提交合并为一个
git rebase -i HEAD~4
# 编辑界面
pick a1b2c3d feat: add user model
squash b2c3d4e fix: typo in user model
squash c3d4e5f docs: update user model comments
fixup d4e5f6g style: format code
# 结果：四个提交合并为一个，保留第一个提交信息，合并其他信息
```

#### 示例3：重新排序提交 (edit)

bash

```
# 重新排序并编辑提交
git rebase -i HEAD~3
# 重新排列行顺序来改变提交顺序
```

## 2. Rebase 冲突解决

### 冲突解决流程

bash

```
# 1. 开始rebase
git rebase -i <target-branch>

# 2. 遇到冲突时，Git会暂停
# 查看冲突文件
git status

# 3. 手动解决冲突
# 编辑有冲突的文件，解决冲突标记（<<<<<<<, =======, >>>>>>>）

# 4. 标记冲突已解决
git add <resolved-file>
# 或添加所有已解决的文件
git add .

# 5. 继续rebase
git rebase --continue

# 6. 如果中途想放弃rebase
git rebase --abort

# 7. 跳过当前冲突提交（慎用）
git rebase --skip
```

### 解决策略

bash

```
# 方法1：使用mergetool
git mergetool  # 使用配置的合并工具

# 方法2：查看冲突文件的双方差异
git diff --ours <file>    # 查看当前分支的更改
git diff --theirs <file>  # 查看要合并的分支的更改

# 方法3：接受特定版本
git checkout --ours <file>    # 采用当前分支版本
git checkout --theirs <file>  # 采用对方分支版本
```

## 3. Reset vs Revert 区别

### 对比表格

|特性|git reset|git revert|
| ------| ------------------------------------| ------------------------|
|**目的**|撤销本地提交，**改变历史**|创建新提交来撤销更改，**不改变历史**|
|**影响范围**|本地仓库（已推送时需强制推送）|本地和远程仓库都安全|
|**协作影响**|影响其他协作者，不推荐用于共享分支|安全，不影响其他协作者|
|**提交历史**|删除提交，历史被重写|添加新提交，历史保留|
|**适用场景**|本地未推送的错误提交|已推送的错误提交|

### git reset 详细用法

bash

```
# 三种模式：

# 1. --soft：仅移动HEAD指针，不修改暂存区和工作区
git reset --soft HEAD~1
# 工作区：修改保留
# 暂存区：修改保留
# HEAD：回退到上一个提交

# 2. --mixed（默认）：移动HEAD指针，重置暂存区
git reset HEAD~1
# 或
git reset --mixed HEAD~1
# 工作区：修改保留
# 暂存区：清空
# HEAD：回退到上一个提交

# 3. --hard：移动HEAD指针，重置暂存区和工作区
git reset --hard HEAD~1
# 工作区：修改丢失（危险！）
# 暂存区：清空
# HEAD：回退到上一个提交

# 4. 重置到特定提交
git reset --hard a1b2c3d

# 5. 撤销add操作（从暂存区移除）
git reset HEAD <file>
```

### git revert 详细用法

bash

```
# 1. 撤销单个提交
git revert <commit-hash>
# 会创建一个新的提交来撤销指定提交的更改

# 2. 撤销多个提交（按顺序撤销）
git revert <oldest-commit>..<latest-commit>
# 注意：按时间顺序从旧到新执行

# 3. 撤销最近的提交
git revert HEAD

# 4. 撤销合并提交
git revert -m 1 <merge-commit-hash>
# -m 1 表示保留主分支的更改

# 5. 不自动提交，手动编辑提交信息
git revert --no-commit <commit-hash>
git commit -m "Revert changes from ..."
```

### 使用场景示例

#### 场景1：本地错误提交（未推送）

bash

```
# 错误提交了不需要的文件
git add .
git commit -m "Wrong commit"

# 撤销但保留更改（推荐）
git reset --soft HEAD~1
# 或撤销并清空暂存区
git reset HEAD~1

# 重新提交
git add correct-files.txt
git commit -m "Correct commit"
```

#### 场景2：已推送的错误提交

bash

```
# 已经推送到远程的错误提交
# 使用revert创建撤销提交
git revert <bad-commit-hash>
git push origin main  # 安全推送
```

#### 场景3：彻底放弃本地未提交的修改

bash

```
# 危险！会丢失所有未提交的更改
git reset --hard HEAD
# 或
git checkout -- .
```

### 最佳实践总结

1. ​**个人分支/未推送**​：可以使用 `reset`
2. ​**共享分支/已推送**​：使用 `revert`
3. ​**重要原则**：

   - 对公共分支永远不要使用 `reset --hard`
   - 使用 `reset` 前确保理解三种模式的区别
   - 使用 `revert` 撤销已推送的提交
   - 频繁提交，使用 `rebase -i` 整理提交历史

### 恢复误操作

bash

```
# 查看操作记录
git reflog

# 恢复误reset的操作
git reset --hard HEAD@{1}

# 查看所有分支的所有操作记录
git log --oneline --graph --all
```

这些工具组合使用可以让你更精细地控制代码历史，但记住：​**对公共历史进行重写操作前，请与团队协商**。

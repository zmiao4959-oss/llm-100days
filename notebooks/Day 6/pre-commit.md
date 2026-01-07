# pre-commit

### 🔧 核心工具与配置

你可以通过一个名为 `.pre-commit-config.yaml` 的配置文件来管理所有检查任务（或称“钩子”）。一个典型的配置文件会集成以下流行工具：

|工具|主要功能|配置示例 (在 `.pre-commit-config.yaml` 中)|
| ------| ------------------------------------------------| ---------------------|
|**Black**|**代码格式化**工具，统一代码风格|​`- repo: https://github.com/psf/black`|
|**Ruff**|**代码检查与修复**工具，集成了 linting 和格式化功能，速度极快|​`- repo: https://github.com/astral-sh/ruff-pre-commit`<br />`- id: ruff`|
|**isort**|自动整理和排序 `import` 语句|​`- repo: https://github.com/PyCQA/isort`|
|**flake8**|**代码风格检查**工具，检查是否符合 PEP 8 等规范|​`- repo: https://github.com/PyCQA/flake8`|
|**pre-commit-hooks**|提供一系列​**通用检查**，如检查文件尾行、删除多余空格等|​`- repo: https://github.com/pre-commit/pre-commit-hooks`|

### 📦 安装与设置

在项目根目录下，只需几步即可完成安装和配置：

1. **安装工具**
   通过 pip 安装 `pre-commit` 包：
   bash

   ```
   python -m pip install pre-commit
   ```
2. **创建配置文件**
   在项目根目录创建 `.pre-commit-config.yaml` 文件。可以参考以下基础配置：
   yaml

   ```
   repos:
     - repo: https://github.com/pre-commit/pre-commit-hooks
       rev: v4.5.0
       hooks:
         - id: trailing-whitespace
         - id: end-of-file-fixer
         - id: check-yaml
         - id: check-added-large-files

     - repo: https://github.com/psf/black
       rev: 23.11.0
       hooks:
         - id: black

     - repo: https://github.com/PyCQA/isort
       rev: 5.12.0
       hooks:
         - id: isort

     # 如需使用 Ruff，可添加
     # - repo: https://github.com/astral-sh/ruff-pre-commit
     #   rev: v0.1.9
     #   hooks:
     #     - id: ruff
     #       args: [--fix]
   ```
3. **启用钩子**
   在项目目录下运行以下命令，它会将 `pre-commit` 安装到 Git 的钩子目录中：
   bash

   ```
   pre-commit install
   ```

   至此，每次执行 `git commit`​ 时，配置的检查都会​**自动运行**。

### 💡 使用流程与技巧

配置完成后，标准的代码提交流程如下：

bash

```
git add your_file.py
git commit -m "你的提交信息"
```

如果代码检查​**发现并自动修复了问题**​，你需要将修复后的文件​**重新暂存**​（`git add`​）并再次提交。如果检查​**发现错误但无法自动修复**，提交会被终止，你需要根据提示手动修复。

一些有用的高级命令：

- ​**手动检查所有文件**​：`pre-commit run --all-files`​。这在首次为已有项目设置 `pre-commit` 时非常有用。
- ​**更新工具版本**​：`pre-commit autoupdate` 可以自动将配置文件中的工具更新到最新版本。
- ​**跳过检查**​：在某些情况下，你可以使用 `git commit --no-verify` 来跳过钩子检查。

### 🤝 团队协作建议

为了使 `pre-commit` 在团队中发挥最大效用，建议：

1. ​**配置文件纳入版本控制**​：将 `.pre-commit-config.yaml` 文件提交到 Git 仓库中，确保所有团队成员使用相同的检查规则。
2. ​**统一开发环境**​：鼓励团队成员在本地安装并启用 `pre-commit`。
3. **集成到持续集成（CI）** ：在 CI 流水线中加入 `pre-commit run --all-files` 命令，确保远程仓库的代码也符合规范。

# NOTE:

你可以把 `.pre-commit-config.yaml`​ 文件想象成一个 “**自动安装与执行脚本**”，整个过程是自动化的：

1. ​**读取配置**​：当你执行 `git commit`​ 时，`pre-commit`​ 会读取项目根目录下的 `.pre-commit-config.yaml` 文件。
2. ​**按需下载**​：`pre-commit`​ 会根据文件中每个 `repo`​ 对应的网址和版本号，检查本地是否已缓存。如果没有，它会**自动从远程仓库（如 GitHub）下载**对应的工具包到你的本地全局缓存目录（通常位于 `~/.cache/pre-commit`）。
3. ​**创建独立环境**​：对于每个钩子（尤其是Python工具），`pre-commit`​ 通常会创建一个**独立的、隔离的虚拟环境**来安装和运行它。这确保了工具之间、工具与你的项目环境之间不会产生依赖冲突。
4. **执行检查**：在隔离环境中运行指定的钩子命令，对你要提交的代码进行检查。

​**​`pre-commit install`​**​ **通常只需要在项目的** **每个本地 Git 仓库中执行一次**。之后，无论你如何修改 `.pre-commit-config.yaml` 文件，都不需要重新运行此命令。

### 📌 两者核心区别

|特性|​`git commit` 时自动触发|​`pre-commit run --all-files` (手动命令)|
| ------| ------------------------------| ---------------------------------------|
|**触发方式**|​**自动**（由Git钩子触发）|**手动**执行|
|**检查范围**|仅检查 **​`git add`​**​ **暂存的文件**|检查项目中的所有文件（无论是否被 `git add`）|
|**主要用途**|​**日常开发流程**，确保每次增量提交都合规|**项目初始化、大扫除、调试或CI/CD环境**|
|**运行时间**|快速，只检查少量文件|较慢，会扫描整个项目|

对于你的情况，最清晰的路径是：

1. ​**第一步（一次性大扫除）** ：
   bash

   ```
   # 一次性修复所有历史文件
   pre-commit run --all-files
   git add .
   git commit -m "style: apply pre-commit formatting across entire project"
   ```
   这相当于给你的项目代码库做一次“大扫除”，建立一个干净的基线。
2. ​**第二步（之后的日常开发）** ​：
   完成第一步后，在后续日常开发中，你只需正常使用 `git add`​ 和 `git commit`​。这时 `pre-commit`​ 只会检查你​**本次修改并暂存的文件**，速度快且针对性强。

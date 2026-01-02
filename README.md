# 🚀 100天LLM系统学习与实践计划 | 100-Day LLM Systematic Learning & Practice Plan

## 中文版

### 🌟 项目概述

作为一名非科班的工科学生，对大型语言模型（LLM）的技术原理与应用前景充满好奇与热情。本项目记录了我为期100天的系统性学习旅程——从零基础到具备LLM全栈实践能力的完整路径。这不仅是知识积累的过程，更是工程思维、学习方法和职业能力的综合锻造。

### 🎯 核心理念

**“以项目驱动学习，以指标衡量进步”**——本计划的每个阶段都设有明确的可交付成果和量化指标，确保学习过程可见、可测、可复现。我坚信，在人工智能时代，**工程化能力**与**理论基础**同等重要，因此本计划特别强调环境配置、代码规范、实验记录和项目部署等实践环节。

### 📊 详细路线图

#### **阶段一：环境与工程习惯搭建（第1-7天）**
- **目标**：建立可复现的开发环境与规范的工程工作流
- **关键指标**：
  1. 完成Linux/WSL + CUDA(如需) + Python(Conda/uv)环境配置，导出`environment.yml`/`requirements.txt`
  2. 掌握Git核心工作流（clone/branch/commit/PR/rebase），在GitHub创建公开仓库并完成≥10次规范提交
  3. 搭建个人学习看板（Notion/Obsidian/Trello），制定100天里程碑与每周复盘模板

#### **阶段二：Python工程化与数据处理（第8-18天）**
- **目标**：从“脚本编写”升级为“可维护模块开发”
- **关键指标**：
  1. 完成Python核心特性（数据结构、OOP、异常处理、类型标注、迭代器/生成器）系统练习≥50题
  2. 掌握NumPy/Pandas/Matplotlib，产出包含≥3张可视化图表+≥3个统计指标的小型数据分析报告
  3. 为仓库集成pytest单元测试≥10个，配置ruff/black格式化与pre-commit钩子，实现GitHub Actions CI流水线

#### **阶段三：计算机基础素养补齐（第19-30天）**
- **目标**：构建LLM工程必需的底层知识体系
- **关键指标**：
  1. 掌握Linux常用命令、shell脚本编写、进程/内存/文件权限管理，完成实操清单≥30项
  2. 实现并解析经典数据结构与算法（栈/队列/哈希/堆/并查集/排序/搜索），LeetCode风格题目累计≥40题
  3. 撰写“LLM服务网络链路”技术笔记，涵盖HTTP/HTTPS、REST、WebSocket等，使用curl复现≥5个API调用示例

#### **阶段四：机器学习核心与实验方法（第31-42天）**
- **目标**：建立可复现的ML实验流程与评估直觉
- **关键指标**：
  1. 在公开数据集上训练≥3个对比模型（LR、XGBoost、MLP），形成完整评估对比表
  2. 产出标准化实验报告，涵盖数据处理、模型选择、评估指标与结论分析
  3. 深入理解过拟合、数据泄漏、类别不平衡问题，各提出≥2种解决方案

#### **阶段五：深度学习与PyTorch训练范式（第43-54天）**
- **目标**：掌握模型训练全流程与问题诊断能力
- **关键指标**：
  1. 使用PyTorch从零实现分类模型，集成Dataset/DataLoader、训练循环、学习率调度等完整组件
  2. 深入理解反向传播、优化器、梯度裁剪等核心机制
  3. 完成≥2次训练排障实践，实现指标提升或训练效率优化≥20%

#### **阶段六：LLM基础与Transformer深度解析（第55-63天）**
- **目标**：从“API调用者”转变为“机制理解者”
- **关键指标**：
  1. 撰写≥3000字Transformer核心技术笔记，涵盖Self-Attention、位置编码、LayerNorm等核心模块
  2. 对比实现≥3种解码策略（greedy/beam/top-p/top-k/temperature）
  3. 完成小规模模型推理实验，量化记录吞吐、延迟、显存占用性能指标

#### **阶段七：LLM应用开发：RAG与工具调用（第64-74天）**
- **目标**：构建“问题→方案→实现→评估”的完整应用闭环
- **关键指标**：
  1. 搭建支持≥200份文档的RAG原型系统，集成文档处理、向量检索、生成回答全流程
  2. 建立离线评估体系，基于自建≥50条QA对计算召回率/准确率
  3. 开发可交互Demo，系统收集≥30条失败案例用于迭代优化

#### **阶段八：微调能力：SFT/LoRA/QLoRA与数据工程（第75-86天）**
- **目标**：在真实资源约束下完成可交付的微调任务
- **关键指标**：
  1. 使用LoRA/QLoRA技术完成指令微调实践，支持单卡/多卡环境
  2. 构建并清洗≥2000条高质量指令数据，包含完整的数据校验流程
  3. 在自建评测集上实现关键指标提升≥10%，保存可复现实验配置

#### **阶段九：部署与工程化：模型服务化（第87-95天）**
- **目标**：掌握生产环境部署与性能优化技能
- **关键指标**：
  1. 基于vLLM/TGI/llama.cpp部署推理服务，提供REST API与流式输出
  2. 实施性能压测与优化，实现P95延迟或吞吐量优化≥20%
  3. 集成可观测性工具，能够诊断超时、OOM等常见线上问题

#### **阶段十：作品集与求职对齐（第96-100天）**
- **目标**：将技术能力转化为有效的职业信号
- **关键指标**：
  1. 完善≥2个展示级项目（RAG应用+微调项目），包含完整文档与演示
  2. 产出LLM岗位定制简历，完成≥3次模拟面试并输出复盘清单≥30条
  3. 分析≥30个目标岗位JD，完成首轮投递≥20份并建立反馈跟踪体系

### 🛠️ 学习方法论

本计划采用 **“三维学习法”**：
1. **深度理论**：通过推导、笔记、教学式输出强化理解
2. **动手实践**：每个知识点配套可运行的代码与可测量的结果
3. **工程规范**：从第一天起培养版本控制、测试、文档、可复现的习惯

### 📈 预期成果

- **技术层面**：建立从数据准备、模型训练到服务部署的LLM全栈能力
- **工程层面**：形成严谨的实验方法论与代码规范意识
- **职业层面**：打造有竞争力的技术作品集与岗位匹配策略

### 🤝 邀请参与

无论你是：
- 🤔 对LLM感兴趣但不知如何开始的学习者
- 🧪 希望参考结构化学习路径的同路人
- 🏢 关注工程能力培养的技术导师
- 🔍 寻找潜力人才的招聘者

都欢迎关注本项目进展、提出建议或参与讨论。每一次Star、Fork或Issue都是对我学习旅程的宝贵支持！

---

# 🚀 100-Day LLM Systematic Learning & Practice Plan

## English Version

### 🌟 Project Overview

As a non-computer science engineering student, I am deeply fascinated by the technical principles and application prospects of Large Language Models (LLMs). This project documents my 100-day systematic learning journey—a complete path from foundational knowledge to full-stack LLM practical capabilities. This is not merely an accumulation of knowledge but a comprehensive cultivation of engineering thinking, learning methodologies, and professional competencies.

### 🎯 Core Philosophy

**"Project-driven learning, metrics-measured progress"**—Each phase of this plan has clear deliverables and quantifiable metrics, ensuring the learning process is visible, measurable, and reproducible. I firmly believe that in the era of artificial intelligence, **engineering capability** is equally important as **theoretical foundation**. Therefore, this plan emphasizes practical aspects such as environment setup, code standards, experiment logging, and project deployment.

### 📊 Detailed Roadmap

#### **Phase 1: Environment & Engineering Habits Setup (Days 1-7)**
- **Goal**: Establish reproducible development environments and standardized engineering workflows
- **Key Metrics**:
  1. Configure Linux/WSL + CUDA (if needed) + Python (Conda/uv) environment, export `environment.yml`/`requirements.txt`
  2. Master Git core workflow (clone/branch/commit/PR/rebase), create public GitHub repository with ≥10 standardized commits
  3. Build personal learning dashboard (Notion/Obsidian/Trello) with 100-day milestones and weekly review templates

#### **Phase 2: Python Engineering & Data Processing (Days 8-18)**
- **Goal**: Advance from "script writing" to "maintainable module development"
- **Key Metrics**:
  1. Complete ≥50 systematic exercises on Python core features (data structures, OOP, exception handling, type hints, iterators/generators)
  2. Master NumPy/Pandas/Matplotlib, produce small-scale data analysis report with ≥3 visualizations + ≥3 statistical metrics
  3. Integrate ≥10 pytest unit tests, configure ruff/black formatting with pre-commit hooks, implement GitHub Actions CI pipeline

#### **Phase 3: Foundational Computer Literacy (Days 19-30)**
- **Goal**: Build essential underlying knowledge system for LLM engineering
- **Key Metrics**:
  1. Master Linux commands, shell scripting, process/memory/file permission management, complete ≥30 practical tasks
  2. Implement and analyze classic data structures & algorithms (stack/queue/hash/heap/union-find/sorting/search), solve ≥40 LeetCode-style problems
  3. Write "LLM Service Network Pipeline" technical notes covering HTTP/HTTPS, REST, WebSocket, reproduce ≥5 API call examples using curl

#### **Phase 4: Machine Learning Core & Experimental Methods (Days 31-42)**
- **Goal**: Establish reproducible ML experimental workflows and evaluation intuition
- **Key Metrics**:
  1. Train ≥3 comparative models (LR, XGBoost, MLP) on public dataset, create comprehensive evaluation comparison table
  2. Produce standardized experiment report covering data processing, model selection, evaluation metrics, and conclusions
  3. Deeply understand overfitting, data leakage, class imbalance, propose ≥2 solutions for each problem

#### **Phase 5: Deep Learning & PyTorch Training Paradigm (Days 43-54)**
- **Goal**: Master end-to-end model training pipeline and problem diagnosis capabilities
- **Key Metrics**:
  1. Implement classification model from scratch using PyTorch, integrate complete components (Dataset/DataLoader, training loop, learning rate scheduling)
  2. Deeply understand backpropagation, optimizers, gradient clipping, and other core mechanisms
  3. Complete ≥2 training troubleshooting practices, achieve ≥20% metric improvement or training efficiency optimization

#### **Phase 6: LLM Fundamentals & Transformer Deep Dive (Days 55-63)**
- **Goal**: Transform from "API consumer" to "mechanism understander"
- **Key Metrics**:
  1. Write ≥3000-word technical notes on Transformer core components (Self-Attention, positional encoding, LayerNorm, etc.)
  2. Compare and implement ≥3 decoding strategies (greedy/beam/top-p/top-k/temperature)
  3. Conduct small-scale model inference experiment, quantitatively record throughput, latency, and memory usage metrics

#### **Phase 7: LLM Application Development: RAG & Tool Calling (Days 64-74)**
- **Goal**: Build complete "problem→solution→implementation→evaluation" application loop
- **Key Metrics**:
  1. Develop RAG prototype supporting ≥200 documents, integrating document processing, vector retrieval, and answer generation
  2. Establish offline evaluation system calculating recall/accuracy based on self-built ≥50 QA pairs
  3. Develop interactive demo, systematically collect ≥30 failure cases for iterative improvement

#### **Phase 8: Fine-tuning Capability: SFT/LoRA/QLoRA & Data Engineering (Days 75-86)**
- **Goal**: Complete deliverable fine-tuning tasks under real resource constraints
- **Key Metrics**:
  1. Practice instruction fine-tuning using LoRA/QLoRA techniques, supporting single/multi-GPU environments
  2. Build and clean ≥2000 high-quality instruction data samples with complete validation pipeline
  3. Achieve ≥10% key metric improvement on self-built evaluation set, save reproducible experiment configuration

#### **Phase 9: Deployment & Engineering: Model Servicization (Days 87-95)**
- **Goal**: Master production deployment and performance optimization skills
- **Key Metrics**:
  1. Deploy inference service using vLLM/TGI/llama.cpp, provide REST API and streaming output
  2. Conduct performance testing and optimization, achieve ≥20% P95 latency reduction or throughput improvement
  3. Integrate observability tools, capable of diagnosing common production issues (timeout, OOM, etc.)

#### **Phase 10: Portfolio & Career Alignment (Days 96-100)**
- **Goal**: Transform technical capabilities into effective career signals
- **Key Metrics**:
  1. Polish ≥2 showcase projects (RAG application + fine-tuning project) with complete documentation and demos
  2. Create LLM-position-targeted resume, complete ≥3 mock interviews with ≥30复盘 points output
  3. Analyze ≥30 target job descriptions, submit ≥20 initial applications and establish feedback tracking system

### 🛠️ Learning Methodology

This plan adopts a **"Three-Dimensional Learning Approach"**:
1. **Deep Theory**: Strengthen understanding through derivations, note-taking, and teach-style output
2. **Hands-on Practice**: Pair each knowledge point with runnable code and measurable results
3. **Engineering Standards**: Cultivate habits of version control, testing, documentation, and reproducibility from day one

### 📈 Expected Outcomes

- **Technical Level**: Establish full-stack LLM capabilities from data preparation and model training to service deployment
- **Engineering Level**: Form rigorous experimental methodology and code standardization awareness
- **Career Level**: Build competitive technical portfolio and job matching strategy

### 🤝 Invitation to Participate

Whether you are:
- 🤔 A learner interested in LLMs but unsure where to start
- 🧪 A fellow traveler seeking reference for structured learning paths
- 🏢 A technical mentor focused on engineering skill development
- 🔍 A recruiter searching for potential talent

You are welcome to follow this project's progress, provide suggestions, or participate in discussions. Every Star, Fork, or Issue is valuable support for my learning journey!

---

**📅 Start Date**: [2026.01.01] | **🏷️ Tags**: #LLM #LearningJourney #100DaysOfCode #AIEngineering #CareerDevelopment

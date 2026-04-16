# 🎮 情感游戏NPC与AI学习之旅 (FeelingGame-NPC & AI Learning Journey)

> **我的个人学习与项目仓库**，记录我从半导体操作工转型AI工程师的成长历程。目标：一年内，通过开发一款具有情感AI的对话游戏原型，找到AI工程师的工作。

## 📋 关于本项目

本项目记录了我从零开始学习AI，并最终开发一个“情感游戏NPC原型”的全过程。我坚信“官方文档+前沿论文+动手实践”是最好的学习方式。所有资料和代码都将在此开源。

## 🎯 项目愿景与可行性分析

### 愿景
开发一款游戏，其中的每个NPC都拥有独立的记忆、性格和情感，能与玩家进行有温度、有深度的动态对话，让游戏世界真正“活”起来。

### 可行性分析
*   **优势**：计算机本科背景提供坚实基础；半导体行业经验为“AI+硬件”方向带来独特视角；当前正值Agent技术爆发期。
*   **挑战**：个人开发资源有限，时间紧迫，目标具有一定复合性。
*   **策略**：将宏大目标分解，第一年聚焦于构建一个可展示的**情感对话系统原型**，作为求职的核心作品。入职后，再利用业余时间迭代完善。

## 🗺️ 12个月学习与项目路线图

> 这是一个“以项目为驱动”的路线图，每个阶段的学习都是为了服务下一阶段的开发。

### 🗓️ 第一阶段：AI与Agent基础 (1-3月) - 项目准备期
*   **学习重点**：Python、PyTorch基础、Agent基本概念。
*   **主要资源**：
    *   [Python官方教程](https://docs.python.org/3/tutorial/)
    *   [Scikit-learn官方教程](https://scikit-learn.org/stable/getting_started.html)
    *   [Google 5-Day AI Agents Intensive Course](https://deepwiki.com/google/adk-docs/Learning-Resources-and-Tutorials)
    *   论文：[A Survey of LLM-based Autonomous Agents](https://arxiv.org/abs/2308.11432)
*   **项目实践**：完成Kaggle入门竞赛，开始构思游戏世界观。

### 🗓️ 第二阶段：深度框架与Agent实战 (4-6月) - 核心开发期
*   **学习重点**：PyTorch、LangChain、Unity/Unreal基础。
*   **主要资源**：
    *   [PyTorch 60-Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
    *   [LangChain Agents官方文档](https://docs.langchain.com/agents/)
    *   [Unity Learn](https://learn.unity.com/) / [Unreal Engine学习](https://dev.epicgames.com/community/unreal-engine/learning)
    *   论文：[Drive-Based Behavior Modeling for Emotionally Responsive NPCs](https://sol.sbc.org.br/index.php/sbgames_estendido/article/view/32812)
*   **项目实践**：搭建首个AI NPC原型，实现基础对话功能。

### 🗓️ 第三阶段：项目迭代与工程化 (7-9月) - 项目强化期
*   **学习重点**：RAG、记忆系统、代码重构。
*   **主要资源**：
    *   [LangChain RAG教程](https://python.langchain.com/docs/tutorials/rag/)
    *   [MLflow文档](https://mlflow.org/docs/latest/index.html)
*   **项目实践**：为NPC加入情感记忆和RAG能力，并进行代码重构和工程化。

### 🗓️ 第四阶段：求职冲刺 (10-12月) - 求职与展示期
*   **学习重点**：系统设计、面试技巧。
*   **主要资源**：各大公司的招聘JD、技术博客。
*   **项目实践**：完善项目文档，制作演示视频，启动求职。

## 🤖 Agent专项学习资源库

### 官方教程与课程
| 资源 | 链接 | 说明 |
|------|------|------|
| Microsoft Agent Academy | [Link](https://devblogs.microsoft.com/powerplatform/agent-academy-spring-drop/) | 官方免费Agent构建课程 |
| LangChain Agents | [Docs](https://docs.langchain.com/agents/) | Agent开发首选文档 |
| Google ADK 5-Day Course | [DeepWiki](https://deepwiki.com/google/adk-docs/Learning-Resources-and-Tutorials) | Google官方Agent课程 |
| Databricks Agent Course | [Databricks](https://www.databricks.com/blog/building-single-agent-applications-databricks) | 涵盖Agent全生命周期 |

### 必读论文
| 论文 | 链接 | 说明 |
|------|------|------|
| A Survey of LLM-based Autonomous Agents | [arXiv:2308.11432](https://arxiv.org/abs/2308.11432) | 领域全景图，入门必读 |
| The Rise and Potential of LLM Based Agents | [arXiv:2309.07864](https://arxiv.org/abs/2309.07864) | 复旦NLP团队经典综述 |
| OS Agents: A Survey | [arXiv:2412.10980](https://arxiv.org/abs/2412.10980) | 操作OS环境的前沿方向 |

### 前沿Agent框架
| 框架 | 链接 | 特点 |
|------|------|------|
| LangChain | [GitHub](https://github.com/langchain-ai/langchain) | 功能全面，生态强大 |
| AutoGen | [GitHub](https://github.com/microsoft/autogen) | 微软开源，多Agent协作 |
| CrewAI | [官网](https://www.crewai.com/) | 角色扮演式Agent团队 |
| OpenAI Agents SDK | [GitHub](https://github.com/openai/openai-agents-python) | OpenAI官方，轻量级 |
| Smolagents | [GitHub](https://github.com/huggingface/smolagents) | Hugging Face出品，极简 |

## 📁 项目目录结构 (规划)
/FeelingGame-NPC/
├── docs/ # 设计文档、学习笔记
├── prototypes/ # 各阶段原型代码
│ ├── phase1_basics/ # 基础学习脚本
│ ├── phase2_agent/ # Agent对话原型
│ └── phase3_emotion/ # 情感系统原型
├── game_project/ # 最终游戏项目源码
│ ├── assets/ # 游戏资源
│ ├── scripts/ # C# (Unity) 或 C++/蓝图 (Unreal)
│ └── models/ # 训练或下载的模型文件
├── README.md # 项目主文档 (本文件)
└── progress.md # 个人学习进度追踪

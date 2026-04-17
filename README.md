# 🎒 情感校园 · AI 叙事游戏 (Campus Soul)

> 一个以“真实社交模拟”为核心的校园恋爱 AI 游戏。  
> **边学边做，一年为期。**  
> 核心理念：每个 NPC 都有自己的背景、情感和偏见——校园即微型社会，而你的每一次开口，都可能改变一段关系。

---

## 📋 关于本项目

本项目是一个**学习+开发**一体化的个人计划。目标是：
1. **系统学习 AI 应用开发**，掌握大模型调用、Agent 设计、RAG 等核心技能。
2. **独立完成一款可展示的 AI 游戏原型**，证明从 0 到 1 的工程能力。
3. **为社恐人群提供一个安全的“社交练习场”**——在虚拟世界中迈出开口的第一步。
4. **对齐 2026 年 AI 岗位市场需求**，通过项目掌握行业最急需的技术栈。

---

## 🎯 游戏愿景

你是一名转校生，来到一所看似普通却暗藏无数故事的校园。  
这里的每个学生都有：
- **独立的生活背景**（家庭条件、过往经历、学业压力）
- **真实的情感与偏见**（有人因外貌疏远你，有人因你的家境靠近你）
- **动态变化的态度**（你的每一句话，都会影响他们对你的看法）

你可以通过**语音或文字**与他们自由对话。  
没有预设的“好感度选项”，只有你真实想说的话。  
AI 会根据角色的人设、记忆、当前情绪，给出独一无二的回应。

**最终，你会和谁成为挚友？又会和谁发展出超越友情的关系？**  
故事由你书写，但终点早已埋下伏笔。

---

## 🧠 技术特色

- **双模式 AI 架构**：玩家可一键切换“云端智能模式”与“纯本地离线模式”，两种模式均可完整体验游戏。
- **情感状态机**：好感度、信任值、情绪维度实时计算，影响 AI 的语气与决策。
- **长期记忆系统（RAG）**：NPC 会记住你们的关键对话，关系具有延续性。
- **AI Agent 行为系统**：NPC 能根据对话自主执行游戏内动作（如赠送物品、改变场景）。
- **真实偏见模拟**：NPC 对玩家的初始态度受外貌、家境等设定影响，形成差异化社交体验。

---

## 📊 技术栈与市场岗位对齐分析

本项目所采用的技术，精准对齐 2026 年 AI 应用开发岗位的核心需求。

| 市场需求 (2026 AI 应用开发岗) | 本项目涵盖情况 | 对应模块 |
| :--- | :--- | :--- |
| **Python 编程** | ✅ 主力开发语言 | 全项目 |
| **大模型 API 调用** | ✅ DeepSeek / 智谱 / 通义千问 | `llm_interface.py` |
| **Prompt Engineering** | ✅ 角色卡 + 系统指令设计 | 角色卡 JSON + Prompt 模板 |
| **RAG (检索增强生成)** | ✅ 向量检索历史对话 | ChromaDB 记忆模块 |
| **AI Agent / Tool Calling** | ✅ NPC 可调用游戏内函数 | LangChain Tools / OpenAI Agents SDK |
| **LangChain 框架** | ✅ 核心对话管理与 Agent 编排 | 全 AI 模块 |
| **向量数据库** | ✅ ChromaDB | `memory_manager.py` |
| **模型本地部署** | ✅ Ollama + 小模型离线模式 | `local_mode` 模块 |
| **FastAPI / 服务化** | 🟡 可扩展为 API 服务 | 后续迭代方向 |

**结论**：本项目覆盖了当前 AI 应用开发岗位 **80% 以上的核心技能要求**。完成本项目后，你将具备应聘 **AI 应用开发工程师、大模型应用开发、AI 产品技术岗** 的硬实力。

### 附加优势：行业背景
具备半导体/制造业现场经验的技术人员，在应聘 **工业 AI、智能制造、AI 产品质量** 等岗位时，因兼具业务理解与技术能力，往往比纯 CS 背景候选人更具竞争力。

---

## 🗺️ 综合学习与开发路线图

> **总时长：12 个月。**  
> 学习与开发同步进行，每一阶段的学习内容直接服务于该阶段的开发任务，并对齐市场需求。

### 📅 第一阶段：地基（第 1-3 个月）
**学习重点**：Python 编程、API 调用、Prompt 工程基础  
**对齐岗位技能**：Python, LLM API, Prompt Engineering

| 学习内容 | 对应资源（官方文档优先） | 开发产出 |
| :--- | :--- | :--- |
| Python 基础复习 | [Python 官方教程](https://docs.python.org/3/tutorial/) | 完成 2-3 个小脚本练习 |
| 大模型 API 调用 | [DeepSeek API 文档](https://platform.deepseek.com/api-docs/) 或 [智谱AI 文档](https://open.bigmodel.cn/dev/api) | 写一个命令行对话脚本，测试角色扮演效果 |
| Prompt 设计基础 | [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | 设计第一张“角色卡”JSON，并能让 AI 稳定扮演 |
| 游戏引擎入门 | [Godot 官方教程](https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html) 或 [Unity Learn](https://learn.unity.com/) | 搭建一个最简单的对话框 UI，并能调用 AI 模块 |
| **里程碑** | **云端模式原型**：游戏窗口里有一个 NPC 立绘，输入文字，TA 能用人设回复你 | |

---

### 📅 第二阶段：注入灵魂（第 4-6 个月）
**学习重点**：LangChain 基础、RAG、向量数据库  
**对齐岗位技能**：LangChain, RAG, Vector DB (核心加分项)

| 学习内容 | 对应资源（官方文档优先） | 开发产出 |
| :--- | :--- | :--- |
| LangChain 核心模块 | [LangChain 官方文档](https://python.langchain.com/docs/introduction/) | 使用 LangChain 管理对话历史与 Prompt 模板 |
| RAG 与向量数据库 | [ChromaDB 文档](https://docs.trychroma.com/) | 将对话记录存入 ChromaDB，实现“回忆”功能 |
| 情感状态机设计 | 自定义 Python 类（好感度、信任值、情绪标签） | NPC 能根据对话内容更新好感度，并影响回复语气 |
| 游戏引擎进阶 | 学习引擎的 UI 交互、数据持久化 | 实现游戏存档/读档，记忆数据本地保存 |
| **里程碑** | **记忆+情感原型**：NPC 能记住你昨天说过的话，并且态度随好感度变化 | |

---

### 📅 第三阶段：开口说话 & Agent 觉醒（第 7-9 个月）
**学习重点**：AI Agent、Function Calling、语音交互  
**对齐岗位技能**：AI Agent, Tool Calling, 多模态交互

| 学习内容 | 对应资源（官方文档优先） | 开发产出 |
| :--- | :--- | :--- |
| Agent 与 Function Calling | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) 或 [LangChain Tools](https://python.langchain.com/docs/how_to/tools/) | 让 NPC 能“做动作”（如递东西、改变表情） |
| 本地语音识别 | [whisper.cpp](https://github.com/ggerganov/whisper.cpp) | 在 Python 中调用 whisper.cpp 实现语音转文字 |
| 本地语音合成 | [Piper TTS](https://github.com/rhasspy/piper) | 将 AI 回复转为语音播放 |
| 本地模式基础搭建 | [Ollama](https://ollama.com/) | 测试 Qwen3-8B 或 Llama3-8B-Chinese 本地对话效果 |
| **里程碑** | **语音交互 + Agent 原型**：可以用麦克风对话，NPC 能执行简单动作 | |

---

### 📅 第四阶段：双模式融合与工程化（第 10-12 个月）
**学习重点**：系统架构设计、项目工程化、文档撰写  
**对齐岗位技能**：模型部署、API 设计、项目展示能力

| 学习内容 | 对应资源（官方文档优先） | 开发产出 |
| :--- | :--- | :--- |
| 模式切换架构 | 自定义统一的 AI 接口类 | 实现游戏设置中一键切换云端/本地模式 |
| 叙事进度系统 | 自定义 `StoryDirector` 类 | 植入 3-5 个关键事件触发器，引导故事走向预设结局 |
| 批量角色生成 | 编写 Python 脚本 | 生成 50 张角色卡，包含不同背景、偏见、喜好 |
| 项目打包与演示 | 引擎导出功能 | 制作一个可独立运行的 Demo，录制演示视频 |
| 文档与博客 | Markdown, GitHub | 完善 README，撰写技术博客，准备面试作品 |
| **最终里程碑** | **可展示的完整游戏原型** + **GitHub 项目** + **技术博客** | |

---

## 🛠️ 技术栈总览

| 层级 | 云端模式 | 本地模式 |
| :--- | :--- | :--- |
| **游戏引擎** | Godot 4 / Unity | 同左 |
| **AI 对话** | DeepSeek / 智谱AI / 通义千问 API | Ollama + Qwen3-8B / Llama3-8B-Chinese |
| **AI 框架** | LangChain / OpenAI Agents SDK | 同左 |
| **语音识别** | （可选）云端 STT | whisper.cpp |
| **语音合成** | （可选）云端 TTS | Piper TTS |
| **记忆存储** | ChromaDB (向量) + SQLite (结构化) | 同左 |
| **情感计算** | Python 自定义模块 | 同左 |

---

## 📁 项目目录结构（规划）

```text
/CampusSoul/
├── docs/                      # 设计文档
│   ├── game_design.md         # 世界观、结局设定、角色关系网
│   ├── character_cards/       # 50 张 NPC 角色卡 (JSON)
│   └── learning_log.md        # 个人学习笔记与踩坑记录
├── game/                      # 游戏工程
│   ├── scenes/                # 场景文件
│   ├── scripts/               # 游戏逻辑脚本
│   │   ├── ai_bridge.gd       # 统一 AI 调用接口
│   │   ├── cloud_mode.gd      # 云端模式实现
│   │   ├── local_mode.gd      # 本地模式实现
│   │   └── story_director.gd  # 叙事进度管理
│   └── assets/                # 临时/免费素材
├── ai_modules/                # 独立 AI 模块 (Python)
│   ├── llm_interface.py       # 统一大模型调用
│   ├── memory_manager.py      # ChromaDB 封装
│   ├── emotion_engine.py      # 情感状态计算
│   ├── agent_tools.py         # Agent 工具函数定义
│   ├── stt_whisper.py         # 语音识别封装
│   └── tts_piper.py           # 语音合成封装
├── tools/                     # 辅助脚本
│   ├── character_generator.py # 批量生成角色卡
│   └── test_api.py            # API 连通性测试
├── README.md                  # 本文件
└── requirements.txt           # Python 依赖清单
```

---

### 📚 核心学习资源清单

## 编程与框架

 [Python 官方教程](https://docs.python.org/3/tutorial/) 

 [Godot 官方教程](https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html) 

 [LangChain 官方文档](https://python.langchain.com/docs/introduction/) 

## 大模型与 API

 [DeepSeek API 文档](https://platform.deepseek.com/api-docs/) 

 [智谱AI 文档](https://open.bigmodel.cn/dev/api)

 [Ollama](https://ollama.com/) 

## 语音技术

 [whisper.cpp](https://github.com/ggerganov/whisper.cpp) 

 [Piper TTS](https://github.com/rhasspy/piper) 
 
 ---

## 📚 必读论文

- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)  
  斯坦福 AI 小镇，NPC 记忆与社交行为的奠基之作。

- [A Survey of LLM-based Autonomous Agents](https://arxiv.org/abs/2308.11432)  
  AI Agent 领域全景综述，理解 Agent 四大核心模块的必读指南。

---

### 💡 设计理念：为什么这款游戏有意义
## 为社恐者创造一个“安全区”
在现实中不敢开口的人，可以在虚拟世界练习表达。NPC 的反应虽然真实，但不会带来现实中“被拒绝”的创伤。

## 模拟微型社会
偏见、喜好、利益——这些真实社交中的微妙元素被显式地写入角色卡。玩家会直观感受到：世界不是围着你转的，你需要学会理解他人。

## 过程自由，终点有光
无论你在过程中如何“搞砸”，故事最终都会走向一个温暖的结局。这是一种无声的鼓励：开口，永远比沉默更接近幸福。

---

### 📈 进度追踪
Phase 1：完成云端对话原型

Phase 2：实现记忆与情感系统（RAG）

Phase 3：集成语音交互与 Agent

Phase 4：完成双模式与叙事系统

Phase 5：打包 Demo，输出技术博客

---

### 📄 许可证

MIT License

---

## “每一个不敢开口的灵魂，都值得拥有一个练习告白的夏天。”
## 项目启动：2026.04

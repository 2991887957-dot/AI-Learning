# 100 天 AI Agent 工程师训练营

> 目标岗位：AI Application Engineer / AI Agent 开发工程师 / LLM 应用开发工程师
>
> 前置条件：软件工程专业在读，每天 2 小时
>
> 核心原则：**写代码 > 看视频，项目质量 > 项目数量，笔记 > 收藏**

---

## 总览

```
Python 工程基础    ████████████████████████████ Day 01-28  (4 周)
AI API 开发        ██████████████             Day 29-42  (2 周)
LangChain 核心     ███████                   Day 43-49  (1 周)
RAG 深入           ████████████████████████   Day 50-77  (4 周)
Agent 开发         ██████████████             Day 78-91  (2 周)
毕业项目 + 就业    ██████                     Day 92-100 (1.5 周)
```

每个阶段之间留 1-2 天缓冲（复习/补进度/休息）。

---

## 每日固定流程

| 环节 | 时间 | 做什么 |
|---|---|---|
| ① 理论 | 25 min | 读官方文档/指定资料，做笔记 |
| ② 我讲 | 10 min | 回顾理解，确认没有跑偏 |
| ③ 写代码 | 60 min | 动手完成当日任务 |
| ④ Git 提交 | 10 min | commit + push，写清楚的 commit message |
| ⑤ 总结 | 15 min | 写今日笔记：学了什么、遇到什么坑、一个核心理解 |

---

## 笔记规范（每天都要写）

```markdown
# Day XX: 主题

## 学了什么
- 概念 1：一句话解释
- 概念 2：一句话解释

## 核心代码
```python
# 今天最关键的一段代码

## 遇到的问题
- 报错：xxx → 原因：xxx → 解决：xxx

## 今天最深的理解
- （用一句话写你今天真正"悟了"的东西）
```

笔记放在 `notes/day-XX.md`，每天提交。

---

# 第一阶段：Python 工程能力（Day 01-28）

> 目标：以后看到任何 Python 项目都能看懂，能独立搭建工程化的 Python 项目。

---------------------------------------------------------------------

## Day 01 ✅ 已完成

**主题：** 开发环境搭建

- Python、Git、GitHub、SSH、VS Code
- 仓库：[AI-Learning](https://github.com)

---------------------------------------------------------------------

## Day 02

**🎯 目标：** 理解面向对象的核心——什么是对象，为什么要用 class

**📚 理论（25 min）：**
- 阅读：[Python 官方文档 - 9. Classes](https://docs.python.org/3/tutorial/classes.html)
- 只看 9.1-9.3（Name and Objects、Scopes、Class Definition）
- 必须能回答：什么是对象？什么是实例？self 是什么？为什么需要 class？
1.对象（object）= 数据+方法
2.类（class）就是对象的模板
3.实例（instance）就是根据类创建出来的具体对象
4.self代表当前实例对象本身
5.将相关的数据和方法组织在一起
  提高代码复用性
  让对象结构更加清晰
  更容易维护和扩展程序
**💻 实操（90 min）：**

```
student_manager/
├── main.py
├── student.py
└── manager.py
```

- `Student`：姓名、年龄、学号
- `Manager`：增加、删除、查询、显示全部
- 在 `main.py` 中写一个简单的命令行交互

**✅ 验收：** 能 add/delete/list/query 学生

**📝 提交：** `feat: student manager v1`

---------------------------------------------------------------------

## Day 03

**🎯 目标：** 用 dataclass 和 typing 写更规范的代码

**📚 理论（25 min）：**
- [dataclasses 官方文档](https://docs.python.org/3/library/dataclasses.html)
- [typing 官方文档](https://docs.python.org/3/library/typing.html) — 只看 `str`, `int`, `list`, `dict`, `Optional`, `Any`

**💻 实操（90 min）：**
- 用 `@dataclass` 重构 Student
- 给所有函数加上 type hints
- 感受 dataclass 和普通 class 的区别

**✅ 验收：** 所有函数有 type hints，Student 用 @dataclass

**📝 提交：** `refactor: use dataclass and type hints`

---

## Day 04

**🎯 目标：** 程序不能因为输入错误就崩溃

**📚 理论（25 min）：**
- [Python 官方 - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- `try / except / finally / raise`
- 什么时候该 catch，什么时候该 let it crash

**💻 实操（90 min）：**
- 学生管理系统：输入 `abc` 当年龄不能崩
- 添加自定义异常：`StudentNotFoundError`
- 写合理的错误提示

**✅ 验收：** 输入任何垃圾数据程序都不崩，错误提示清晰

**📝 提交：** `feat: exception handling`

---

## Day 05

**🎯 目标：** 数据能存下来——文件操作和 JSON

**📚 理论（25 min）：**
- [Python 官方 - Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [json 模块](https://docs.python.org/3/library/json.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html) — 用 Path 而不是字符串拼路径

**💻 实操（90 min）：**
- 学生数据保存到 `students.json`
- 程序启动时自动加载
- 用 `pathlib.Path` 处理文件路径

**✅ 验收：** 关闭程序 → 重新打开 → 数据还在

**📝 提交：** `feat: persistent storage with json`

---

## Day 06

**🎯 目标：** 日志和模块化——代码开始像"正经项目"

**📚 理论（25 min）：**
- [logging 官方文档](https://docs.python.org/3/howto/logging.html) — 只看 basicConfig 和几个 level
- [modules](https://docs.python.org/3/tutorial/modules.html) — `__init__.py` 的作用
- package 和 module 的区别

**💻 实操（90 min）：**
- 给 student_manager 加 logging（info / warning / error）
- 重构目录结构：

```
student_manager/
├── models/        # Student dataclass
│   └── __init__.py
├── services/      # 业务逻辑
│   └── __init__.py
├── utils/         # 工具函数（日志配置等）
│   └── __init__.py
└── main.py
```

**✅ 验收：** 目录结构清晰，日志输出规范

**📝 提交：** `refactor: modular project structure with logging`

---

## Day 07

**🎯 目标：** 复盘和巩固

**💻 实操（90 min）：**
- 从零重写 student_manager（不看之前的代码）
- 写 Week 1 总结笔记
- 整理 GitHub README

**📝 提交：** `docs: week 1 summary`

---

## Day 08

**🎯 目标：** 写测试——这是面试必问，工作中必用

**📚 理论（25 min）：**
- [pytest 官方文档](https://docs.pytest.org/en/stable/getting-started.html)
- `pip install pytest`
- `assert`、`fixture`、`parametrize`
- 测试文件命名：`test_*.py`
- 为什么测试重要？一个没有测试的项目 = 不可维护

**💻 实操（90 min）：**
- 给 student_manager 写测试：

```
tests/
├── test_student.py
├── test_manager.py
```

- 至少写 10 个测试用例
- 运行 `pytest -v`

**✅ 验收：** 10+ 测试全部通过

**📝 提交：** `test: add pytest tests for student manager`

---

## Day 09

**🎯 目标：** 列表推导式、生成器、lambda——让 Python 代码更"Pythonic"

**📚 理论（25 min）：**
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- generator expression vs list comprehension
- `lambda`、`map`、`filter`、`reduce`
- `sorted(key=...)` 的用法

**💻 实操（90 min）：**
- 把 manager.py 里的 for 循环尽可能改成推导式（合适的才改）
- 写一个数据处理的练习脚本：过滤、排序、分组
- 对比性能：list vs generator

**✅ 验收：** 能解释何时用推导式、何时用生成器

**📝 提交：** `feat: pythonic data processing`

---

## Day 10

**🎯 目标：** 装饰器和上下文管理器——两个最常用的 Python 高级特性

**📚 理论（25 min）：**
- [装饰器](https://docs.python.org/3/glossary.html#term-decorator) — 函数是一等公民
- `@staticmethod`、`@classmethod`、`@property`
- 自己写一个装饰器（计时器）
- [context manager](https://docs.python.org/3/library/contextlib.html) — `with` 语句
- 写一个 `@contextmanager`（文件自动关闭、数据库连接自动释放）

**💻 实操（90 min）：**
- 写一个 `@timer` 装饰器（打印函数执行时间）
- 写一个 `@retry` 装饰器（失败自动重试 N 次）
- 写一个 `FileManager` context manager

**✅ 验收：** 能自己写出装饰器，解释 `with` 背后的 `__enter__` / `__exit__`

**📝 提交：** `feat: decorators and context managers`

---

## Day 11

**🎯 目标：** 异步编程基础——AI 应用的性能核心

**📚 理论（25 min）：**
- [asyncio 官方文档](https://docs.python.org/3/library/asyncio.html) — 先看 Coroutines and Tasks
- `async def` / `await` / `asyncio.run()`
- 并发 vs 并行（一个服务员 vs 多个服务员）
- 为什么 AI 应用必须用 async？（同时调 3 个 API，不等任何一个）

**💻 实操（90 min）：**
- 写同步版本和异步版本的 `sleep(1)` × 10 次，对比时间
- 用 `asyncio.gather()` 并发执行
- 理解：同步 10 秒，异步 1 秒

**✅ 验收：** 能解释为什么 async 快，什么场景用它

**📝 提交：** `feat: async io basics`

---

## Day 12

**🎯 目标：** 异步进阶——aiohttp 和实际场景

**📚 理论（25 min）：**
- `aiohttp` 基本用法
- 用 `aiohttp` 并发请求多个 URL
- 错误处理：部分请求失败怎么办

**💻 实操（90 min）：**
- 写一个脚本：并发请求 5 个公开 API
- 对比同步 requests vs 异步 aiohttp 的时间
- 处理超时和错误

**✅ 验收：** 异步版本明显快于同步版本，错误不阻塞其他请求

**📝 提交：** `feat: async http with aiohttp`

---

## Day 13

**🎯 目标：** 虚拟环境和包管理——让项目可复现

**📚 理论（25 min）：**
- [uv 官方文档](https://docs.astral.sh/uv/)
- `uv init` / `uv add` / `uv sync`
- `pyproject.toml` 的结构
- 和 `pip` / `venv` 的区别
- 为什么每个项目都要独立环境

**💻 实操（90 min）：**
- 用 `uv init` 创建新项目 `todo-cli`
- 添加依赖：`pytest`, `rich`（终端美化库）
- 写一个简单的命令行 Todo 工具

**✅ 验收：** `uv sync` 能复现环境，`pyproject.toml` 配置正确

**📝 提交：** `feat: todo-cli with uv`

---

## Day 14

**🎯 目标：** 项目实战——Todo CLI 完整版

**📚 理论（25 min）：**
- 复习装饰器、异常处理、文件 IO、async
- 每个都用到 Todo 项目里

**💻 实操（90 min）：**
```
todo-cli/
├── pyproject.toml
├── src/
│   └── todo/
│       ├── __init__.py
│       ├── models.py      # @dataclass TodoItem
│       ├── storage.py     # 文件读写
│       ├── cli.py         # 命令行交互
│       └── main.py
└── tests/
    └── test_todo.py
```

**✅ 验收：** 完整的增删改查 + 数据持久化 + 测试

**📝 提交：** `feat: complete todo-cli`

---

## Day 15

**🎯 目标：** FastAPI 入门——把代码变成 API

**📚 理论（25 min）：**
- [FastAPI 官方文档](https://fastapi.tiangolo.com/) — First Steps 和 Path Parameters
- 什么是 REST API
- `@app.get()` / `@app.post()`
- `uvicorn` 启动服务

**💻 实操（90 min）：**
- 写第一个 FastAPI 应用：`/health` 返回 `{"status": "ok"}`
- 把 Todo CLI 的功能改成 API：

```
GET    /todos        # 列出所有
POST   /todos        # 创建
GET    /todos/{id}   # 查询
DELETE /todos/{id}   # 删除
```

**✅ 验收：** 用浏览器或 curl 能调通所有接口

**📝 提交：** `feat: todo api with fastapi`

---

## Day 16

**🎯 目标：** FastAPI 进阶——Pydantic 和请求体

**📚 理论（25 min）：**
- [Pydantic](https://docs.pydantic.dev/latest/) — BaseModel
- Request Body、Query Parameters、Path Parameters 的区别
- 自动生成 Swagger 文档（`/docs`）

**💻 实操（90 min）：**
- 用 Pydantic 定义请求和响应模型
- 给 Todo API 加数据校验（标题不能为空、状态只能是 pending/done）
- 访问 `/docs` 看自动生成的接口文档

**✅ 验收：** 数据校验生效，Swagger 文档可见

**📝 提交：** `feat: pydantic validation and swagger docs`

---

## Day 17

**🎯 目标：** FastAPI 实战——完整的 Todo API 项目

**📚 理论（25 min）：**
- HTTP 状态码：200, 201, 400, 404, 500
- `HTTPException`
- 中间件的概念（middleware）

**💻 实操（90 min）：**
- 完善 Todo API：
  - 错误处理（404 返回有意义的信息）
  - 状态筛选（`GET /todos?status=pending`）
  - 请求日志中间件

**✅ 验收：** API 功能完整，错误处理规范

**📝 提交：** `feat: complete todo api`

---

## Day 18

**🎯 目标：** 数据库入门——SQLite

**📚 理论（25 min）：**
- SQL 基础：`CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- SQLite 的特点（不需要安装服务端，一个文件就是数据库）
- `sqlite3` 模块

**💻 实操（90 min）：**
- 把 Todo 的存储从 JSON 文件改成 SQLite
- 写 SQL 建表语句
- 用 Python 的 `sqlite3` 执行 CRUD

**✅ 验收：** 所有数据存在 SQLite，API 读写正常

**📝 提交：** `feat: sqlite storage for todo api`

---

## Day 19

**🎯 目标：** 数据库进阶——SQLAlchemy ORM

**📚 理论（25 min）：**
- 什么是 ORM（不用写 SQL，用 Python 对象操作数据库）
- SQLAlchemy 基本用法
- Model 定义 → 自动建表

**💻 实操（90 min）：**
- 用 SQLAlchemy 替换裸 SQL
- 定义 `TodoModel`
- 用 session 做 CRUD

**✅ 验收：** CRUD 功能不变，代码更简洁

**📝 提交：** `refactor: use sqlalchemy orm`

---

## Day 20

**🎯 目标：** Docker 入门

**📚 理论（25 min）：**
- [Docker 官方文档](https://docs.docker.com/get-started/)
- 镜像（Image）vs 容器（Container）
- Dockerfile 是什么
- `docker build` / `docker run`
- 为什么用 Docker？"我电脑上能跑，你电脑上也能跑"

**💻 实操（90 min）：**
- 安装 Docker Desktop
- 写 `Dockerfile`：

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**✅ 验收：** `docker run` 后能访问 API

**📝 提交：** `feat: dockerize todo api`

---

## Day 21

**🎯 目标：** Docker Compose——多服务编排

**📚 理论（25 min）：**
- `docker-compose.yml`
- 服务（service）、网络（network）、卷（volume）
- FastAPI + 数据库两个服务怎么通信

**💻 实操（90 min）：**
- 写 `docker-compose.yml`：FastAPI + PostgreSQL
- `depends_on` 控制启动顺序
- 数据库数据用 volume 持久化

**✅ 验收：** `docker compose up` 一键启动所有服务

**📝 提交：** `feat: docker compose with postgresql`

---

## Day 22

**🎯 目标：** Git 进阶——团队协作必备

**📚 理论（25 min）：**
- branch、merge、rebase
- Pull Request 流程
- `.gitignore` 的正确写法
- `git stash`、`git cherry-pick`、`git log --oneline`

**💻 实操（90 min）：**
- 在 Todo API 仓库里：
  - 创建 feature 分支
  - 开发 → commit → push
  - 创建 PR（自己合并）
  - 写一份像样的 PR description

**✅ 验收：** 熟悉分支操作，知道 PR 流程

**📝 提交：** —（练习用 PR）

---

## Day 23

**🎯 目标：** 代码质量工具——让代码像大厂出品

**📚 理论（25 min）：**
- [ruff](https://docs.astral.sh/ruff/) — Python linter + formatter（极快）
- [mypy](https://mypy.readthedocs.io/) — 静态类型检查
- [pre-commit](https://pre-commit.com/) — 提交前自动检查

**💻 实操（90 min）：**
- 给 Todo API 配置：
  - `ruff`（代码风格检查 + 自动格式化）
  - `mypy`（类型检查）
  - `.pre-commit-config.yaml`
- 修复所有 lint 错误

**✅ 验收：** `ruff check` 和 `mypy` 全部通过，`pre-commit` 自动运行

**📝 提交：** `chore: add linting and type checking`

---

## Day 24

**🎯 目标：** 环境变量和配置管理

**📚 理论（25 min）：**
- 12-Factor App 的 Config 原则
- `python-dotenv` 和 `.env` 文件
- [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- 敏感信息（API Key、数据库密码）绝不提交到 Git

**💻 实操（90 min）：**
- 给 Todo API 加配置管理
- 用 `.env` 存数据库连接、端口号
- 用 `pydantic-settings` 加载配置
- `.gitignore` 确保 `.env` 不会提交

**✅ 验收：** 改 `.env` 就能切换配置，不需要改代码

**📝 提交：** `feat: configuration management`

---

## Day 25

**🎯 目标：** Python 工程大复习（上）

**💻 实操（90 min）：**
- 从零创建 `notes-api`：FastAPI + SQLAlchemy + pytest + Docker + pre-commit
- 今天只写架构和模型层
- 不抄代码，自己写

**📝 提交：** `feat: notes-api scaffold`

---

## Day 26

**🎯 目标：** Python 工程大复习（下）

**💻 实操（90 min）：**
- 完成 `notes-api` 所有功能
- 写测试
- 写 Dockerfile

**✅ 验收：** 完整可运行的项目，测试全过

**📝 提交：** `feat: complete notes-api`

---

## Day 27

**🎯 目标：** 阶段复盘

**💻 实操（90 min）：**
- 回顾 Day 1-26 所有项目
- 整理 GitHub 仓库（README、目录结构）
- 写阶段总结：哪些概念理解了，哪些还模糊
- 更新简历草稿中的"技术栈"部分

**📝 提交：** `docs: phase 1 retrospective`

---

## Day 28

**🎯 目标：** 缓冲日

> 补进度 / 休息 / 或者提前进入下一阶段。

---

# 第二阶段：AI API 开发（Day 29-42）

> 目标：能熟练调用 OpenAI/DeepSeek API，理解 token、streaming、error handling。

---

## Day 29

**🎯 目标：** 第一次 API 调用

**📚 理论（25 min）：**
- [OpenAI API 文档](https://platform.openai.com/docs/overview) — Quickstart
- API Key 是什么，怎么获取
- Chat Completions endpoint
- Message 的结构：`system`, `user`, `assistant`
- 什么是 token（不是"字数"，是"词元"）

**💻 实操（90 min）：**
```python
# 第一个 AI 调用
from openai import OpenAI

client = OpenAI(api_key="...")  # 从 .env 读取！
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "你是一个有用的助手"},
        {"role": "user", "content": "你好，介绍一下自己"}
    ]
)
print(response.choices[0].message.content)
```

**✅ 验收：** 调通 API，理解每个参数的含义

**📝 提交：** `feat: first openai api call`

---

## Day 30

**🎯 目标：** 多轮对话——Message 的真正用法

**📚 理论（25 min）：**
- 为什么要把历史 messages 全发回去（LLM 是无状态的）
- System prompt 的作用（设定人设、行为规范）
- Token 是怎么计算的（用 [tiktoken](https://github.com/openai/tiktoken) 数一下）

**💻 实操（90 min）：**
- 写一个终端聊天机器人：
  - 维护 `messages` 列表
  - 每次把用户输入 append 进去
  - 把 AI 回复也 append 进去
  - 下一轮全量发送
- 实现 `/clear` 清空对话
- 显示每轮的 token 用量

**✅ 验收：** 能多轮对话，上下文保持

**📝 提交：** `feat: multi-turn chat bot`

---

## Day 31

**🎯 目标：** Streaming——实时输出

**📚 理论（25 min）：**
- `stream=True` 的原理（SSE）
- chunk 的结构
- 为什么要流式（用户体验：ChatGPT 一个字一个字出来，不是等 10 秒）

**💻 实操（90 min）：**
- 把聊天机器人改成流式输出
- 每个 chunk 到了就 `print(..., end="", flush=True)`
- 感受"打字机效果"

**✅ 验收：** 流式输出流畅

**📝 提交：** `feat: streaming chat`

---

## Day 32

**🎯 目标：** 错误处理——API 调用的健壮性

**📚 理论（25 min）：**
- API 会出的错：Rate Limit、Timeout、Connection Error、Content Filter
- `try/except` 针对不同异常分别处理
- 重试策略：指数退避（exponential backoff）
- [tenacity](https://tenacity.readthedocs.io/) 库

**💻 实操（90 min）：**
- 给聊天机器人加：
  - 超时处理
  - 自动重试（最多 3 次，间隔递增）
  - 限流处理（遇到 rate limit 等一等再试）
  - 友好的错误提示

**✅ 验收：** 断网、超时、限流都不崩

**📝 提交：** `feat: robust error handling`

---

## Day 33

**🎯 目标：** 聊天机器人项目 v1——用 FastAPI 包装

**📚 理论（25 min）：**
- 回顾 FastAPI + async
- 流式响应怎么做：`StreamingResponse`
- 异步调用 OpenAI API

**💻 实操（90 min）：**
```
ai-chat/
├── main.py              # FastAPI app
├── chat_service.py      # OpenAI 调用逻辑
├── models.py            # Pydantic models
├── requirements.txt
└── .env
```

```
POST /chat  {"message": "你好"}  →  流式返回
GET  /history                 →  对话历史
DELETE /history               →  清空历史
```

**✅ 验收：** 用 curl 调通流式接口

**📝 提交：** `feat: ai chat api v1`

---

## Day 34

**🎯 目标：** 接入 DeepSeek API

**📚 理论（25 min）：**
- DeepSeek API 和 OpenAI API 的区别（兼容 OpenAI SDK）
- 不同模型的对比：价格、速度、能力
- 什么时候用 DeepSeek，什么时候用 GPT

**💻 实操（90 min）：**
- 给 AI Chat API 加模型切换：
  - `POST /chat` 增加 `model` 参数
  - 支持 `gpt-4o-mini` 和 `deepseek-chat`
- 对比两个模型的输出差异

**✅ 验收：** 一个接口支持多模型切换

**📝 提交：** `feat: multi-model support`

---

## Day 35

**🎯 目标：** Token 管理和成本控制

**📚 理论（25 min）：**
- 不同模型的 token 价格表
- Context window（上下文窗口）限制
- 怎么估算一次调用的成本
- 长对话超出 context window 怎么办（截断策略）

**💻 实操（90 min）：**
- 给聊天机器人加：
  - Token 计数（每次调用前后显示 token 用量和费用）
  - Context window 管理（超长自动截断最早的对话）
  - 费用汇总

**✅ 验收：** 能看到每轮对话花了多少钱

**📝 提交：** `feat: token management and cost tracking`

---

## Day 36

**🎯 目标：** Function Calling 基础

**📚 理论（25 min）：**
- [OpenAI Function Calling 文档](https://platform.openai.com/docs/guides/function-calling)
- 什么是 tool/function calling
- LLM 不会执行函数，它只是"告诉你要调哪个函数"
- tool definition 的 JSON Schema 格式

**💻 实操（90 min）：**
- 写一个简单的 function calling：
  - 定义 `get_weather(city: str)` 工具
  - LLM 判断用户是否在问天气
  - 如果是，返回 `{"name": "get_weather", "arguments": {"city": "北京"}}`
  - 你拿到这个结果，真的去调用函数
  - 把结果返回给 LLM 生成最终回复

**✅ 验收：** 理解 LLM → tool call → execute → LLM 的完整流程

**📝 提交：** `feat: function calling basics`

---

## Day 37

**🎯 目标：** Function Calling 实战——多工具

**📚 理论（25 min）：**
- 多个 tool 怎么定义
- LLM 怎么选择调哪个
- parallel tool calls（一次调多个工具）

**💻 实操（90 min）：**
- 实现 3 个工具：
  - `get_weather(city)` — 返回天气（mock 数据）
  - `get_time(city)` — 返回当地时间
  - `calculate(expression)` — 数学计算
- LLM 自动选择正确的工具

**✅ 验收：** "北京天气怎么样"→调 get_weather，"1+2*3 等于多少"→调 calculate

**📝 提交：** `feat: multi-tool function calling`

---

## Day 38

**🎯 目标：** AI 项目实战——AI 总结工具

**📚 理论（25 min）：**
- Prompt Engineering 基础：
  - 明确角色
  - 指定输出格式
  - 提供示例（few-shot）
  - 分步骤思考（CoT）

**💻 实操（90 min）：**
```
ai-summarizer/
├── main.py
├── summarizer.py
└── .env
```
- 输入一段长文本 → AI 生成 3 句话总结
- 支持多种风格：简洁 / 详细 / 要点列表
- 调 temperature 看输出差异

**✅ 验收：** 能对不同文本生成合理总结

**📝 提交：** `feat: ai text summarizer`

---

## Day 39

**🎯 目标：** AI 翻译工具 + Prompt Engineering 练习

**📚 理论（25 min）：**
- system prompt 如何影响翻译质量
- temperature 的作用（0 = 确定性强，1+ = 创造性高）
- 什么时候用低 temperature（翻译、分类），什么时候用高（创意写作）

**💻 实操（90 min）：**
- 实现一个翻译工具：
  - 中→英、英→中、自动检测
  - 保持格式（markdown 翻译后仍然是 markdown）
  - 专业术语保留（用 glossary）

**✅ 验收：** 翻译质量可接受，格式保持

**📝 提交：** `feat: ai translator`

---

## Day 40

**🎯 目标：** 结构化输出——让 LLM 返回 JSON

**📚 理论（25 min）：**
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
- `response_format={"type": "json_object"}`
- 用 Pydantic 定义输出 schema
- JSON Mode vs Function Calling 的区别

**💻 实操（90 min）：**
- 实现一个邮件解析工具：
  - 输入：邮件正文
  - 输出：`{"sender": "...", "subject": "...", "action_items": [...], "sentiment": "positive/neutral/negative"}`
- 用 Pydantic 定义输出格式

**✅ 验收：** 输出严格符合定义的格式

**📝 提交：** `feat: structured output with json mode`

---

## Day 41

**🎯 目标：** AI Chat 项目升级——加对话记录存储

**💻 实操（90 min）：**
- 给 AI Chat API 加 SQLite 存储：
  - 每个会话（session）存下来
  - 历史消息持久化
  - 列出所有会话
  - 恢复历史会话

**✅ 验收：** 对话记录持久化，可选会话

**📝 提交：** `feat: chat history persistence`

---

## Day 42

**🎯 目标：** 阶段复盘 + 缓冲

**💻 实操（90 min）：**
- 回顾 AI API 阶段所有项目
- 整理 GitHub
- 写阶段总结笔记

**📝 提交：** `docs: phase 2 retrospective`

---

# 第三阶段：LangChain 核心（Day 43-49）

> 目标：理解 LangChain 解决了什么问题，只用核心模块。
>
> ⚠️ 只学 1 周，不深入。实际工作中大多数场景用 OpenAI SDK 就够了。

---

## Day 43

**🎯 目标：** LangChain 是什么，为什么有它

**📚 理论（25 min）：**
- [LangChain 官方文档](https://python.langchain.com/docs/get_started/introduction)
- LangChain 想解决的问题：把 LLM 调用组织成可复用的组件
- 核心抽象：PromptTemplate → Model → OutputParser
- LangChain 的争议（过度抽象、版本不稳定）

**💻 实操（90 min）：**
- 用 LangChain 重写 AI Chat：
  ```python
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser
  ```
- 对比原生 OpenAI SDK 和 LangChain 的代码量

**✅ 验收：** 理解 LangChain 的抽象层次

**📝 提交：** `feat: langchain hello world`

---

## Day 44

**🎯 目标：** PromptTemplate 和 OutputParser

**📚 理论（25 min）：**
- `ChatPromptTemplate` — 系统提示 + 用户输入模板
- `MessagesPlaceholder` — 放历史对话
- `StrOutputParser`、`JsonOutputParser`、`PydanticOutputParser`
- Few-shot prompt template

**💻 实操（90 min）：**
- 把 AI 总结工具改成 LangChain 版本
- 用 `PydanticOutputParser` 强制输出 JSON
- 用 few-shot templates 提升质量

**✅ 验收：** 输出格式稳定

**📝 提交：** `feat: langchain prompts and parsers`

---

## Day 45

**🎯 目标：** Chain 和 LCEL

**📚 理论（25 min）：**
- LCEL（LangChain Expression Language）：`prompt | model | parser`
- `RunnablePassthrough`、`RunnableLambda`
- Chain 的组合：SequentialChain、RouterChain

**💻 实操（90 min）：**
- 用 LCEL 搭建一个分析管道：
  ```
  输入文本 → 提取关键词 → 用关键词搜索总结 → 生成摘要
  ```
- 每个步骤都是独立的 Runnable

**✅ 验收：** 理解 `|` 管道的含义

**📝 提交：** `feat: lcel pipeline`

---

## Day 46

**🎯 目标：** Memory——对话记忆管理

**📚 理论（25 min）：**
- `ConversationBufferMemory`
- `ConversationSummaryMemory`（用 LLM 压缩历史）
- Memory 的本质：就是管理一个 messages 列表

**💻 实操（90 min）：**
- 用 LangChain Memory 重写聊天机器人
- 对比 Buffer vs Summary 的效果和 token 消耗

**✅ 验收：** 理解各种 Memory 策略的适用场景

**📝 提交：** `feat: langchain memory`

---

## Day 47

**🎯 目标：** LangChain 的 Tool 和 Agent（预览）

**📚 理论（25 min）：**
- `@tool` 装饰器
- `AgentExecutor` 的基本结构
- 感受 LangChain Agent 和原生 Function Calling 的区别

**💻 实操（90 min）：**
- 用 LangChain Agent 实现一个带工具的助手
- 对比 Day 37 的原生实现

**✅ 验收：** 理解 LangChain Agent 的优缺点

**📝 提交：** `feat: langchain agent preview`

---

## Day 48

**🎯 目标：** LangChain 小结——什么时候用，什么时候不用

**💻 实操（90 min）：**
- 写一篇"LangChain 利弊分析"笔记
- 把 AI Chat 项目同时保留两个版本：原生 SDK + LangChain
- 决定后续项目用什么（建议：RAG 用 LangChain，Agent 尽量原生）

**✅ 验收：** 能清楚地解释选择理由

**📝 提交：** `docs: langchain evaluation`

---

## Day 49

**🎯 目标：** 缓冲日

---

# 第四阶段：RAG 深入（Day 50-77）

> 目标：能独立设计和实现一个生产级 RAG 系统。
>
> RAG 是 LLM 应用最核心的场景，面试必问。

---

## Day 50

**🎯 目标：** 什么是 Embedding

**📚 理论（25 min）：**
- [OpenAI Embeddings 文档](https://platform.openai.com/docs/guides/embeddings)
- Embedding 的本质：把文字变成向量（一串数字）
- 相似的文字 → 相似的向量（余弦相似度）
- 为什么需要 Embedding？（计算机不能理解文字，只能算向量）

**💻 实操（90 min）：**
- 调用 `text-embedding-3-small` 把几段文字向量化
- 计算余弦相似度
- 验证："猫喜欢吃鱼" 和 "猫咪爱吃海鲜" 相似度 > "猫喜欢吃鱼" 和 "今天天气很好"

**✅ 验收：** 直观理解 embedding 的原理

**📝 提交：** `feat: embedding basics`

---

## Day 51

**🎯 目标：** 向量数据库——FAISS

**📚 理论（25 min）：**
- [FAISS](https://github.com/facebookresearch/faiss) — Facebook 的向量搜索库
- 向量索引（index）：把所有向量组织起来，快速搜索
- `add()` / `search()` 的基本流程
- 为什么不用数据库的全文搜索而用向量搜索

**💻 实操（90 min）：**
- 创建 100 条"文档"（可以是中文短句）
- 用 embedding 模型向量化
- 存入 FAISS index
- 搜索："如何学习 Python" → 返回最相关的 3 条

**✅ 验收：** 搜索结果和问题相关

**📝 提交：** `feat: faiss vector search`

---

## Day 52

**🎯 目标：** Chroma——更友好的向量数据库

**📚 理论（25 min）：**
- [Chroma](https://docs.trychroma.com/) — 开源的向量数据库
- vs FAISS：Chroma 自带持久化、metadata 过滤、更方便的 API
- 什么时候用 FAISS（大规模、纯内存）、什么时候用 Chroma（中小规模、需要持久化）

**💻 实操（90 min）：**
- 用 Chroma 重写 Day 51 的例子
- 加入 metadata（每条文档的标题、日期、类别）
- 用 metadata 过滤：只看"Python 教程"相关的文档里搜索

**✅ 验收：** 能按 metadata 筛选 + 向量搜索

**📝 提交：** `feat: chroma vector store`

---

## Day 53

**🎯 目标：** Chunking（文档切分）——RAG 最难的部分

**📚 理论（25 min）：**
- 为什么要切分？（一篇 1 万字的文章不能整个塞进 context window）
- Chunk size 和 overlap 的权衡：
  - 太小 → 丢失上下文
  - 太大 → 检索不精确
  - overlap → 不让一个意思被切在两段里
- 不同的切分策略：按字符、按句子、按段落、递归分割

**💻 实操（90 min）：**
- 拿一篇长文章，用不同策略切分：
  - `CharacterTextSplitter`（chunk_size=500, overlap=50）
  - `RecursiveCharacterTextSplitter`
  - 自己写一个"按段落切分"
- 对比三种切分结果

**✅ 验收：** 理解不同切分策略的效果差异

**📝 提交：** `feat: document chunking strategies`

---

## Day 54

**🎯 目标：** 第一个 RAG——PDF 问答

**📚 理论（25 min）：**
- RAG 的完整流程：Load → Split → Embed → Store → Retrieve → Generate
- [LangChain Document Loaders](https://python.langchain.com/docs/integrations/document_loaders/)
- PyPDFLoader、TextLoader

**💻 实操（90 min）：**
- 找一个 PDF（教程/论文），实现：
  1. 加载 PDF
  2. 切分成 chunks
  3. 向量化存入 Chroma
  4. 用户提问 → 检索相关 chunks → 喂给 LLM 生成答案
- 输出答案时标注来源（哪个 chunk）

**✅ 验收：** 问 PDF 里的问题，能得到正确答案（大概对就行）

**📝 提交：** `feat: rag pdf qa v1`

---

## Day 55

**🎯 目标：** RAG 质量分析——为什么有时候不准

**💻 实操（90 min）：**
- 给 Day 54 的 RAG 做测试：
  - 问 10 个 PDF 里的问题
  - 记录哪些答对了、哪些答错了
  - 分析错误原因：
    - chunk 没找到？（检索问题）
    - chunk 找到了但答案不对？（生成问题）
    - chunk 切坏了？（chunking 问题）
- 写一份"RAG 调优笔记"

**✅ 验收：** 能诊断 RAG 的常见问题

**📝 提交：** `docs: rag quality analysis`

---

## Day 56

**🎯 目标：** 语义切分——比固定大小更聪明

**📚 理论（25 min）：**
- Semantic chunking：用 embedding 判断"话题是否变了"，变了就断开
- 和固定大小切分的对比
- `langchain_experimental.text_splitter.SemanticChunker`

**💻 实操（90 min）：**
- 用 semantic chunker 重新切分 PDF
- 对比固定大小 vs 语义切分的检索质量
- 用同一个问题集测试，看哪种切分更准确

**✅ 验收：** 能解释语义切分什么时候效果好

**📝 提交：** `feat: semantic chunking`

---

## Day 57

**🎯 目标：** 检索策略——不止一种

**📚 理论（25 min）：**
- Dense retrieval（向量搜索）vs Sparse retrieval（BM25 关键词搜索）
- 各自的优缺点
- 混合检索（Hybrid Search）= Dense + Sparse
- Reciprocal Rank Fusion（RRF）合并结果

**💻 实操（90 min）：**
- 实现 BM25 关键词检索（用 `rank_bm25` 库）
- 实现混合检索：向量搜索结果 + BM25 结果 → RRF 合并
- 对比纯向量搜索 vs 混合搜索的效果

**✅ 验收：** 混合搜索在某些问题上明显优于纯向量搜索

**📝 提交：** `feat: hybrid search with rrf`

---

## Day 58

**🎯 目标：** Re-ranking——给检索结果再加一道过滤

**📚 理论（25 min）：**
- 为什么需要 re-ranking？（检索了 20 个 chunks，真正有用的可能只有 3 个）
- Cross-encoder vs Bi-encoder
- [Cohere Rerank](https://docs.cohere.com/docs/rerank-2) / [BGE Reranker](https://huggingface.co/BAAI/bge-reranker-v2-m3)

**💻 实操（90 min）：**
- 检索 top-20 chunks → reranker 排序 → 取 top-5 → 喂给 LLM
- 用本地 BGE Reranker（免费，不需要 API key）
- 对比有无 reranking 的答案质量

**✅ 验收：** reranking 后答案质量有提升

**📝 提交：** `feat: reranking with bge`

---

## Day 59

**🎯 目标：** RAG 评估——RAGAS

**📚 理论（25 min）：**
- [RAGAS](https://docs.ragas.io/) — RAG 系统的评估框架
- 四个核心指标：
  - Faithfulness（答案是否忠于原文）
  - Answer Relevancy（答案是否相关）
  - Context Recall（检索是否找全了）
  - Context Precision（检索是否找对了）

**💻 实操（90 min）：**
- 准备测试集（问题 + 标准答案）
- 用 RAGAS 评估你的 RAG 系统
- 根据分数定位问题

**✅ 验收：** 能量化评估 RAG 质量

**📝 提交：** `feat: rag evaluation with ragas`

---

## Day 60

**🎯 目标：** 项目实战——RAG 知识库 v1（后端）

**💻 实操（90 min）：**
```
rag-knowledge-base/
├── main.py                 # FastAPI
├── loader.py               # 文档加载
├── splitter.py             # 文档切分
├── vector_store.py         # Chroma 操作
├── retriever.py            # 检索逻辑
├── generator.py            # LLM 生成
├── models.py               # Pydantic
└── .env
```

```
POST /documents/upload     # 上传文档
POST /query                # 提问
GET  /documents            # 列出已上传文档
DELETE /documents/{id}     # 删除文档
```

**✅ 验收：** API 调通，能上传文档并提问

**📝 提交：** `feat: rag knowledge base api v1`

---

## Day 61

**🎯 目标：** 项目实战——RAG 知识库 v2（优化）

**💻 实操（90 min）：**
- 加入混合检索 + reranking
- 答案带引用来源
- 错误处理完善

**✅ 验收：** 答案质量明显提升

**📝 提交：** `feat: rag knowledge base v2 with hybrid search`

---

## Day 62

**🎯 目标：** RAG 项目——支持多种文档格式

**💻 实操（90 min）：**
- 扩展文档支持：PDF、TXT、Markdown、网页 URL
- 每种格式用对应的 loader
- 统一处理管道

**✅ 验收：** 上传任意支持的格式都能正常工作

**📝 提交：** `feat: multi-format document support`

---

## Day 63

**🎯 目标：** RAG 阶段中期复盘

**💻 实操（90 min）：**
- 整理 RAG 知识库项目代码
- 写 README（架构图、如何使用、技术栈）
- 写 RAG 学习总结笔记

**📝 提交：** `docs: rag mid-phase review`

---

## Day 64

**🎯 目标：** 多模态 RAG——图片也能搜

**📚 理论（25 min）：**
- 多模态 embedding（CLIP 等）
- 图片 + 文字混合检索
- 场景：上传产品说明书（图文混排），问"第 3 页的表格说了什么"

**💻 实操（90 min）：**
- 用支持图片的 PDF loader（`UnstructuredPDFLoader`）
- 图片用多模态 LLM（GPT-4o）生成文字描述
- 文字描述也加入检索

**✅ 验收：** 能从图文混合的文档中找到相关信息

**📝 提交：** `feat: multimodal rag support`

---

## Day 65

**🎯 目标：** 自查询检索（Self-Querying）

**📚 理论（25 min）：**
- 问题："2024 年发布的关于 Python 的文档"
- 需要两个操作：① 向量搜索"Python" ② metadata 过滤"year=2024"
- Self-query retriever：让 LLM 自动拆解查询

**💻 实操（90 min）：**
- 实现 self-querying retriever
- 测试：带条件的自然语言查询能正确解析

**✅ 验收：** LLM 自动生成 metadata filter

**📝 提交：** `feat: self-querying retriever`

---

## Day 66

**🎯 目标：** RAG 高级——Query Transformation

**📚 理论（25 min）：**
- 用户问的问题可能不是最好的检索查询
- Query Rewriting：让 LLM 把用户问题改写成更利于检索的形式
- HyDE（Hypothetical Document Embeddings）：先生成一个"假答案"，用假答案去检索
- Multi-Query：一个用户问题拆成多个检索查询

**💻 实操（90 min）：**
- 实现 Query Rewriting
- 实现 Multi-Query Retrieval
- 对比改写前后的检索结果

**✅ 验收：** 改写后的查询检索质量更好

**📝 提交：** `feat: query transformation`

---

## Day 67

**🎯 目标：** RAG 项目 v3——完整的知识库系统

**💻 实操（90 min）：**
- 整合所有 RAG 技术：
  - 多格式文档上传
  - 语义切分
  - 混合检索 + Reranking
  - Query Transformation
  - 答案带引用
  - 对话历史（contextual RAG）
- 写一个像样的 README（架构图、API 文档）

**✅ 验收：** 一个完整的、可以放简历的 RAG 项目

**📝 提交：** `feat: complete rag knowledge base v3`

---

## Day 68-69

**🎯 目标：** RAG 项目 Docker 化 + 部署

**💻 实操（每天 90 min）：**
- Dockerfile + docker-compose.yml（FastAPI + Chroma）
- 环境变量管理
- 写部署文档

**📝 提交：** `feat: docker deployment` / `docs: deployment guide`

---

## Day 70

**🎯 目标：** RAG 阶段总复习

**💻 实操（90 min）：**
- 回顾整个 RAG 阶段
- 理论梳理：画一张 RAG 全景图（从 Load 到 Generate 的所有环节）
- 整理所有可调优的参数（chunk_size, overlap, top_k, temperature, ...）

**📝 提交：** `docs: rag phase retrospective`

---

## Day 71-77

**🎯 目标：** RAG 预留缓冲 + 深入研究周

这一周用来：
- 补 RAG 阶段没做完的内容
- 深入研究某个感兴趣的方向（Graph RAG / Agentic RAG）
- 或者提前进入 Agent 阶段

> 可选方向：Graph RAG（用知识图谱增强 RAG）、Agentic RAG（用 Agent 控制检索流程）

---

# 第五阶段：Agent 开发（Day 78-91）

> 目标：能独立开发基于 Function Calling 的 AI Agent。
>
> 这是你简历上最有分量的部分。

---

## Day 78

**🎯 目标：** Agent 的核心概念

**📚 理论（25 min）：**
- 什么是 Agent？（LLM + 工具 + 决策循环）
- Agent = 大脑（LLM）+ 手（Tools）+ 循环（观察→思考→行动）
- ReAct 模式：Reasoning + Acting
- Agent 和普通 LLM 调用的区别：Agent 会"自己想办法"

**💻 实操（90 min）：**
- 用原生 Function Calling 实现一个最简 Agent 循环：
  ```python
  while not done:
      response = llm.chat(messages, tools)
      if response has tool_calls:
          for tool_call in tool_calls:
              result = execute(tool_call)
              messages.append(result)
      else:
          done = True
  ```
- 给 Agent 两个工具：计算器 + 搜索（mock）

**✅ 验收：** Agent 能自己决定什么时候调用工具、什么时候结束

**📝 提交：** `feat: minimal agent loop`

---

## Day 79

**🎯 目标：** Agent 的工具设计

**📚 理论（25 min）：**
- 好的 Tool 设计原则：
  - 单一职责（一个 tool 只做一件事）
  - 清晰的 description（LLM 靠描述来选工具）
  - 合理的参数（参数名要和 description 呼应）
- 用 Pydantic 定义 tool schema

**💻 实操（90 min）：**
- 设计 5 个工具：
  - `search_web(query)` — 搜索互联网
  - `get_stock_price(symbol)` — 查询股价
  - `get_weather(city)` — 查询天气
  - `send_email(to, subject, body)` — 发送邮件（mock）
  - `create_reminder(text, time)` — 创建提醒
- 每个工具有清晰的 docstring

**✅ 验收：** LLM 能根据用户意图正确选择工具

**📝 提交：** `feat: agent tools design`

---

## Day 80

**🎯 目标：** Agent 记忆——短期和长期

**📚 理论（25 min）：**
- 短期记忆：messages 列表（对话历史）
- 长期记忆：跨会话的信息（用户偏好、历史决策）
- Agent 需要在 messages 里看到"自己的工具调用历史"

**💻 实操（90 min）：**
- 给 Agent 加：
  - 对话历史管理
  - 工具调用历史（Agent 能看到自己刚才做了什么）
  - 用户偏好存储（"记住，我不喜欢被称呼为'您'"）

**✅ 验收：** Agent 能记住之前的对话和用户偏好

**📝 提交：** `feat: agent memory`

---

## Day 81

**🎯 目标：** Agent 安全——你不能把数据库密码给 LLM

**📚 理论（25 min）：**
- Agent 的常见安全问题：
  - Prompt Injection（用户说"忽略之前的所有指令"）
  - Tool 权限过大（一个"删除数据库"的 tool 不应该存在）
  - 信息泄露（tool 返回了不该返回的数据）
- 防御方案：输入过滤、输出过滤、权限最小化

**💻 实操（90 min）：**
- 给 Agent 加安全层：
  - 敏感 tool（如 send_email）需要用户确认
  - 输入过滤（检测"ignore previous instructions"）
  - Tool 返回结果过滤（检查是否包含敏感信息）

**✅ 验收：** 基本的安全防护机制到位

**📝 提交：** `feat: agent safety guardrails`

---

## Day 82

**🎯 目标：** Agent 项目——AI 旅行助手 v1

**💻 实操（90 min）：**

```
travel-agent/
├── main.py           # FastAPI + Agent 循环
├── agent.py          # Agent 核心逻辑
├── tools/
│   ├── weather.py    # 天气工具
│   ├── flight.py     # 机票搜索
│   ├── hotel.py      # 酒店搜索
│   ├── map.py        # 地图/距离
│   └── translator.py # 翻译
├── models.py
└── .env
```

- 实现核心 Agent 循环
- 实现天气 + 翻译工具（真实 API）
- 机票和酒店用 mock 数据

**✅ 验收：** 能完成简单的旅行咨询（"周末去杭州玩，天气怎么样"）

**📝 提交：** `feat: travel agent v1`

---

## Day 83

**🎯 目标：** 旅行助手 v2——加入规划能力

**📚 理论（25 min）：**
- Planning：旅行 Agent 不能只是回答单个问题
- 它需要：理解整体需求 → 拆解子任务 → 逐步执行 → 汇总结果
- Plan-and-Execute 模式

**💻 实操（90 min）：**
- 给 Agent 加 Planning：
  - 用户说"帮我规划一个 3 天北京游"
  - Agent 先输出计划：
    1. 查天气
    2. 搜景点
    3. 搜酒店
    4. 算交通
    5. 汇总行程
  - 然后逐步执行
  - 最后生成完整行程

**✅ 验收：** 能生成一个像样的旅行计划

**📝 提交：** `feat: travel agent with planning`

---

## Day 84

**🎯 目标：** 旅行助手 v3——错误恢复

**💻 实操（90 min）：**
- Agent 执行中可能出错：
  - API 超时
  - 搜索没结果
  - 工具返回异常
- Agent 要知道"出错了怎么办"：
  - 重试
  - 换一个工具
  - 告诉用户

**✅ 验收：** Agent 遇到错误不崩溃，能自行处理或告知用户

**📝 提交：** `feat: agent error recovery`

---

## Day 85

**🎯 目标：** 旅行助手 v4——完整的 API 项目

**💻 实操（90 min）：**
- FastAPI 包装
- 流式输出（用户能看到 Agent "正在搜索天气..."）
- 对话记录存储
- Docker 化

**✅ 验收：** 完整可部署的 Agent 项目

**📝 提交：** `feat: travel agent complete`

---

## Day 86

**🎯 目标：** LangGraph 入门——为什么需要图结构

**📚 理论（25 min）：**
- [LangGraph 官方文档](https://langchain-ai.github.io/langgraph/)
- 什么时候 Agent 循环不够用？
  - 复杂的多步骤流程
  - 条件分支
  - 人机协作（等人批准）
- Node、Edge、State 的概念

**💻 实操（90 min）：**
- 用 LangGraph 实现一个简单流程：
  ```
  开始 → 分析问题类型 → [简单问题 → 直接回答]
                        → [复杂问题 → 拆解 → 逐步回答]
  ```
- 可视化这个图

**✅ 验收：** 理解图结构的优势

**📝 提交：** `feat: langgraph hello world`

---

## Day 87

**🎯 目标：** LangGraph——多 Agent 协作

**📚 理论（25 min）：**
- 多 Agent 模式：
  - 流水线：A → B → C
  - 辩论：A 和 B 各自回答，C 评判
  - 分工：Planner → Searcher → Writer → Reviewer
- Agent 间的通信：通过 State 传递

**💻 实操（90 min）：**
- 实现一个文章写作工作流：
  ```
  Planner（定大纲）
    ↓
  Researcher（搜资料）
    ↓
  Writer（写初稿）
    ↓
  Reviewer（审校）
    ↓
  最终输出
  ```

**✅ 验收：** 三个 Agent 协作产出比单个更好的结果

**📝 提交：** `feat: multi-agent writing workflow`

---

## Day 88

**🎯 目标：** LangGraph——Human-in-the-loop

**📚 理论（25 min）：**
- 有些操作需要人批准（发送邮件、付款、删除数据）
- `interrupt()` 暂停执行，等待用户确认
- 确认后恢复执行

**💻 实操（90 min）：**
- 给旅行助手加 human-in-the-loop：
  - Agent 规划好行程后，暂停，给用户看
  - 用户确认/修改
  - Agent 继续执行（订票等 mock 操作）

**✅ 验收：** 流程能暂停-确认-恢复

**📝 提交：** `feat: human in the loop`

---

## Day 89

**🎯 目标：** Agent 阶段项目——多 Agent 研究助手

**💻 实操（90 min）：**
```
research-agent/
├── main.py
├── graph.py            # LangGraph workflow
├── agents/
│   ├── planner.py      # 制定研究计划
│   ├── searcher.py     # 搜索信息
│   ├── analyzer.py     # 分析整理
│   └── writer.py       # 生成报告
├── tools/
│   ├── web_search.py
│   ├── pdf_reader.py
│   └── note_taker.py
└── .env
```

**✅ 验收：** 输入一个研究主题 → 多 Agent 协作 → 生成研究报告

**📝 提交：** `feat: multi-agent research assistant`

---

## Day 90

**🎯 目标：** 研究助手 v2——完善和优化

**💻 实操（90 min）：**
- 完善错误处理
- 加入流式输出
- 写 README（架构图 + 使用说明）

**✅ 验收：** 项目完整，文档清晰

**📝 提交：** `feat: research agent complete`

---

## Day 91

**🎯 目标：** Agent 阶段复盘

**💻 实操（90 min）：**
- 整理所有 Agent 项目
- 写 Agent 学习总结：Function Calling → ReAct → Planning → Multi-Agent
- 画一张"Agent 全景图"

**📝 提交：** `docs: agent phase retrospective`

---

# 第六阶段：毕业项目 + 就业准备（Day 92-100）

> 目标：1 个毕业大项目 + 简历打磨 + 面试准备。

---

## Day 92-93

**🎯 目标：** 毕业项目——选题和架构设计

**选题建议（选一个）：**

1. **AI 知识库助手**（最推荐，面试最有得聊）
   - 上传公司文档 → RAG 问答 → Agent 自动整理 → 支持多用户
   - 技术栈：FastAPI + PostgreSQL + Chroma + Docker + LangGraph

2. **AI 自动化工作助手**
   - 自然语言输入 → Agent 自动执行（查邮件、写总结、定日程）
   - 技术栈：FastAPI + Agent + 多工具集成

3. **AI 学习助手**
   - 上传课程资料 → 自动生成笔记 → 出题 → 批改
   - 技术栈：RAG + Agent + 多模态

**先做架构设计，再写代码。不要上来就写。**

---

## Day 94-97

**🎯 目标：** 毕业项目开发

每天 90 分钟专注写代码。目标：
- 完整的 FastAPI 后端
- 数据库存储
- Docker 部署
- 测试覆盖
- 像样的 README（架构图、API 文档、部署方式、使用示例）

---

## Day 98

**🎯 目标：** 简历打磨

**💻 实操（90 min）：**
- 整理所有项目，写成简历项目经历（STAR 法则）
- 每个项目用 3-4 句话描述：做了什么、用了什么技术、解决了什么问题、有什么成果
- 技术栈总结：

```
语言：Python
框架：FastAPI, LangChain, LangGraph
数据库：PostgreSQL, SQLite, Chroma, FAISS
工具：Docker, Git, pytest, uv
AI：OpenAI API, DeepSeek API, Function Calling, RAG, Agent
```

---

## Day 99

**🎯 目标：** 面试准备

**重点准备方向：**

1. **Python 基础八股**（装饰器、生成器、GIL、async、类型系统）
2. **RAG 系统设计**（"设计一个企业知识库问答系统"）
3. **Agent 原理**（"Agent 和普通 LLM 调用有什么区别"）
4. **项目深挖**（"你做的 RAG 系统，chunk size 为什么选 500？"）
5. **代码题**（LeetCode Easy-Medium，用 Python）

**练习方式：对着镜子讲，或者录视频。**

---

## Day 100

**🎯 目标：** 收尾

- 整理 GitHub 主页（pin 最好的 6 个项目）
- 每个项目写清晰的 README
- 写一篇"100 天 AI Agent 学习总结"（中文，放 GitHub README）
- 规划下一步（找实习？继续深入？）

---

# 课外阅读清单

不要一次性读完，用到的时候看：

## 必读

- [Python 官方教程](https://docs.python.org/3/tutorial/)
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [OpenAI API 文档](https://platform.openai.com/docs/)
- [LangChain 文档](https://python.langchain.com/)

## 推荐

- [The Twelve-Factor App](https://12factor.net/) — 理解工程化
- [pytest 文档](https://docs.pytest.org/)
- [Docker Get Started](https://docs.docker.com/get-started/)

## 深入

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/)
- [RAGAS 文档](https://docs.ragas.io/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)

---

# 常见问题

**Q：某一天的任务没做完怎么办？**
A：第二天接着做，不要跳过。每个阶段留了缓冲日就是干这个的。

**Q：考试周怎么办？**
A：暂停学习计划，考完回来。不要焦虑进度——100 天是学习日，不是日历日。

**Q：要不要看视频教程？**
A：可以看，但控制在 30 分钟内。看完必须立刻动手写代码。只看不写 = 白看。

**Q：某个概念理解不了怎么办？**
A：① 再看一遍官方文档 ② 写个小 demo 验证 ③ 如果还不行，记下来，先跳过，过几天回来看。

**Q：要学前端吗？**
A：这 100 天先不学。后端和 AI 才是核心竞争力。前端后面再补。

**Q：能找到工作吗？**
A：认真完成这 100 天，你的 GitHub 会有 5-8 个有质量的项目，技术栈覆盖 AI 应用工程师的核心要求。剩下的就看面试发挥和运气了。

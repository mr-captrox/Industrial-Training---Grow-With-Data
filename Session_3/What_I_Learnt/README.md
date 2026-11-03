# 📘 Session 3: What I Learnt — LangChain, Local LLMs & Agents

## 🎯 Objectives
Explore the **LangChain** ecosystem to transition from raw SDK API calls to a unified, composable architecture. Learn multi-turn conversation memory, local model inference with **Ollama**, and autonomous agent tool-calling patterns.

---

## 🔑 Key Learnings

### 1. LangChain Message Schema Abstraction
- Unified message types:
  - `SystemMessage`: Sets persona, tone, rules, and guardrails.
  - `HumanMessage`: Represents user queries and incoming requests.
  - `AIMessage`: Captures model responses and conversational state.
- Structuring multi-turn conversations by managing chat message lists dynamically.

### 2. Local LLMs with ChatOllama
- Running models locally (e.g. `llama3.2:3b`) using Ollama at `http://127.0.0.1:11434`.
- Decoupling application logic from proprietary cloud APIs for private, offline-first development.

### 3. Tool Calling with `@tool` & Schema Validation
- Defining callable tools using the `@tool` decorator.
- Enforcing strong argument validation using Pydantic `args_schema` (`WeatherInput`).
- Inspecting generated tool schemas for accurate LLM invocation.

### 4. Agent Orchestration (`create_agent`)
- Constructing autonomous agents that intelligently decide when to answer directly versus invoking tools.
- Multi-step execution flow: user query $\rightarrow$ LLM decides tool call $\rightarrow$ tool executes $\rightarrow$ LLM synthesizes final answer.

### 5. Observability with LangSmith
- Configuring `LANGSMITH_TRACING` to log runs, token counts, latency, and full execution graphs.

---

## 📂 Notebooks in this Directory
- [`session3.ipynb`](./session3.ipynb): End-to-end interactive exploration covering LangSmith tracing, ChatOllama, message roles, tool definitions, and agent workflows.

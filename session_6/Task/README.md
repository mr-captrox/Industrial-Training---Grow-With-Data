# Session 6 — Task

**Goal:** Upgrade the Northstar Services Support Assistant (built across Sessions 2–5) to a fully hand-crafted **LangGraph** agent with cross-thread long-term memory.

## What's new in Session 6

| Feature | Description |
|---------|-------------|
| **Custom ReAct loop** | Built with `StateGraph` — no more `create_agent` black-box |
| **`guard_check` node** | Prompt injection detection as a dedicated graph node |
| **`InMemoryStore`** | Cross-thread long-term memory — customer facts persist across sessions |
| **`InMemorySaver`** | Short-term per-thread conversation memory (checkpointer) |
| **LangSmith tracing** | Every node and tool call traced automatically |

## Project evolution

```
Session 2 → Structured triage output
Session 3 → YAML prompts + domain tools
Session 4 → Middleware stack + HITL
Session 5 → RAG (Qdrant vector store)
Session 6 → Custom LangGraph agent + cross-thread memory  ← HERE
```

## Files

| File | Description |
|------|-------------|
| `session6taskcode.ipynb` | Main notebook — run top to bottom |
| `prompt.yml` | Externalized triage & reply system prompts |

## How to run

1. Make sure `.env` has your `GOOGLE_API_KEY` and `LANGSMITH_*` variables.
2. Select the `.venv` kernel in Jupyter.
3. Run all cells in `session6taskcode.ipynb`.
4. Check LangSmith under the `ollama` project to see the traces.

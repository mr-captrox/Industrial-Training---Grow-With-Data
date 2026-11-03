# 📘 Session 4: What I Learnt — Memory, Streaming & Concurrency

## 🎯 Objectives
Master stateful conversational agent architectures using **LangGraph** memory checkpointers, optimize user-perceived responsiveness via token streaming, and understand threading primitives for background execution.

---

## 🔑 Key Learnings

### 1. Conversational Memory with LangGraph Checkpointing
- Overcoming stateless LLM limitations using `InMemorySaver()`.
- Thread-scoped conversation isolation using `{"configurable": {"thread_id": "..."}}`.
- How the checkpointer automatically records turn-by-turn message history, allowing the agent to recall user details (e.g., name, previous questions) across multiple turns without manual list management.

### 2. Streaming vs. Non-Streaming Latency
- Understanding **Time to First Token (TTFT)** vs. total generation time.
- `.invoke()`: Blocks execution synchronously until the full response is generated (high perceived latency).
- `.stream()`: Yields tokens incrementally as they are sampled, delivering immediate visual feedback to end users.

### 3. Concurrency & Background Threads
- Using Python's `threading` module to execute tasks concurrently.
- Running long operations or polling background workers without blocking the main event loop.

---

## 📂 Notebooks & Files in this Directory
- [`session4.ipynb`](./session4.ipynb): Demonstrates stateful memory retention across threads and performs a live latency benchmark comparing `.invoke()` against `.stream()`.
- [`session4.py`](./session4.py): Standalone Python script demonstrating the `InMemorySaver` agent memory checkpointer.
- [`prac4.ipynb`](./prac4.ipynb): Concurrent multithreading demonstration with `threading.Thread`.

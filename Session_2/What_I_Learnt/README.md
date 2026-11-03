# 📘 Session 2: What I Learnt — Prompt Engineering & API Basics

## 🎯 Objectives
Explore the mechanics of interacting directly with modern LLM APIs, mastering prompt structure, and handling real-world operational challenges like API rate limits and authentication errors.

---

## 🔑 Key Learnings

### 1. API Client Initialization & Authentication
- Initializing API client libraries (such as OpenAI and Google GenAI) using environment variables loaded securely via `python-dotenv`.
- Best practices for keeping API keys private and out of version control.

### 2. Prompt Mechanics & System vs. User Roles
- Separating high-level instructions (system prompt) from user inputs to control persona, output style, and safety boundaries.
- Exploring one-shot, few-shot, and role-based prompt engineering techniques.

### 3. Error Handling & Production Robustness
- Understanding HTTP status codes and API exceptions:
  - `429 RateLimitError` / `InsufficientQuota`: Handling quota limits and implementing exponential backoff.
  - `401 AuthenticationError`: Catching missing or malformed API keys early.
- Wrapping API calls with robust `try/except` blocks to prevent silent application crashes.

---

## 📂 Notebooks in this Directory
- [`session2.ipynb`](./session2.ipynb): Interactive demonstration of LLM client initialization, completion requests, and graceful exception handling for API limits.

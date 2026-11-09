# 🌟 Northstar Services — Support Assistant (v3: RAG-Powered Knowledge Grounding)

## 📖 Overview
Welcome to **v3** of the course-long iterative SaaS customer support AI! 
In **Session 5**, we upgraded the Northstar Triage & Support Assistant with **Retrieval-Augmented Generation (RAG)**. 

In earlier sessions, the agent had to rely on either a single hardcoded string or LLM memory to answer policy questions. In **v3**, Northstar's complete corporate policy documentation (cancellations, refund eligibility, SLA uptime credits, dispute rules) is chunked, converted into dense semantic vector embeddings via Google Gemini (`gemini-embedding-2`), and stored in **Qdrant**. The agent dynamically searches this vector knowledge base using the new `company_policy` tool!

---

## ✨ System Evolution
- **Session 2:** Structured output classification & ticket triage (`Triage` schema).
- **Session 3:** Externalized prompt engineering via `prompt.yml` and domain tool calling.
- **Session 4:** Short-term conversational memory with LangGraph's `InMemorySaver`, multi-step workflows, and enterprise middleware (`policy_guard`, retry, call limits, and Human-in-the-Loop gating on refunds).
- **Session 5 (v3 Upgrade):** **RAG Knowledge Grounding** — Integrating vector database semantic search (`company_policy`) alongside tabular customer lookups and transactional refund actions.

---

## 🛠️ The 6 Enterprise Domain Tools
The agent is equipped with the complete 6-tool suite from the system architecture:
1. `lookup_customer(email)`: Query relational database for customer plan, ID, status, and signup date.
2. `list_invoices(customer_id)`: Retrieve customer invoice history to detect duplicate charges.
3. `get_return_policy()`: Baseline legacy policy summary.
4. `company_policy(query)`: **(NEW Session 5 RAG Tool)** Semantically retrieves exact contractual clauses from the corporate policy vector store in Qdrant.
5. `check_refund_status(invoice_id)`: Inspect status and ETA of existing refund tickets.
6. `issue_refund(invoice_id, amount)`: Proposes financial refund execution (strictly intercepted and gated by Human-in-the-Loop approval before money moves).

---

## 📂 Files in this Directory
- [`session5taskcode.ipynb`](./session5taskcode.ipynb) (also available as [`session5ipynbtask.ipynb`](./session5ipynbtask.ipynb)): Complete production notebook with RAG indexing, the 6 domain tools, multi-ticket evaluation, and HITL resumption.
- [`prompt.yml`](./prompt.yml): Production YAML configuration containing the grounded triage and support agent system prompts.
- [`README.md`](./README.md): Architecture documentation, evolution guide, and run instructions.

---

## 🚀 How to Run Locally

1. **Activate the project virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

2. **Verify Environment Variables:**
   Ensure your `.env` at the root contains:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key
   QDRANT_URL=https://your-cluster.cloud.qdrant.io:6333
   QDRANT_API_KEY=your_qdrant_api_key
   LANGSMITH_TRACING=true
   LANGSMITH_PROJECT=ollama
   ```
   *(Note: If no remote Qdrant credentials are provided, the notebook automatically falls back to local in-memory Qdrant storage so you can run offline seamlessly!)*

3. **Run the Notebook:**
   Open `session5taskcode.ipynb` (or `session5ipynbtask.ipynb`) in VS Code or Jupyter and execute the cells sequentially!


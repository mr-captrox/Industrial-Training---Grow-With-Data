# 🌟 Northstar Services — Support Assistant (v2)

## 📖 Overview
Welcome to **v2** of the course-long iterative SaaS customer support AI! 
In Session 4, we upgraded our assistant with the superpower of **Tool Calling (Function Calling)**. Instead of just answering text-based questions, the Northstar Triage Assistant can now actively pull real customer data, check invoices, review refund status, and even execute refunds using tools!

## ✨ Features (v2)
1. **Tool Calling Integration:** The LLM can now intelligently choose when to call specific backend Python functions based on the customer's request.
2. **Context-Aware Interactions:**
   * `lookup_customer`: Finds user accounts securely.
   * `list_invoices`: Checks if the customer was billed twice.
   * `check_refund_status`: Gives real-time updates on active refunds.
   * `get_return_policy`: Grounds the assistant in factual, up-to-date company policies.
   * `issue_refund`: Proposes an actionable refund request (requires human approval before execution).
3. **Fact Grounding & Zero Hallucinations:** The LLM is strictly instructed never to invent account details or transactions. Every claim is rooted in a tool result.
4. **Automated Triage System:** Still performs world-class classification (category, urgency, sentiment, escalation flags).

## 🚀 How to Run Locally

1. **Activate the global environment:**
   ```bash
   # From the root of the repository
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

2. **Navigate to this folder & install dependencies:**
   ```bash
   cd Session_4/Task
   pip install pydantic pyyaml python-dotenv langchain google-generativeai langchain-google-genai
   ```

3. **Configure your API Key:**
   - Ensure your `.env` file at the root has your actual Gemini API key.

4. **Run the Notebook:** Open `session4taskcode.ipynb` and run the cells sequentially to watch the agent use tools in real time!

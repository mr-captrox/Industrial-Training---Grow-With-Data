# 🌟 Northstar Services — Support Assistant (v0)

## 📖 Overview
This project is **v0** of a course-long, iterative SaaS customer support AI. 
For this version, we built a fully functional backend logic system that takes incoming customer support messages, triages them using strict Pydantic schemas, and drafts an initial empathetic reply.

## ✨ Features (v0)
1. **Automated Triage System:** Evaluates customer messages to extract:
   * `Category` (billing, technical, account, general)
   * `Urgency` (low, medium, high)
   * `Sentiment` (positive, neutral, negative)
   * `needs_human` (Boolean escalation flag)
2. **Drafting Agent:** Generates a concise, 2-3 sentence initial response engineered to avoid hallucinations (e.g., promising refunds).
3. **Structured Outputs:** Uses Pydantic and the Gemini API to guarantee the LLM returns pure, parsable data.
4. **Separation of Concerns:** System instructions are maintained in a cleanly formatted `prompt.yml` file outside the main logic.

## 🚀 How to Run Locally

1. **Clone the repository and activate the global environment:**
   ```bash
   # From the root of the repository
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

2. **Navigate to this folder & install dependencies:**
   ```bash
   cd Session_2/Task
   pip install pydantic pyyaml python-dotenv google-generativeai
   ```

3. **Configure your API Key:**
   - Rename `.env.example` to `.env`
   - Add your actual Gemini API key inside.

4. **Run the Notebook:** Open `session2taskcode.ipynb` and run the cells sequentially!

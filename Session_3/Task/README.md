# 🌟 Northstar Services — Support Assistant (v1)

## 📖 Overview
This project is **v1** of a course-long, iterative SaaS customer support AI. 
For this version, we leveled up our system by integrating **LangChain**. It takes incoming customer support messages, triages them using strict Pydantic schemas, and drafts an initial empathetic reply, all powered by LangChain's structured chat models.

## ✨ Features (v1)
1. **LangChain Integration:** Modernized our LLM interactions by using LangChain's `init_chat_model` for modular and scalable AI operations.
2. **Automated Triage System:** Evaluates customer messages to extract:
   * `Category` (billing, technical, account, general)
   * `Urgency` (low, medium, high)
   * `Sentiment` (positive, neutral, negative)
   * `needs_human` (Boolean escalation flag)
   * `Summary` (One-line summary of what the customer wants)
3. **Drafting Agent:** Generates a concise initial response engineered to avoid hallucinations.
4. **Structured Outputs:** Uses Pydantic to guarantee the LLM returns pure, parsable data for downstream systems.
5. **Separation of Concerns:** System instructions are maintained in a cleanly formatted `prompt.yml` file outside the main logic.

## 🚀 How to Run Locally

1. **Clone the repository and activate the global environment:**
   ```bash
   # From the root of the repository
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

2. **Navigate to this folder & install dependencies:**
   ```bash
   cd Session_3/Task
   pip install pydantic pyyaml python-dotenv langchain google-generativeai langchain-google-genai
   ```

3. **Configure your API Key:**
   - Create a `.env` file (if you haven't already at the root) or ensure your `google_genai` keys are accessible.
   - Add your actual Gemini API key inside.

4. **Run the Notebook:** Open `session3taskcode.ipynb` and run the cells sequentially!

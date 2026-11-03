"""Session 4: Stateful Agent Memory Demonstration.

Demonstrates conversational memory using LangGraph's InMemorySaver checkpointer
with an Ollama-backed chat agent. Context is retained across multiple turns
belonging to the same thread ID.
"""

from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver  
from langchain_ollama import ChatOllama


def get_user_info() -> str:
    """Look up information about the current user."""
    return "No user profile on file."


def main() -> None:
    # Load environment variables
    load_dotenv()

    # Initialize local LLM and stateful agent
    llm = ChatOllama(model="llama3.2:3b")
    agent = create_agent(
        llm,
        tools=[get_user_info],
        checkpointer=InMemorySaver(),
    )

    thread_config = {"configurable": {"thread_id": "1"}}

    # Turn 1: State introduction
    print("--- Turn 1: Introducing user name ---")
    response_1 = agent.invoke(
        {"messages": [{"role": "user", "content": "Hi! My name is Sourav."}]},
        thread_config,
    )["messages"][-1].content
    print("Agent:", response_1)

    # Turn 2: State recall verification
    print("\n--- Turn 2: Verifying memory retention ---")
    response_2 = agent.invoke(
        {"messages": [{"role": "user", "content": "What's my name?"}]},
        thread_config,
    )["messages"][-1].content
    print("Agent:", response_2)


if __name__ == "__main__":
    main()

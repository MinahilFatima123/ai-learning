from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from typing import TypedDict

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

class AgentState(TypedDict):
    question: str
    answer: str

def ask_llm_node(state: AgentState) -> AgentState:
    print("--- asking LLM ---")
    response = llm.invoke(state["question"])
    return {"answer": response.content}

def format_node(state: AgentState) -> AgentState:
    print("--- formatting answer ---")
    formatted = f"Q: {state['question']}\nA: {state['answer']}"
    return {"answer": formatted}

graph = StateGraph(AgentState)

graph.add_node("llm", ask_llm_node)
graph.add_node("formatter", format_node)

graph.set_entry_point("llm")
graph.add_edge("llm", "formatter")
graph.add_edge("formatter", END)

app = graph.compile()

result = app.invoke({
    "question": "What is LangGraph in one sentence?",
    "answer": ""
})

print("\n", result["answer"])
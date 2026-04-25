from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from typing import TypedDict

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

class State(TypedDict):
    question: str
    answer: str
    needs_calculation: bool

# Node 1 — decide if math is needed
def classifier_node(state: State) -> State:
    print("--- classifier running ---")
    question = state["question"].lower()
    is_math = any(word in question for word in ["calculate", "multiply", "add", "subtract", "divide", "what is"])
    return {"needs_calculation": is_math}

# Node 2 — math path
def math_node(state: State) -> State:
    print("--- math_node running ---")
    response = llm.invoke(f"Solve this math problem and return only the answer: {state['question']}")
    return {"answer": f"[MATH] {response.content}"}

# Node 3 — general path
def general_node(state: State) -> State:
    print("--- general_node running ---")
    response = llm.invoke(state["question"])
    return {"answer": f"[GENERAL] {response.content}"}

# ✅ Router function — returns the name of the next node
def router(state: State) -> str:
    if state["needs_calculation"]:
        return "math"       # must match add_node name
    else:
        return "general"

graph = StateGraph(State)

graph.add_node("classifier", classifier_node)
graph.add_node("math", math_node)
graph.add_node("general", general_node)

graph.set_entry_point("classifier")

# ✅ Conditional edge — classifier decides which node runs next
graph.add_conditional_edges(
    "classifier",   # from this node
    router,         # call this function to decide
    {
        "math": "math",         # if router returns "math" → go to math node
        "general": "general"    # if router returns "general" → go to general node
    }
)

graph.add_edge("math", END)
graph.add_edge("general", END)

app = graph.compile()

# Test math path
print("=== Test 1: Math ===")
r1 = app.invoke({"question": "What is 144 divided by 12?", "answer": "", "needs_calculation": False})
print("Answer:", r1["answer"])

# Test general path
print("\n=== Test 2: General ===")
r2 = app.invoke({"question": "Why is Python popular?", "answer": "", "needs_calculation": False})
print("Answer:", r2["answer"])
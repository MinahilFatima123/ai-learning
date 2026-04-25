from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, END
from typing import TypedDict

# ✅ Step 1 — Define your State
# This is the dictionary that travels through every node
class MyState(TypedDict):
    name: str
    message: str

# ✅ Step 2 — Define Nodes (just plain functions)
def greet_node(state: MyState) -> MyState:
    print("--- greet_node running ---")
    return {"message": f"Hello, {state['name']}!"}

def shout_node(state: MyState) -> MyState:
    print("--- shout_node running ---")
    return {"message": state["message"].upper()}

# ✅ Step 3 — Build the Graph
graph = StateGraph(MyState)

graph.add_node("greeter", greet_node)   # register nodes
graph.add_node("shouter", shout_node)

graph.set_entry_point("greeter")        # where to start
graph.add_edge("greeter", "shouter")    # greeter → shouter
graph.add_edge("shouter", END)          # shouter → done

app = graph.compile()

# ✅ Step 4 — Run it
result = app.invoke({"name": "Minahil", "message": ""})
print("\nFinal State:", result)
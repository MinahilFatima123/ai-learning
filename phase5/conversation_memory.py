from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_react_agent, AgentExecutor
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.memory import ConversationBufferMemory
from langchain import hub

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

@tool
def calculator(expression: str) -> str:
    """Use this to do math. Input should be a math expression like '25 * 4' or '100 + 50'."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

@tool
def reverse_string(text: str) -> str:
    """Use this to reverse any string or word. Input is the text to reverse."""
    return text[::-1]

tools = [calculator, reverse_string]

# ✅ NEW — memory that persists across multiple invoke() calls
memory = ConversationBufferMemory(
    memory_key="chat_history",  # must match the prompt variable
    return_messages=True
)

prompt = hub.pull("hwchase17/react-chat")  # react-CHAT version, not react

agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,       # plugged in here
    verbose=True
)

# Turn 1 — tell it your name
executor.invoke({"input": "My name is Minahil"})

# Turn 2 — use a tool
executor.invoke({"input": "What is 16 * 3?"})

# Turn 3 — test if it remembers Turn 1
result = executor.invoke({"input": "What is my name?"})
final=executor.invoke({"input": "What calculation did I ask you to do earlier?"})
print("\nFinal Answer:", final["output"])
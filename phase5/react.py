from langchain.tools import tool
from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

load_dotenv()

# 1. LLM
llm = ChatGroq(
   model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# 2. Custom tool
@tool
def add_num(n1: int, n2: int) -> str:
    """Adds 2 numbers. Use this when the user wants to add two numbers."""
    return f"Result: {n1 + n2}"

# 3. Built-in tool (updated)
search_tool = TavilySearch(
    max_results=3,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)

# 4. Tools list
tools = [add_num, search_tool]

# 5. Create agent
agent_executor = create_agent(model=llm, tools=tools)

# 6. Run it
response = agent_executor.invoke({
    "messages": [{"role": "user", "content": "Who invented Python? Also add 1991 + 33"}]
})

# 7. Print final answer
print(response["messages"][-1].content)
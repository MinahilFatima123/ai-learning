from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import create_react_agent, AgentExecutor
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain import hub

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0,)

@tool
def calculator(expression: str) -> str:
    """Use this to do math. Input should be a math expression like '25 * 4' or '100 + 50'."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

@tool
def reverse_string(text: str) -> str:
    """Use this to reverse any string or word. Input is the text to reverse."""
    return text[::-1]

tools = [calculator, reverse_string]

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = executor.invoke({"input": "What is 25 multiplied by 4?"})
print("\nFinal Answer:", result["output"])
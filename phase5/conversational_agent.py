from dotenv import load_dotenv
import os
load_dotenv()
from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.tools import Tool
from langchain import hub

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

tools = [
    Tool(
        name="Calculator",
        func=lambda x: eval(x),
        description="Use for math calculations. Input is a math expression."
    )
]

# This is the only difference — memory is added
memory = ConversationBufferMemory(
    memory_key="chat_history",   # must match the prompt's variable name
    return_messages=True
)

prompt = hub.pull("hwchase17/react-chat")  # Note: react-CHAT, not just react

agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,      # plugged in here
    verbose=True
)

# Turn 1
executor.invoke({"input": "My name is Minahil"})

# Turn 2 — agent remembers Turn 1
executor.invoke({"input": "What is my name?"})
# → It will correctly say "Minahil"
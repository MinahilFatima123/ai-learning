from langchain_groq import ChatGroq
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

memory = ConversationBufferMemory()

chain = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True  # shows you exactly what gets sent to the LLM
)

print("=== Buffer Memory Chatbot ===\n")

chain.predict(input="Hi! My name is Minahil and I am a CS student.")
chain.predict(input="I am currently on Phase 3 of my AI learning roadmap.")
chain.predict(input="What is my name and what am I studying?")

# See raw memory contents
print("\n--- Raw Memory ---")
print(memory.load_memory_variables({}))
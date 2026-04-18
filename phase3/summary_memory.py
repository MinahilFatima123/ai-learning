from langchain_groq import ChatGroq
from langchain_classic.memory import ConversationSummaryMemory
from langchain_classic.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

# needs an LLM to generate the summary
memory = ConversationSummaryMemory(llm=llm)

chain = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print("=== Summary Memory Chatbot ===\n")

chain.predict(input="My name is Minahil. I am a CS student in Pakistan.")
chain.predict(input="I am learning LangChain and currently on Phase 3.")
chain.predict(input="I use Groq as my free LLM provider.")
chain.predict(input="What do you know about me so far?")

# See the summary instead of raw history
print("\n--- Memory Summary ---")
print(memory.load_memory_variables({}))
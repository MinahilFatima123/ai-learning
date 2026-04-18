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
    memory=memory
)

print("🤖 Chatbot with Memory — type 'quit' to exit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    
    response = chain.predict(input=user_input)
    print(f"Bot: {response}\n")
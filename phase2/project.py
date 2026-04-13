from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful assistant"}
]

while True:
    user_input = input("You: ")
    
    if user_input == "quit":
        print("Goodbye!")
        break       
    
    messages.append({  
        "role": "user", 
        "content": user_input
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7
    )
    
    reply = response.choices[0].message.content  
    
    print(f"Assistant: {reply}")
    
    messages.append({
        "role": "assistant",
        "content": reply
    })
  

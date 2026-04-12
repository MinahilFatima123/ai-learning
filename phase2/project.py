from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

question = "Write me a one sentence story"

for temp in [0.0, 0.7, 1.5]:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": question}],
        temperature=temp
    )
    print(f"Temp {temp}: {response.choices[0].message.content}")
    print("---")


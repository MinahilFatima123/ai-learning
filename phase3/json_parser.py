from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# No class needed!
parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract the information as JSON. {format_instructions}"),
    ("human", "{input}")
])

chain = prompt | llm | parser

result = chain.invoke({
    "input": "Minahil is a 20 year old CS student learning AI engineering in Pakistan.",
    "format_instructions": parser.get_format_instructions()
})

print(result)              # plain dictionary
print(result["name"])      # Minahil
print(type(result))        # <class 'dict'>
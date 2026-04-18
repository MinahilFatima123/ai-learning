from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# 1. Define your structure
class Person(BaseModel):
    name: str = Field(description="The person's full name")
    age: int = Field(description="The person's age")
    profession: str = Field(description="The person's job or field of study")

# 2. Create the parser
parser = PydanticOutputParser(pydantic_object=Person)

# 3. Create prompt — notice we inject format instructions
prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract the information from the text. {format_instructions}"),
    ("human", "{input}")
])

# 4. Build chain
chain = prompt | llm | parser

# 5. Run it
result = chain.invoke({
    "input": "Minahil is a 20 year old CS student who is learning AI engineering.",
    "format_instructions": parser.get_format_instructions()
})

print(result)           # Person object
print(result.name)      # Minahil
print(result.age)       # 20
print(result.profession) # CS student
print(type(result))     # <class 'Person'>
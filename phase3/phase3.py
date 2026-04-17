from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# create the LLM wrapper
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. Keep answers under 2 sentences."),
    ("human", "{question}")
])
roles=["Python teacher","5 year old child explainer" ,"Senior software engineer"]
for role in roles:
    filled=prompt.invoke({
        "role": role,
        "question": "What is an API?"
    })
    response = llm.invoke(filled)
    print(f"As {role}:")
    print(response.content)
    print("---")


##LCEL Chains
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# create the LLM wrapper
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. Keep answers under 2 sentences."),
    ("human", "{question}")
])

chain = prompt | llm
roles=["Python teacher","5 year old child explainer" ,"Senior software engineer"]
for role in roles:
    response=chain.invoke({
        "role": role,
        "question": "What is an API?"
    })
    print(f"As {role}:")
    print(response.content)
    print("---")

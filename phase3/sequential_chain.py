from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
import os

load_dotenv()

# create the LLM wrapper
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)
parser = StrOutputParser()      # converts AIMessage → plain string

# Chain 1
prompt1 = ChatPromptTemplate.from_template(
    "Generate one interesting blog topic idea about: {keyword}"
)
chain1 = prompt1 | llm | parser

# Chain 2
prompt2 = ChatPromptTemplate.from_template(
    "Write a compelling intro paragraph for this blog topic: {topic}"
)
chain2 = prompt2 | llm | parser

# Chain 3
prompt3 = ChatPromptTemplate.from_template(
    "Write a punchy tweet (under 280 chars) to promote a blog post "
    "with this intro: {intro}"
)
chain3 = prompt3 | llm | parser

# Updated full chain
full_chain = (
    chain1
    | (lambda topic: {"topic": topic})
    | chain2
    | (lambda intro: {"intro": intro})
    | chain3
)

result = full_chain.invoke({"keyword": "artificial intelligence"})
print(result)

# Step 1: get topic from chain1
step1 = RunnableParallel(
    topic=chain1,
    keyword=RunnablePassthrough()  # keep original input too
)

# Step 2: get intro from chain2, keep topic
step2 = RunnableParallel(
    intro=lambda x: (chain2.invoke({"topic": x["topic"]})),
    topic=lambda x: x["topic"]
)

# Step 3: get tweet from chain3, keep everything
step3 = RunnableParallel(
    tweet=lambda x: chain3.invoke({"intro": x["intro"]}),
    intro=lambda x: x["intro"],
    topic=lambda x: x["topic"]
)

full_chain = step1 | step2 | step3

result = full_chain.invoke({"keyword": "artificial intelligence"})

print(" TOPIC:\n",  result["topic"])
print("\n INTRO:\n", result["intro"])
print("\n TWEET:\n", result["tweet"])
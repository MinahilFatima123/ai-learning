from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process

# ✅ Just a string — no ChatGroq needed
MODEL = "groq/llama-3.3-70b-versatile"

researcher = Agent(
    role="Research Specialist",
    goal="Find detailed information about the given topic",
    backstory="""You are an expert researcher with years of experience 
    finding accurate and relevant information on any topic.""",
    llm=MODEL,
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Write clear and engaging summaries based on research",
    backstory="""You are a skilled writer who takes raw research 
    and turns it into clean, readable content.""",
    llm=MODEL,
    verbose=True
)

reviewer = Agent(
    role="Quality Reviewer",
    goal="Review content for clarity, accuracy and completeness",
    backstory="""You are a strict editor who ensures all content 
    is high quality before it goes out.""",
    llm=MODEL,
    verbose=True
)

research_task = Task(
    description="Research the topic: {topic}. Find key facts, use cases, and importance.",
    expected_output="A detailed bullet-point list of findings about the topic.",
    agent=researcher
)

write_task = Task(
    description="Using the research provided, write a short 3-paragraph summary about {topic}.",
    expected_output="A clean 3-paragraph article about the topic.",
    agent=writer
)

review_task = Task(
    description="Review the written summary. Check for clarity and suggest improvements.",
    expected_output="A final polished version of the article with review notes.",
    agent=reviewer
)

crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, write_task, review_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"topic": "LangGraph"})
print("\n===== FINAL OUTPUT =====")
print(result)
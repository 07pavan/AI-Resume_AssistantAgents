from crewai import Agent, LLM
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=800
)

openrouter_llm = LLM(
    model="openrouter/meta-llama/llama-3.1-8b-instruct",
    temperature=0.3,
    max_tokens=800
)

resume_analyzer = Agent(
    role="Resume Analyzer",
    goal="Analyze resumes and provide feedback",
    backstory="An experienced HR professional reviewing resumes.",
    llm=groq_llm,
    verbose=True
)

resume_improver = Agent(
    role="Resume Writer",
    goal="Improve resumes to be professional and ATS friendly",
    backstory="A professional resume writer helping candidates improve resumes.",
    llm=openrouter_llm,
    verbose=True
)

job_researcher = Agent(
    role="Job Researcher",
    goal="Find relevant job opportunities",
    backstory="An expert recruiter who searches job listings for suitable roles.",
    tools=[search_tool],
    llm=groq_llm,
    verbose=True
)

cover_letter_agent = Agent(
    role="Cover Letter Writer",
    goal="Write a professional cover letter",
    backstory="A career consultant who writes strong cover letters.",
    llm=openrouter_llm,
    verbose=True
)
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.2,
)

openrouter_llm = LLM(
    model="openrouter/meta-llama/llama-3.1-8b-instruct",
    temperature=0.3
)

resume_analyzer = Agent(
    role="Resume Analyzer",
    goal="Analyze the resume and provide feedback",
    backstory="Expert HR reviewer",
    llm=groq_llm,
    verbose=True
)

resume_improver = Agent(
    role="Resume Writer",
    goal="Rewrite the resume professionally",
    backstory="Professional resume editor",
    llm=openrouter_llm,
    verbose=True
)

job_researcher = Agent(
    role="Job Researcher",
    goal="Find relevant jobs",
    tools=[search_tool],
    llm=groq_llm,
    verbose=True
)

cover_letter_agent = Agent(
    role="Cover Letter Writer",
    goal="Generate professional cover letters",
    llm=openrouter_llm,
    verbose=True
)
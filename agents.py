from crewai import Agent
from crewai_tools import SerperDevTool
from llm_router import get_llm

search_tool = SerperDevTool()

resume_analyzer = Agent(
    role="Resume Analyzer",
    goal="Analyze resumes and provide improvement suggestions",
    backstory="Experienced HR professional evaluating candidate resumes.",
    llm=get_llm("analysis"),
    verbose=True
)

resume_improver = Agent(
    role="Resume Writer",
    goal="Rewrite resumes to make them professional and ATS friendly",
    backstory="Professional resume writer with expertise in ATS optimization.",
    llm=get_llm("improve"),
    verbose=True
)

job_researcher = Agent(
    role="Job Researcher",
    goal="Find relevant job opportunities for candidates",
    backstory="Expert recruiter who researches job openings.",
    tools=[search_tool],
    llm=get_llm("jobs"),
    verbose=True
)

cover_letter_agent = Agent(
    role="Cover Letter Writer",
    goal="Generate professional cover letters",
    backstory="Career consultant who writes strong cover letters.",
    llm=get_llm("cover_letter"),
    verbose=True
)
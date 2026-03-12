from crewai import Crew
from tasks import create_tasks
from agents import *

def run_resume_assistant(parsed_resume, options):

    tasks = create_tasks(parsed_resume, options)

    selected_agents = []

    if "analysis" in options:
        selected_agents.append(resume_analyzer)

    if "improve" in options:
        selected_agents.append(resume_improver)

    if "jobs" in options:
        selected_agents.append(job_researcher)

    if "cover_letter" in options:
        selected_agents.append(cover_letter_agent)

    crew = Crew(
        agents=selected_agents,
        tasks=tasks,
        verbose=False
    )

    result = crew.kickoff()

    return result
from crewai import Crew
from agents import *
from tasks import create_tasks

def run_resume_assistant(resume_text, options):

    tasks = create_tasks(resume_text, options)

    crew = Crew(
        agents=[
            resume_analyzer,
            resume_improver,
            job_researcher,
            cover_letter_agent
        ],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return result
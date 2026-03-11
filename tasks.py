from crewai import Task
from agents import *

def create_tasks(resume_text):

    analyze_resume_task = Task(
        description=f"Analyze this resume:\n{resume_text}",
        expected_output="Detailed resume analysis",
        agent=resume_analyzer
    )

    improve_resume_task = Task(
        description=f"Improve this resume:\n{resume_text}",
        expected_output="Improved professional resume",
        agent=resume_improver
    )

    job_search_task = Task(
        description="Find 5 relevant jobs for the candidate",
        expected_output="List of relevant job roles",
        agent=job_researcher
    )

    cover_letter_task = Task(
        description="Generate a professional cover letter",
        expected_output="A strong cover letter",
        agent=cover_letter_agent
    )

    return [
        analyze_resume_task,
        improve_resume_task,
        job_search_task,
        cover_letter_task
    ]
from crewai import Task
from agents import *

def create_tasks(resume_text):

    analyze_resume_task = Task(
        description=f"Analyze this resume:\n{resume_text}",
        expected_output="Detailed resume feedback",
        agent=resume_analyzer
    )

    improve_resume_task = Task(
        description=f"Improve this resume:\n{resume_text}",
        expected_output="Improved professional resume",
        agent=resume_improver
    )

    job_search_task = Task(
        description="Find 5 relevant jobs based on candidate skills",
        expected_output="Job title, company and location",
        agent=job_researcher
    )

    cover_letter_task = Task(
        description="Write a cover letter for the candidate",
        expected_output="Professional cover letter",
        agent=cover_letter_agent
    )

    return [
        analyze_resume_task,
        improve_resume_task,
        job_search_task,
        cover_letter_task
    ]
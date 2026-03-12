from crewai import Task
from agents import *

def create_tasks(resume_text, options):

    tasks = []

    if "analysis" in options:
        tasks.append(
            Task(
                description=f"Analyze this resume:\n{resume_text}",
                expected_output="Detailed resume feedback",
                agent=resume_analyzer
            )
        )

    if "improve" in options:
        tasks.append(
            Task(
                description=f"Improve this resume:\n{resume_text}",
                expected_output="Improved professional resume",
                agent=resume_improver
            )
        )

    if "jobs" in options:
        tasks.append(
            Task(
                description="Find 5 relevant jobs for this candidate",
                expected_output="List of jobs",
                agent=job_researcher
            )
        )

    if "cover_letter" in options:
        tasks.append(
            Task(
                description="Write a professional cover letter",
                expected_output="A strong cover letter",
                agent=cover_letter_agent
            )
        )

    return tasks
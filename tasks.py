from crewai import Task
from agents import *

def create_tasks(parsed_resume, options):

    tasks = []

    if "analysis" in options:

        tasks.append(
            Task(
                description=f"""
Analyze this candidate profile.

Skills: {parsed_resume['skills']}
Projects: {parsed_resume['projects']}
Education: {parsed_resume['education']}
Experience: {parsed_resume['experience']}
""",
                expected_output="Detailed resume feedback",
                agent=resume_analyzer
            )
        )

    if "improve" in options:

        tasks.append(
            Task(
                description=f"""
Improve this candidate resume.

Skills: {parsed_resume['skills']}
Projects: {parsed_resume['projects']}
Education: {parsed_resume['education']}
""",
                expected_output="Improved professional resume",
                agent=resume_improver
            )
        )

    if "jobs" in options:

        tasks.append(
            Task(
                description=f"""
Find relevant job opportunities for a candidate with these skills:

{parsed_resume['skills']}
""",
                expected_output="List of relevant jobs",
                agent=job_researcher
            )
        )

    if "cover_letter" in options:

        tasks.append(
            Task(
                description=f"""
Write a professional cover letter for a candidate with:

Skills: {parsed_resume['skills']}
Projects: {parsed_resume['projects']}
""",
                expected_output="Professional cover letter",
                agent=cover_letter_agent
            )
        )

    return tasks
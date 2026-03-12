def run_resume_assistant(resume_text, options):

    try:
        tasks = create_tasks(resume_text, options)

        crew = Crew(
            agents=[
                resume_analyzer,
                resume_improver,
                job_researcher,
                cover_letter_agent
            ],
            tasks=tasks,
            verbose=False
        )

        result = crew.kickoff()

        return result

    except Exception as e:
        return f"Error occurred: {str(e)}"
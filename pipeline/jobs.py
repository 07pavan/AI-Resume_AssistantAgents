from llm.llm_client import generate_response


def suggest_jobs(resume_text):

    prompt = f"""
Based on the following resume suggest suitable job roles.

Resume:
{resume_text[:2000]}

Return:

Job Title
Required Skills
Short Description
"""

    return generate_response(prompt)
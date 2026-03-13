from llm.llm_client import generate_response


def generate_cover_letter(resume, job_role):

    prompt = f"""
Write a professional cover letter.

Resume:
{resume[:2500]}

Job Role:
{job_role}

Keep it concise and professional.
"""

    return generate_response(prompt)
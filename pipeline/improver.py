from llm.llm_client import generate_response


def improve_resume(resume_text, analysis):

    prompt = f"""
Improve this resume based on the recruiter feedback.

Resume:
{resume_text[:3000]}

Feedback:
{analysis}

Generate an ATS optimized resume.
"""

    return generate_response(prompt)
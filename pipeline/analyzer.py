from llm.llm_client import generate_response


def analyze_resume(resume_text):

    prompt = f"""
You are a professional recruiter.

Analyze this resume and give feedback on:

1. Skills
2. Experience
3. Projects
4. ATS compatibility
5. Missing skills

Resume:
{resume_text[:3500]}
"""

    return generate_response(prompt)
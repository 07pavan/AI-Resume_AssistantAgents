from llm.llm_client import generate_response


def calculate_ats_score(resume_text):

    prompt = f"""
You are an ATS (Applicant Tracking System).

Evaluate this resume and give:

1. ATS Score (0-100)
2. Strengths
3. Weaknesses
4. Missing keywords

Resume:
{resume_text[:3000]}

Return format:

ATS Score: <number>/100

Strengths:
- ...

Weaknesses:
- ...

Missing Keywords:
- ...
"""

    return generate_response(prompt)
from llm.llm_client import generate_response


def match_resume_to_job(resume_text, job_role):

    prompt = f"""
You are an AI hiring assistant.

Compare the resume with the job role and calculate a match score.

Resume:
{resume_text[:3000]}

Job Role:
{job_role}

Return in this format:

Match Score: <number>%

Matching Skills:
- skill
- skill

Missing Skills:
- skill
- skill

Short Recommendation:
1-2 sentences explaining how the candidate can improve.
"""

    try:

        result = generate_response(prompt)

        return result

    except Exception as e:

        return f"⚠️ Unable to calculate job match score: {str(e)}"
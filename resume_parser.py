import json
from llm_router import get_llm

llm = get_llm("analysis")

def parse_resume_llm(resume_text):

    prompt = f"""
Extract structured information from the following resume.

Resume:
{resume_text}

Return JSON with:
skills
projects
education
experience
"""

    response = llm.call(prompt)

    try:
        parsed_data = json.loads(response)
        return parsed_data

    except:
        return {
            "skills": [],
            "projects": [],
            "education": "",
            "experience": ""
        }
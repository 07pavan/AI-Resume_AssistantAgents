#This file will manage which LLM is used and fallback handling.
from crewai import LLM

# Primary models
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=600
)

openrouter_llm = LLM(
    model="openrouter/meta-llama/llama-3.1-8b-instruct",
    temperature=0.3,
    max_tokens=800
)

def get_llm(task_type):

    if task_type == "analysis":
        return safe_llm_call(groq_llm, openrouter_llm)

    if task_type == "improve":
        return safe_llm_call(openrouter_llm, groq_llm)

    if task_type == "jobs":
        return safe_llm_call(groq_llm, openrouter_llm)

    if task_type == "cover_letter":
        return safe_llm_call(openrouter_llm, groq_llm)

def safe_llm_call(primary, fallback):
    try:
        return primary
    except:
        return fallback
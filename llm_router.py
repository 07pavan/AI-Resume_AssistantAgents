from crewai import LLM

groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.2
)

deepseek_llm = LLM(
    model="deepseek/deepseek-chat",
    temperature=0.3
)

openrouter_llm = LLM(
    model="openrouter/meta-llama/llama-3.1-8b-instruct"
)

together_llm = LLM(
    model="together/mistralai/Mixtral-8x7B-Instruct-v0.1"
)

hf_llm = LLM(
    model="huggingface/mistralai/Mistral-7B-Instruct-v0.2"
)


def get_llm(agent_name):

    if agent_name == "parser":
        return groq_llm

    elif agent_name == "analyzer":
        return deepseek_llm

    elif agent_name == "improver":
        return openrouter_llm

    elif agent_name == "job":
        return together_llm

    elif agent_name == "cover":
        return hf_llm

    else:
        raise ValueError(f"Unknown agent: {agent_name}")
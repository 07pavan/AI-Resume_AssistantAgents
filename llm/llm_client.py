import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def generate_response(prompt, retries=3):

    for attempt in range(retries):

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are an expert resume assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            return response.choices[0].message.content

        except Exception as e:

            print(f"LLM Error: {e}")

            if attempt < retries - 1:
                print("Retrying...")
                time.sleep(3)
            else:
                return "Error: Unable to generate response right now."
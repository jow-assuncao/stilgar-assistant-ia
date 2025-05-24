import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_system_message(original_role, memory_context=""):
    system_message = original_role.strip()

    if memory_context:
        system_message += f"""

Abaixo estão memórias relevantes resgatadas do banco vetorial, para te ajudar a responder:

{memory_context.strip()}"""

    return system_message

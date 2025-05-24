from core.config import client, create_system_message
from core.memory import add_to_memory, search_memory
from utils.helpers import load_history
import uuid


def ask_stilgar(question):
    history = load_history()
    messages = []

    system_message = next((m for m in history if m["role"] == "system"), None)
    context = search_memory(question)

    if context:
        top_context = "\n".join(context[:3])
        messages = [
            {
                "role": "system",
                "content": create_system_message(
                    system_message["content"], top_context
                ),
            }
        ]
    else:
        messages = [
            {
                "role": "system",
                "content": create_system_message(system_message["content"]),
            }
        ]

    messages.append({"role": "user", "content": question})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=300
        )
        answer = response.choices[0].message.content.strip()

        document_text = f"user: {question}\nstilgar: {answer}"

        add_to_memory(
            document_text,
            metadata={
                "role": "dialogue",
                "type": "qa-pair",
            },
            uid=str(uuid.uuid4()),
        )

        return answer
    except Exception as e:
        return f"Erro: {e}"

from chat.config import client
from utils.helpers import load_history, save_history


def ask_stilgar(question):
    history = load_history()
    messages = []

    system_message = next((m for m in history if m["role"] == "system"), None)

    if system_message:
        messages = [system_message]
    else:
        messages = []

    messages.extend(history[-6:])
    messages.append({"role": "user", "content": question})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=300
        )
        answer = response.choices[0].message.content.strip()
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer})
        save_history(history)
        return answer
    except Exception as e:
        return f"Erro: {e}"

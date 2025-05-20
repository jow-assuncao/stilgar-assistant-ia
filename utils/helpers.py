import json
import os

HISTORY_PATH = "memory/history.json"
INTERPRETOR_ROLE_PATH = "memory/interpretor.json"


def load_history():
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
        
def load_interpretor_role():
    if os.path.exists(INTERPRETOR_ROLE_PATH):
        with open(INTERPRETOR_ROLE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
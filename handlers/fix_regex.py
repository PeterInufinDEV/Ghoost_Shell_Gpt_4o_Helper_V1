# handlers/fix_regex.py
from utils.openai_client import ask_gpt

def handle(regex):
    prompt = (
        f"This regex pattern may be broken or unclear: {regex}\n"
        f"Please fix it and explain what it does in plain English."
    )
    return ask_gpt(prompt, system_msg="You are a regex expert.")

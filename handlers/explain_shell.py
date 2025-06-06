# handlers/explain_shell.py
from utils.openai_client import ask_gpt

def handle(command):
    prompt = (
        f"Explain what this shell command does in simple, clear language:\n\n{command}"
    )
    return ask_gpt(prompt, system_msg="You are a Linux shell expert.")

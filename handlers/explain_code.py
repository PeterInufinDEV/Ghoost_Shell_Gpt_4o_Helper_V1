# handlers/explain_code.py
from utils.openai_client import ask_gpt

def handle(code):
    prompt = f"Please explain what the following code does:\n\n{code}"
    return ask_gpt(prompt, system_msg="You are an expert software engineer.")

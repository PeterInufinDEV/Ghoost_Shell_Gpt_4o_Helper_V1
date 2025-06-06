# handlers/text_gen.py
from utils.openai_client import ask_gpt

def handle(prompt):
    return ask_gpt(prompt, system_msg="You are a creative writing assistant.")

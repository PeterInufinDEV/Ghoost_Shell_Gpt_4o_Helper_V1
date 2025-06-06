# main.py
import os
import sys
from datetime import datetime

from utils.openai_client import ask_gpt

ascii_logo = r"""
██████╗ ███████╗██████╗ ██╗██████╗ ████████╗██╗  ██╗
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██║  ██║
██████╔╝█████╗  ██████╔╝██║██████╔╝   ██║   ███████║
██╔══██╗██╔══╝  ██╔══██╗██║██╔══██╗   ██║   ██╔══██║
██║  ██║███████╗██████║ ██║██║  ██║   ██║   ██║  ██║
╚═╝  ╚═╝╚══════╝╚════╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
         GPT-HELPER | REBIRTH TERMINAL MODE     
-------------------------------------------------------
 Welcome back, ANONYMOUS. Today is {date}
-------------------------------------------------------
""".format(date=datetime.now().strftime("%A, %d %B %Y"))

actions = {
    "1": ("Generate Text", "You are a creative writing assistant."),
    "2": ("Explain Code", "You are an expert software engineer."),
    "3": ("Fix Regex", "You are a regex expert."),
    "4": ("Explain Shell Command", "You are a Linux shell expert.")
}

def show_menu():
    print(ascii_logo)
    for key, (label, _) in actions.items():
        print(f"[{key}] {label}")
    print("[0] Exit")

def main():
    while True:
        show_menu()
        choice = input("\nSelect an option: ").strip()
        
        if choice == "0":
            print("\nGoodbye.")
            break
        elif choice in actions:
            task, system_msg = actions[choice]
            prompt = input(f"\nEnter your prompt for {task}: ").strip()
            if not prompt:
                print("XXX Prompt cannot be empty.\n")
                continue
            print("\n>>> Thinking...")
            result = ask_gpt(prompt, system_msg)
            print(f"\n=== {task.upper()} RESULT ===\n{result}\n")
            input("Press Enter to continue...")
        else:
            print("XXX Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()

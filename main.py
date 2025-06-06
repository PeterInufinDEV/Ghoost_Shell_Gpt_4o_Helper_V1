import os
from datetime import datetime
from colorama import init, Fore, Style

from handlers.text_gen import handle as generate_text
from handlers.explain_code import handle as explain_code
from handlers.fix_regex import handle as fix_regex
from handlers.explain_shell import handle as explain_shell

init(autoreset=True)  # Initialize colorama

ascii_logo = f"""{Fore.CYAN}
               ██████╗          ███████╗
              ██╔═══██╗         ██╔════╝
              ██║   ██║         █████╗  
              ██║   ██║         ██╔══╝  
              ╚██████╔╝         ███████╗
            Gh ╚═════╝ ost - Sh ╚══════╝ ll 

{Fore.YELLOW}    GPT-4o-HELPER | Author: PENREBIRTH TERMINAL MODE  {Fore.GREEN}[V1]   
{Fore.MAGENTA}----------------------------------------------------------
 Welcome back, {Fore.GREEN}ANONYMOUS{Fore.MAGENTA}. Today is {Fore.WHITE}{datetime.now().strftime("%A, %d %B %Y")}
----------------------------------------------------------{Style.RESET_ALL}
"""

actions = {
    "1": ("Generate Text", generate_text),
    "2": ("Explain Code", explain_code),
    "3": ("Fix Regex", fix_regex),
    "4": ("Explain Shell Command", explain_shell),
}

def show_menu():
    print(ascii_logo)
    for key, (label, _) in actions.items():
        print(f"{Fore.CYAN}[{key}]{Style.RESET_ALL} {Fore.WHITE}{label}")
    print(f"{Fore.RED}[0] Exit{Style.RESET_ALL}")

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        clear_terminal()
        show_menu()
        choice = input(f"\n{Fore.YELLOW}Select an option: {Style.RESET_ALL}").strip()
        
        if choice == "0":
            print(f"\n{Fore.GREEN}Goodbye.{Style.RESET_ALL}")
            break
        elif choice in actions:
            task, handler = actions[choice]
            prompt = input(f"\n{Fore.BLUE}Enter your prompt for {task}: {Style.RESET_ALL}").strip()
            if not prompt:
                print(f"{Fore.RED}XXX Prompt cannot be empty.\n")
                continue
            print(f"\n{Fore.CYAN}>>> Thinking...{Style.RESET_ALL}")
            result = handler(prompt)
            print(f"\n{Fore.GREEN}=== {task.upper()} RESULT ===\n{Style.RESET_ALL}{result}\n")
            input(f"{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}XXX Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()

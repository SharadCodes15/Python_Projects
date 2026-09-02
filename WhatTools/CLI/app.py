from main import pyAuto
import os
import sys
import time

# ---------------
# Colors 
# ---------------

RESET = "\033[0m"
BOLD = "\033[1m"

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"
GRAY = "\033[90m"

# ---------------
# Terminal Helpers
# ---------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def pause():
    input(f"\n{GRAY} Press Enter to Continue..... {RESET}")

def print_line(char='-',width=62):
    print(f"{CYAN}{char*width}{RESET}")

def print_box(title,width=62):
    print(f"{CYAN}╔{'═' * width}╗{RESET}")
    print(
        f"{CYAN}║{RESET}"
        f"{BOLD}{WHITE}{title.center(width)}{RESET}"
        f"{CYAN}║{RESET}"
    )
    print(f"{CYAN}╚{'═' * width}╝{RESET}")

# ---------------
# Header
# ---------------

def show_header():
    width = 62

    lines = [
        "███████╗ █████╗ ███╗   ███╗",
        "██╔════╝██╔══██╗████╗ ████║",
        "███████╗███████║██╔████╔██║",
        "╚════██║██╔══██║██║╚██╔╝██║",
        "███████║██║  ██║██║ ╚═╝ ██║",
        "╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝",
    ]

    print(f"{CYAN}╔{'═' * width}╗{RESET}")

    print(f"{CYAN}║{' ' * width}║{RESET}")

    for line in lines:
        print(
            f"{CYAN}║{RESET}"
            f"{BOLD}{WHITE}{line.center(width)}{RESET}"
            f"{CYAN}║{RESET}"
        )

    print(f"{CYAN}║{' ' * width}║{RESET}")

    print(
        f"{CYAN}║{RESET}"
        f"{BOLD}{WHITE}{'SAM What Tools'.center(width)}{RESET}"
        f"{CYAN}║{RESET}"
    )

    print(
        f"{CYAN}║{RESET}"
        f"{WHITE}{'What Tools'.center(width)}{RESET}"
        f"{CYAN}║{RESET}"
    )

    print(f"{CYAN}║{' ' * width}║{RESET}")

    print(f"{CYAN}╚{'═' * width}╝{RESET}")



# ---------------
# Menu
# ---------------

def show_menu():
    menu = [
        "[1]  Spam Message",
        "[2]  Coming soon",
        "[3]  About",
        "[4]  Exit"
    ]

    width = 60

    print(f"\n{WHITE}{BOLD}")
    print("┌" + "─" * width + "┐")
    print("│" + "MAIN MENU".center(width) + "│")
    print("├" + "─" * width + "┤")

    for item in menu:
        print("│   " + item.ljust(width - 3) + "│")

    print("└" + "─" * width + "┘")
    print(RESET)

# ---------------
# Spam Messages
# ---------------

def spamMessageAfterScreen(message,num,interval):
    title = "✔ Sending Message"

    lines = [
        f"Message: {message}",
        f"Frequency: {num}",
        f"Interval: {interval}",
    ]

    content_width = max(
        len(title),
        *(len(line) + 2 for line in lines)
    ) + 2

    print()
    print(f"{GREEN}╔{'═' * content_width}╗")
    print(f"║{title.center(content_width)}║")
    print(f"╠{'═' * content_width}╣")

    for line in lines:
        print(f"║  {line:<{content_width - 2}}║")

    print(f"╚{'═' * content_width}╝{RESET}")


def spam():
    print("Spam Messages")
    message = input(
        f"\n{YELLOW}➜ Enter Message : {RESET}"
    ).strip()
    if not message:
        print(f"{RED}Error: Message cannot be empty.{RESET}")
        pause()
        return

    try:
        num = input(
        f"\n{YELLOW}➜ Enter Frequency : (default 0) {RESET}"
    ).strip()
        time.sleep(0.5)
        interval = input(
                f"\n{YELLOW}➜ Enter Interval : (default 0.5s) {RESET}"
            ).strip()
        pyGUI = pyAuto();
        time.sleep(0.5)
        print(f"{GREEN}| Open Whatsapp and Press Input bar |{RESET}")
        spamMessageAfterScreen(message,num,interval);
        result = pyGUI.spamMessages(message=message,num=num,interval=interval);
        if result != 1:
            print(f"\n{RED}✘ Failed to Send Messages with Error \n {result}.{RESET}")
    except Exception as e:
            print(f"\n{RED}✘ Failed to Send Messages with Error \n {e}.{RESET}")

    pause()


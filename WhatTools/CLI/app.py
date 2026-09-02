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

def thankyou():
    title = "Thank you for using QR Generator!"
    goodbye = "Goodbye 👋"

    width = max(len(title), len(goodbye)) + 10

    print(f"""
{CYAN}╔{'═' * width}╗
║{' ' * width}║
║{BOLD}{WHITE}{title.center(width)}{RESET}{CYAN}║
║{' ' * width}║
║{goodbye.center(width)}║
║{' ' * width}║
╚{'═' * width}╝{RESET}
""")


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
        num = int(input(
        f"\n{YELLOW}➜ Enter Frequency : (default 1) {RESET}"
    ).strip() or "1")
        time.sleep(0.5)
        interval = float(input(
                f"\n{YELLOW}➜ Enter Interval : (default 0.5s) {RESET}"
            ).strip() or "0.5")
        pyGUI = pyAuto();
        time.sleep(0.5)
        print(f"{GREEN}| Open Whatsapp and Press Input bar |{RESET}")
        spamMessageAfterScreen(message,num,interval);
        result = pyGUI.spamMessages(message=message,num=num,interval=interval);
        if result != 1:
            print(f"\n{RED}✘ Failed to Send Messages with Error \n {result}.{RESET}")
        print(f"\n{GREEN}| ✔ Successfully Sent |{RESET}")
    except Exception as e:
            print(f"\n{RED}✘ Failed to Send Messages with Error \n {e}.{RESET}")

    pause()

def main():
    while True:
        clear_screen()
        show_header()
        show_menu()

        choice = input(
            f"{YELLOW}➜ Select an option [1-4]: {RESET}"
        ).strip()

        if choice == "1":
            clear_screen()
            show_header()
            spam()

        elif choice == "2":
            clear_screen()
            show_header()
            print("Comming Soon...")

        elif choice == "3":
            clear_screen()
            show_header()
            # about()
            print("Comming Soon...")


        elif choice == "4":
            clear_screen()
            thankyou()
            sys.exit(0)

        else:
            print(f"\n{RED}✘ Invalid option. Please choose 1-4.{RESET}")
            time.sleep(1)



# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
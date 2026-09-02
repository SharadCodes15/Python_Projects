from main import QRCodeGenerator
import os
import sys
import time
from PIL import Image

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
    input(f"\n{GRAY} Press Enter to Continue .... {RESET}")

def print_line(char="-",width=62):
    print(f"{CYAN}{char * width}{RESET}")

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
        f"{BOLD}{WHITE}{'SAM QR'.center(width)}{RESET}"
        f"{CYAN}║{RESET}"
    )

    print(
        f"{CYAN}║{RESET}"
        f"{WHITE}{'QR CODE GENERATOR'.center(width)}{RESET}"
        f"{CYAN}║{RESET}"
    )

    print(f"{CYAN}║{' ' * width}║{RESET}")

    print(f"{CYAN}╚{'═' * width}╝{RESET}")

# ---------------
# Menu
# ---------------


def show_menu():
    menu = [
        "[1]  Generate QR Code",
        "[2]  Generate & Save QR Code",
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
# Generate QR
# ---------------

def generate_qr():
    print("GENERATE QR CODE")
    url = input(
        f"\n{YELLOW}➜ Enter URL / text: {RESET}"
    ).strip()
    if not url:
        print(f"\n{RED}✘ Input cannot be empty.{RESET}")
        pause()
        return

    try:
        print(f"\n{GRAY}Generating QR code...{RESET}")
        time.sleep(0.5)
        qr = QRCodeGenerator()
        qr.generateQR(url)
        print(f"{GREEN}✔ QR code generated successfully!{RESET}")
        return qr
    except Exception as e:
        print(f"\n{RED}✘ Failed to generate QR code.{RESET}")
        print(f"{GRAY}Error: {e}{RESET}")

    pause()

# ─────────────────────────────────────────────────────────────
# Generate + Save
# ─────────────────────────────────────────────────────────────

def generate_and_save():
    print_box("GENERATE & SAVE QR CODE")

    url = input(
        f"\n{YELLOW}➜ Enter URL / text: {RESET}"
    ).strip()

    if not url:
        print(f"\n{RED}✘ Input cannot be empty.{RESET}")
        pause()
        return

    filename = input(
        f"{YELLOW}➜ Filename [qr.png]: {RESET}"
    ).strip()

    if not filename:
        filename = "qr.png"

    if not filename.lower().endswith(".png"):
        filename += ".png"

    try:
        print(f"\n{GRAY}Generating...{RESET}")

        qr = QRCodeGenerator()
        qr.generateQR(url)

        qr.saveQR(filename)

        print()
        print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                          ✔ SUCCESS                           ║")
        print(f"╠══════════════════════════════════════════════════════════════╣")
        print(f"║  QR Code saved successfully!                                 ║")
        print(f"║                                                              ║")
        print(f"║  File: {filename:<54}║")
        print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")

    except Exception as e:
        print(f"\n{RED}✘ Error: {e}{RESET}")

    pause()


# ─────────────────────────────────────────────────────────────
# About
# ─────────────────────────────────────────────────────────────

def about():
    print_box("ABOUT")

    print(f"""
{WHITE}
    QR Code Generator
    ──────────────────

    A simple command-line QR code generator.

    Features:
      • URL / text QR generation
      • PNG output
      • Interactive CLI
      • Input validation
      • Colored terminal interface

    Version: 1.0.0 CLI
{RESET}
""")

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
            generate_qr()

        elif choice == "2":
            clear_screen()
            show_header()
            generate_and_save()

        elif choice == "3":
            clear_screen()
            show_header()
            about()

        elif choice == "4":
            clear_screen()

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


            sys.exit(0)

        else:
            print(f"\n{RED}✘ Invalid option. Please choose 1-4.{RESET}")
            time.sleep(1)

# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
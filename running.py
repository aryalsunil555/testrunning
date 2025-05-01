from datetime import datetime
import time
import random
import pyfiglet
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# List of fun fonts from pyfiglet
fonts = ["slant", "standard", "big", "block", "bubble", "digital", "doom", "isometric1"]
colors = [Fore.RED, Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA, Fore.BLUE]

def cool_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_time_and_greet(name):
    # Get current time
    now = datetime.now()
    formatted_time = now.strftime("%A, %d %B %Y - %I:%M:%S %p")

    # Select random font and color
    font = random.choice(fonts)
    color = random.choice(colors)

    # Create ASCII banner
    banner = pyfiglet.figlet_format(f"Hi {name}!", font=font)

    # Print stylish header
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX + "="*70)
    cool_print(Fore.LIGHTCYAN_EX + "🌟 Welcome to the Python Fun Time Console 🌟", 0.05)
    print(Fore.LIGHTWHITE_EX + "="*70)

    # Show date and time
    cool_print(Fore.LIGHTGREEN_EX + f"🕒 Current Date & Time: {formatted_time}", 0.02)
    print()

    # Show greeting banner
    print(color + banner)

    # Extra ASCII art
    cool_print(Fore.LIGHTYELLOW_EX + r"""
        (\_/)
        ( •_•)
       / >🍪   Here's a cookie for you!
    """, 0.01)

    print(Fore.LIGHTWHITE_EX + "="*70)
    cool_print(Fore.LIGHTMAGENTA_EX + "Have a fun-tastic day, Sunil! 😎", 0.04)

# Run it
display_time_and_greet("Sunil")


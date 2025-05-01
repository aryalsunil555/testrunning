# cool_greet.py
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
    output = ''
    for char in text:
        output += char
        time.sleep(delay)
    return output

def display_time_and_greet(name):
    # Get current time
    now = datetime.now()
    formatted_time = now.strftime("%A, %d %B %Y - %I:%M:%S %p")

    # Select random font and color
    font = random.choice(fonts)
    color = random.choice(colors)

    # Create ASCII banner
    banner = pyfiglet.figlet_format(f"Hi {name}!", font=font)

    # Start building the response
    result = ""
    result += "=" * 70 + "\n"
    result += cool_print(Fore.LIGHTCYAN_EX + "🌟 Welcome to the Python Fun Time Console 🌟", 0.05) + "\n"
    result += "=" * 70 + "\n"
    result += cool_print(Fore.LIGHTGREEN_EX + f"🕒 Current Date & Time: {formatted_time}", 0.02) + "\n\n"
    result += color + banner + "\n"
    result += cool_print(Fore.LIGHTYELLOW_EX + r"""
        (\_/)
        ( •_•)
       / >🍪   Here's a cookie for you!
    """, 0.01) + "\n"
    result += "=" * 70 + "\n"
    result += cool_print(Fore.LIGHTMAGENTA_EX + "Have a fun-tastic day, Susan! 😎", 0.04) + "\n"

    return result

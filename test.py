import getpass
import os
import sys
import time

# ===== SETTINGS =====
PASSWORD = "LARKINCONRADTOOL"

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

BANNER = f"""{GREEN}
░██████╗███████╗░█████╗░██╗░░░██╗██████╗░██╗████████╗██╗░░░██╗
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██║╚══██╔══╝╚██╗░██╔╝
╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝██║░░░██║░░░░╚████╔╝░
░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██║░░░██║░░░░░╚██╔╝░░
██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║██║░░░██║░░░░░░██║░░░
╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░
{RESET}"""

# ===== PASSWORD CHECK =====
pwd = getpass.getpass("🔒 Enter password: ")

if pwd != PASSWORD:
    print(f"{RED}❌ Access Denied!{RESET}")
    time.sleep(1)
    sys.exit()

# ===== CLEAR & SHOW BANNER =====
os.system("clear")
print(BANNER)
print(f"{GREEN}✅ Access Granted! Welcome to the tool.{RESET}")

# ===== YOUR TOOL CODE BELOW =====
# Example:
print("\nRunning tool...")

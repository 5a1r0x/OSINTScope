#!/usr/bin/env python3

"""
OSINTScope - 1.0
Developer: Syrox (5a1r0x)
License: MIT
Powered by AI
"""

import webbrowser
import argparse
import urllib.parse
import colorama

# Colors
red = colorama.Fore.RED
cyan = colorama.Fore.CYAN
green = colorama.Fore.GREEN
magenta = colorama.Fore.MAGENTA
yellow = colorama.Fore.YELLOW
reset = colorama.Fore.RESET

# ArgumentParser
parser = argparse.ArgumentParser(
    prog="osintscope",
    description="modern and extensible toolkit for Open Source Intelligence Gathering",
    epilog="use ethically and responsibly"
)
# Arguments
parser.add_argument('-gd', '--googledorks', help='google dorks, hacking', nargs=1, type=str, required=False)
parser.add_argument('-of', '--osintframework', help='osint framework', action='store_true', required=False)
# Args
args = parser.parse_args()

# Google Dorks
def googledorks():
    """Google Dorks, Hacking"""
    dorks = args.googledorks[0]
    query = urllib.parse.quote_plus(f"{dorks}")
    try:
        webbrowser.open_new(f"https://www.google.com/search?q={query}")
        print(f"[{magenta}#{reset}] {magenta}REPORT{reset}")
        print(f"[{cyan}@{reset}] Dorks: {cyan}{dorks}{reset}")
        print(f"[{green}@{reset}] Status: {green}Success{reset}")
    except Exception as e:
        print(f"{red}[E] {e}{reset}")

# OSINT Framework
def osintframework():
    """OSINT Framework"""
    website = "https://osintframework.com/"
    frameworks = [
        "Username",
        "Email Address",
        "Domain Name",
        "IP & MAC Address",
        "Images / Videos / Docs",
        "Social Networks",
        "Instant Messaging",
        "People Search Engines",
        "Dating",
        "Telephone Numbers",
        "Public Records",
        "Business Records",
        "Transportation",
        "Geolocation Tools / Maps",
        "Search Engines",
        "Forums / Blogs / IRC",
        "Archives",
        "Language Translation",
        "Metadata",
        "Mobile Emulation",
        "Terrorism",
        "Dark Web",
        "Digital Currency",
        "Classifieds",
        "Encoding / Decoding",
        "Tools",
        "AI Tools",
        "Malicious File Analysis",
        "Exploits & Advisories",
        "Threat Intelligence",
        "OpSec",
        "Documentation / Evidence Capture",
        "Training",
    ]
    try:
        print(f"[{magenta}#{reset}] {magenta}REPORT{reset}")
        print(f"[{cyan}@{reset}] Website: {cyan}{website}{reset}")
        for framework in frameworks:
            print(f"[{green}+{reset}] {framework}")
    except Exception as e:
        print(f"{red}[E] {e}{reset}")

def osintscope():
    if args.googledorks:
        googledorks()
    if args.osintframework:
        osintframework()

if __name__ == "__main__":
    osintscope()

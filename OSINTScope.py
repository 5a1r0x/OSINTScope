#!/usr/bin/env python3

"""
OSINTScope
Version: 1.0
Developer: Syrox (5a1r0x)
GitHub: https://github.com/5a1r0x/OSINTScope
License: MIT
Powered by AI
"""

import requests
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
    description="modern and extensible toolkit for open source intelligence gathering",
    epilog="use ethically and responsibly"
)
# Arguments
parser.add_argument('-gd', '--googledorks', help='google dorks, hacking', nargs=1, type=str, required=False)
parser.add_argument('-of', '--osintframework', help='osint framework', action='store_true', required=False)
parser.add_argument('-ot', '--osintools', help='osint tools', action='store_true', required=False)
parser.add_argument('-gh', '--github', help='github information', action='store_true', required=False)

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

# OSINT Tools
def osintools():
    """Osint Tools"""
    free_tools = [
        "Epieos = https://epieos.com/",
        "HaveIBeenPwned = https://haveibeenpwned.com/",
        "DeHashed = https://app.dehashed.com/",
        "Maltego = https://www.maltego.com/",
        "Spiderfoot = https://www.kali.org/tools/spiderfoot/",
        "TheHarvester = https://www.kali.org/tools/theharvester/",
        "WaybackMachine = https://web.archive.org/",
        "DNSDumpster = https://dnsdumpster.com/",
        "GHunt = https://github.com/mxrch/GHunt",
        "AwesomeOSINT = https://github.com/jivoi/awesome-osint"
    ]
    payment_tools = [
        "OSINT Industries = https://www.osint.industries/",
        "Skopenow = https://www.skopenow.com/",
        "DarkOwl = https://www.darkowl.com/",
        "RecordedFuture = https://www.recordedfuture.com/",
        "DigitalStakeout = https://www.digitalstakeout.com/",
        "ShadowDragon = https://shadowdragon.io/"
    ]
    
    try:
        print(f"[{magenta}#{reset}] {magenta}REPORT{reset}")
        print(f"[{cyan}@{reset}] Free{cyan}{reset}")
        for tool in free_tools:
            print(f"[{green}+{reset}] {tool}")
        print(f"[{cyan}@{reset}] Payment{cyan}{reset}")
        for tool in payment_tools:
            print(f"[{green}+{reset}] {tool}")
    except Exception as e:
        print(f"{red}[E] {e}{reset}")

# GitHub
def github():
    """GitHub Information"""
    r = requests.get("https://github.com/5a1r0x/OSINTScope", timeout=10)
    print(f"[{magenta}#{reset}] {magenta}REPORT{reset}")
    print(f"[{cyan}@{reset}] Name: {cyan}OSINTScope{reset}")
    print(f"[{cyan}@{reset}] Repository: {cyan}https://github.com/5a1r0x/OSINTScope{reset}")
    print(f"[{cyan}@{reset}] Public: {green}Yes{reset}") if r.ok else print(f"[{cyan}@{reset}] Public: {red}No{reset}")
    print(f"[{cyan}@{reset}] HTTPS: {cyan}https://github.com/5a1r0x/OSINTScope.git{reset}")
    print(f"[{cyan}@{reset}] CLI: {cyan}gh repo clone 5a1r0x/OSINTScope{reset}")
    print(f"[{cyan}@{reset}] Developer: {cyan}5a1r0x{reset}")
    print(f"[{cyan}@{reset}] Version: {cyan}1.0{reset}")

# OSINT Scope
def osintscope():
    """OSINTScope Main"""
    if args.googledorks:
        googledorks()
    if args.osintframework:
        osintframework()
    if args.osintools:
        osintools()
    if args.github:
        github()
# Run
if __name__ == "__main__":
    osintscope()

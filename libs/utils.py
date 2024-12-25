# libs/utils.py

from colorama import Fore

def print_success(message):
    print(Fore.GREEN + "[+] " + message)

def print_error(message):
    print(Fore.RED + "[-] " + message)

def print_status(message):
    print(Fore.YELLOW + "[*] " + message)

def ask_question(question):
    return input(Fore.WHITE + question + " ")

def parse_proxy_file(file_path):
    """Reads a proxy list from a file."""
    proxies = []
    try:
        with open(file_path, 'r') as f:
            proxies = [line.strip() for line in f.readlines()]
    except Exception as e:
        print_error(f"Error reading proxy file: {e}")
    return proxies

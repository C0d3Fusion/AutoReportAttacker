# libs/utils.py

from colorama import Fore

def parse_proxy_file(file_path):
    """Parses proxy file to get a list of proxies."""
    proxies = []
    try:
        with open(file_path, 'r') as f:
            proxies = f.read().splitlines()
    except FileNotFoundError:
        print_error(f"File not found: {file_path}")
    return proxies

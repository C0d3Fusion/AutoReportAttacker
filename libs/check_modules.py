# libs/check_modules.py

import sys

def check_modules():
    required_modules = ["requests", "colorama", "multiprocessing"]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"[ERROR] Missing module: {module}. Please install it using pip.")
            sys.exit(1)

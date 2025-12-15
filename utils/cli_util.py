import os

def clear_screen():
    # Check the operating system
    if os.name == 'nt':
        # For Windows
        _ = os.system('cls')
    else:
        # For macOS and Linux (os.name is 'posix')
        _ = os.system('clear')
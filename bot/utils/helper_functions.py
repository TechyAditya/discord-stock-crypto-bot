from datetime import datetime

# helper_functions.py
# Utility functions for the bot.

def log_command(author_name, command: str):
    """
    Logs the received command to the console.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Command executed by {author_name}: {command}")


def format_number(num):
    if num >= 1_000_000_000_000:
        return f'{num / 1_000_000_000_000:.2f}T'
    elif num >= 1_000_000_000:
        return f'{num / 1_000_000_000:.2f}B'
    elif num >= 1_000_000:
        return f'{num / 1_000_000:.2f}M'
    elif num >= 1_000:
        return f'{num / 1_000:.2f}K'
    else:
        return str(num)
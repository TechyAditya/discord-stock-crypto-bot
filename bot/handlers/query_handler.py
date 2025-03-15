def handle_query(command: str) -> str:
    """
    Process the command and return an appropriate response.

    For the 'test' command, it returns a fixed response.
    """
    if command.lower() == "test":
        return "The bot is working"
    else:
        return f"Unknown command: {command}"


def handle_help(args):
    """
    Process the help command and return a help message.
    """
    command = args[0].lower() if args else ""
    match command:
        case "test":
            return "Check if the bot is working"

        case "stocks" | "s":
            return (
                "Usage: \\stocks [option] | s\n"
                "Available options:\n"
                "- index [indexname] | i: Get the latest quote for the given index\n"
                "- equity [stockname] | e: Get the latest quote for the given stock\n"
                "- calcequity [number of stocks] [stockname] | ce: Get the price of n number of stocks\n"
            )

        case "crypto" | "c":
            return (
                "Usage: \\crypto [option] | c\n"
                "Available options:\n"
                "- price [coin name] [currency] | p: Get the latest price for the given cryptocurrency\n"
                "- calc [number of coins] [coin name] [currency] | c: Calculate the price of n number of coins\n"
            )

        case _:
            return (
                "Usage: \\[command] help | h\n"
                "Available commands:\n"
                "- test: Check if the bot is working\n"
                "- stocks | s: Get stock and index commands\n"
                "- crypto | c: Get cryptocurrency commands\n"
            )

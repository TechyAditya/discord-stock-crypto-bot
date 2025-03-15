from bot.handlers.query_handler import handle_help
from bot.services.stocks import print_equity, print_index_quote


def handle_stocks(args):
    """
    Process subquery commands.
    Currently not implemented.
    """
    command = args[0].lower()

    match command:
        case "stocks":
            return "The bot is working"

        case "help":
            return handle_help("stocks")

        case "index" | "i":
            if len(args) < 2:
                return "Index name not provided. Refer '\\stocks help' for more information."

            print(args)
            indexname = " ".join(args[1:]).upper()
            print(indexname)
            try:
                return (
                    f"Index: {indexname}\n"
                    f"Last price: Rs {print_index_quote(indexname)}\n"
                )
            except Exception as e:
                return f"Error occurred: {e}"

        case "equity" | "e":
            if len(args) < 2:
                return "Equity name not provided. Refer '\\stocks help' for more information."

            print(args)
            eqname = " ".join(args[1:]).upper()
            print(eqname)
            try:
                return (
                    f"Stock: {eqname}\n"
                    f"Last price: Rs {print_equity(eqname)}\n"
                )
            except Exception as e:
                return f"Error occurred: {e}"

        case "calcequity" | "ce":
            if len(args) < 3:
                return "Equity name not provided. Refer '\\stocks help' for more information."

            print(args)
            eqname = " ".join(args[2:]).upper()
            print(eqname)
            try:
                return (
                    f"Stock: {eqname}\n"
                    f"Last price: Rs {print_equity(eqname)}\n"
                    f"Total cost: Rs {float(args[1]) * print_equity(eqname)}"
                )
            except Exception as e:
                return f"Error: {e}"

        case _:
            return handle_help("stocks")

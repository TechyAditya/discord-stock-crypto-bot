from bot.handlers.query_handler import handle_help
from bot.services.crypto import fetch_crypto_data


async def handle_crypto(args, user_handle, channel_id):
    """
    Process subquery commands.
    Currently not implemented.
    """
    command = args[0].lower() if args else None

    match command:
        case "crypto":
            return "The bot is working"

        case "help":
            return handle_help("crypto", channel_id)

        case "price" | "p":
            if len(args) < 3:
                return "Cryptocurrency name not provided. Refer '\\crypto help' for more information."

            try:
                coin = args[1].upper()
                currency = args[2].upper()
                data = await fetch_crypto_data(coin, currency)
                if data:
                    return (
                        f"Coin: {coin.upper()}\n"
                        f"Currency: {currency.upper()}\n"
                        f"Price: ${data['price']:.4f}\n"
                        f"Market Cap: {data['market_cap']}\n"
                        f"24h Change: {data['percent_change_24h']:.2f}%\n"
                    )
                else:
                    return f"Sorry {user_handle}, there was an error retrieving the data. Please check the coin and currency symbols."
            except Exception as e:
                return f"Error occurred: {e}"

        case "calc" | "c":
            if len(args) < 4:
                return "Cryptocurrency name or amount not provided. Refer '\\crypto help' for more information."

            try:
                quantity = float(args[1])
                coin = args[2].upper()
                currency = args[3].upper()
                data = await fetch_crypto_data(coin, currency)
                if data:
                    total_price = quantity * data["price"]
                    return (
                        f"Coin: {coin.upper()}\n"
                        f"Currency: {currency.upper()}\n"
                        f"Price: ${data['price']:.2f}\n"
                        f"Price of {quantity} Coins: ${total_price:.2f}\n"
                        f"Market Cap: {data['market_cap']}\n"
                        f"24h Change: {data['percent_change_24h']:.2f}%\n"
                    )
                else:
                    return f"Sorry {user_handle}, there was an error retrieving the data. Please check the coin and currency symbols."
            except Exception as e:
                return f"Error occurred: {e}"

        case _:
            return handle_help("crypto", channel_id)

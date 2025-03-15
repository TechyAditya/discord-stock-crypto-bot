import requests
from bot.utils.helper_functions import log_command, format_number
from bot.config import CMC_API_KEY


async def fetch_crypto_data(coin, currency):
    try:
        url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": CMC_API_KEY}
        parameters = {"symbol": coin.upper(), "convert": currency.upper()}
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()
        price_info = data["data"][coin.upper()]["quote"][currency.upper()]
        return {
            "price": price_info["price"],
            "market_cap": format_number(price_info["market_cap"]),
            "percent_change_24h": price_info[
                "percent_change_24h"
            ],  # Added to show 24h price change percentage
        }
    except Exception as e:
        print(f"Error fetching crypto data: {str(e)}")
        return None

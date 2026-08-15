import requests


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    response = requests.get(url)
    data = response.json()

    return data["bitcoin"]["usd"]


def check_price(price, lower_limit, upper_limit):
    if price < lower_limit:
        return "below"

    if price > upper_limit:
        return "above"

    return "normal"
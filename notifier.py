import requests

from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram settings are missing.")
        return None

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print(f"Failed to send Telegram message: {error}")
        return None


def create_alert_message(status, price, lower_limit, upper_limit):
    if status == "below":
        return (
            "Bitcoin Price Alert!!!\n\n"
            f"Current price: ${price}\n"
            f"Lower limit: ${lower_limit}\n\n"
            "Bitcoin price is below your limit."
        )

    if status == "above":
        return (
            "Bitcoin Price Alert!!!\n\n"
            f"Current price: ${price}\n"
            f"Upper limit: ${upper_limit}\n\n"
            "Bitcoin price is above your limit."
        )

    return (
        "Bitcoin Price Alert!!!\n\n"
        f"Current price: ${price}\n\n"
        "Bitcoin price is back within the limits."
    )
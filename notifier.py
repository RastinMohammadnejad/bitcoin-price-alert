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
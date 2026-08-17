import os
import requests
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")


def send_message(message):
    if not bot_token or not chat_id:
        print("Telegram settings are missing.")
        return None

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print(f"Failed to send Telegram message: {error}")
        return None
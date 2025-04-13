import requests
from django.conf import settings

def send_telegram_message(message: str):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[TG ERROR] Не удалось отправить сообщение: {e}")
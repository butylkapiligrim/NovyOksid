import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.logger import setup_logging

logger = setup_logging()


load_dotenv()
API_KEY = os.getenv("api_key")


def get_curr_rate(currency: Any) -> Any:
    """Получение курса валюты осуществляется через API, и возвращаемое значение имеет формат float."""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    try:
        response = requests.get(url, headers={"apikey": API_KEY}, timeout=5)
        response.raise_for_status()
        """Поднимает исключение, если код ответа не 2xx"""
        response_data = response.json()
        rate = response_data["rates"]["RUB"]
        return rate
    except requests.exceptions.RequestException as e:
        print(f"Ошибка API: {e}")
        """# Возвращаем 1.0 как значение по умолчанию"""
        return 1.0

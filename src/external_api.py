import os
from dotenv import load_dotenv
import requests
from requests import HTTPError

load_dotenv()

API_KEY = os.getenv("APILAYER_KEY")

headers = {
    "apikey" : API_KEY
}

def get_amount_of_transaction(transaction : dict) -> float:
    """
    Возвращает сумму транзакции в рублях.
    Если изначальная валюта USD или EUR - Переводит в рубли.
    :param transaction: Словарь, описывающий данные о транзакции
    :return: Сумма транзакции
    """
    amount = transaction.get("operationAmount", {}).get("amount", 0)
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "RUB")

    if currency== "RUB":
        return float(amount)

    elif currency in ("USD", "EUR"):


        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            resulted_currency = data.get("result")
            if resulted_currency is None:
                raise ValueError('Такого ключа нет')
            return float(resulted_currency)
        except requests.RequestException as e:
            raise HTTPError(f"Произошла ошибка при обращении к API")
    else:
        return float(amount)
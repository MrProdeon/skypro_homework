from requests import HTTPError

from src.external_api import get_amount_of_transaction

import pytest
from unittest.mock import patch, Mock
import requests

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("APILAYER_KEY")

headers = {
    "apikey" : API_KEY
}


def test_get_amount_rub():
    transacation = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }}

    assert get_amount_of_transaction(transacation) == 31957.58

def test_get_amount_usd():
    transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }}

    mock_response = Mock()
    mock_response.json.return_value = {"result" : 100.0}
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response) as mock_get:
        result = get_amount_of_transaction(transaction)
        assert result == 100.0
        mock_get.assert_called_once()

def test_get_amount_eur():
    transaction = {"operationAmount" : {"amount" : 100, "currency" : {"code" : "EUR"}}}

    mock_response = Mock()
    mock_response.json.return_value = {"result" : 100.0}
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response) as mock_get:
        result = get_amount_of_transaction(transaction)

        assert result == 100.0

def test_get_amount_result_is_none():
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "EUR"}}}

    mock_responce = Mock()
    mock_responce.json.return_value = {"none_result" : 0}

    with patch("requests.get", return_value=mock_responce) as mock_get:
        with pytest.raises(ValueError) as e:
            result = get_amount_of_transaction(transaction)
        assert str(e.value) == "Такого ключа нет"



def test_get_amount_error_403():
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "EUR"}}}

    with patch("requests.get", side_effect=requests.RequestException):
        with pytest.raises(HTTPError) as e:
            get_amount_of_transaction(transaction)

def test_unknown_currency():
       """Неизвестная валюта"""
       transaction = {
           "operationAmount": {
               "amount": "200.0",
               "currency": {"code": "CNY"}
           }
       }
       result = get_amount_of_transaction(transaction)
       assert result == 200.



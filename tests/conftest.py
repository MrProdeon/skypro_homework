# mypy: ignore-errors
import pytest


@pytest.fixture
def get_account_1():
    return "48291530670418293750"


@pytest.fixture
def get_account_2():
    return "70913428560194732016"


@pytest.fixture
def get_account_3():
    return "35678049281756019324"


@pytest.fixture
def get_card_number_1():
    return 4242424242424242


@pytest.fixture
def get_card_number_2():
    return 5555555555554444


@pytest.fixture
def get_card_number_3():
    return 3891725234553456


@pytest.fixture
def transactions_for_test():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 919739511,
            "state": "CANCELED",
            "date": "2013-02-31T02:08:58.425572",
            "operationAmount": {"amount": "9322.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142381766,
            "state": "CANCELED",
            "date": "2012-01-01T23:20:05.206878",
            "operationAmount": {"amount": "793454.93", "currency": {"name": "EURO", "code": "EURO"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708642345527258542",
            "to": "Счет 75651123456060284188",
        },
    ]

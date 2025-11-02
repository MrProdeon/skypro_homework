# mypy: ignore-errors

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions_for_test):
    testing_usd = filter_by_currency(transactions_for_test, "USD")
    assert next(testing_usd) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    testing_rub = filter_by_currency(transactions_for_test, "RUB")
    assert next(testing_rub) == {
        "id": 919739511,
        "state": "CANCELED",
        "date": "2013-02-31T02:08:58.425572",
        "operationAmount": {"amount": "9322.07", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    testing_euro = filter_by_currency(transactions_for_test, "EURO")
    assert next(testing_euro) == {
        "id": 142381766,
        "state": "CANCELED",
        "date": "2012-01-01T23:20:05.206878",
        "operationAmount": {"amount": "793454.93", "currency": {"name": "EURO", "code": "EURO"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708642345527258542",
        "to": "Счет 75651123456060284188",
    }

    testing_empty_list = filter_by_currency([], "USD")
    assert list(testing_empty_list) == []

    testing_no_currency = filter_by_currency(transactions_for_test, "BTC")
    assert list(testing_no_currency) == []

    testing_key_error = filter_by_currency([{"currency_code" : "USD"}], "USD")
    assert list(testing_key_error) == [{"currency_code" : "USD"}]


def test_descriptions(transactions_for_test):
    testins_desc = transaction_descriptions(transactions_for_test)
    assert next(testins_desc) == "Перевод организации"
    assert next(testins_desc) == "Перевод со счета на счет"

    testing_empty_list = transaction_descriptions([])
    assert list(testing_empty_list) == []


@pytest.mark.parametrize(
    "start_gen, end_gen, expected",
    [
        (
            3,
            7,
            [
                "0000 0000 0000 0000 0003",
                "0000 0000 0000 0000 0004",
                "0000 0000 0000 0000 0005",
                "0000 0000 0000 0000 0006",
                "0000 0000 0000 0000 0007",
            ],
        ),
        (
            1,
            5,
            [
                "0000 0000 0000 0000 0001",
                "0000 0000 0000 0000 0002",
                "0000 0000 0000 0000 0003",
                "0000 0000 0000 0000 0004",
                "0000 0000 0000 0000 0005",
            ],
        ),
    ],
)
def test_card_number_generator_wirh_params(start_gen, end_gen, expected):

    assert list(card_number_generator(start_gen, end_gen)) == expected
    assert list(card_number_generator(start_gen, end_gen)) == expected

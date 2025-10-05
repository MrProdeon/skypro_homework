from collections.abc import Iterable


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Iterable:
    """
    Функция для отбора транзакций по заданной валюте.
    Функция принимает список транзакций в виде списка словарей и валюту, по умолчанию USD
    Вернет итератор, в котором будут только словари, которые имеют только нужная валюта.
    Если список на входе пуст или нет подходящей валюты - генератор будет пуст, ошибки при этом
    не возникает.
    """
    filtered_transactions = (
        one_transaction
        for one_transaction in transactions
        if one_transaction["operationAmount"]["currency"]["name"] == currency
    )
    for transaction in filtered_transactions:
        yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterable:
    """
    Функция принимает список словарей из транзакций, формирует итератор из описаний
     и возвращает описание этой транзакции по одной при обращении к итератору.
    """
    descriptions = (desc["description"] for desc in transactions)

    for desc in descriptions:
        yield desc


def card_number_generator(start_gen: int, end_gen: int) -> Iterable:
    """
    Генерирует номер карты в заданном в диапазоне.
    Генерация начинается с 20 нулей и каждый раз прибавляется единица из заданного в параметрах промежутка.
    Генерация может происходить, условно, бесконечно.
    """
    for i in range(start_gen, end_gen + 1):
        resulted_card_number = []
        starting_number = i
        zfilled_number = str(starting_number).zfill(20)
        for j in range(0, len(zfilled_number), 4):
            chunk = zfilled_number[j : j + 4]
            resulted_card_number.append(chunk)

        yield " ".join(resulted_card_number)

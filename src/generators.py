from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Iterator[dict]:
    """
    Функция для отбора транзакций по заданной валюте.
    Функция принимает список транзакций в виде списка словарей и валюту, по умолчанию USD
    Вернет итератор, в котором будут только словари, которые имеют только нужная валюта.
    Если список на входе пуст или нет подходящей валюты - генератор будет пуст, ошибки при этом
    не возникает.
    """
    for one_transaction in transactions:
        try:
            code = one_transaction["operationAmount"]["currency"]["code"]
        except KeyError:
            code = one_transaction["currency_code"]
        if code == currency:
            yield one_transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Функция принимает список словарей из транзакций, формирует итератор из описаний
     и возвращает описание этой транзакции по одной при обращении к итератору.
    """
    descriptions = (desc["description"] for desc in transactions)

    for desc in descriptions:
        yield desc


def card_number_generator(start_gen: int, end_gen: int) -> Iterator[str]:
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

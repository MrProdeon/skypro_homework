def filter_by_currency(transactions : list[dict], currency : str = 'USD') -> iter :
    """
    Функция для отбора транзакций по заданной валюте.
    Функция принимает список транзакций в виде списка словарей и валюту, по умолчанию USD
    Вернет итератор, в котором будут только словари, которые имеют только нужная валюта.
    """
    filtered_transactions = (one_transaction for one_transaction in transactions
                             if one_transaction['operationAmount']['currency']['name'] == currency)

    for transaction in filtered_transactions:
        yield transaction


def transaction_descriptions(transactions : list[dict]) -> str:
    descriptions = (desc['description'] for desc in transactions)

    for desc in descriptions:
        yield desc

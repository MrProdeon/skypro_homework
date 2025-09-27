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


def card_number_generator(start_gen, end_gen):
    starting_number = 0
    for i in range(start_gen, end_gen + 1):
        resulted_card_number = []
        starting_number += 1
        zfilled_number = str(starting_number).zfill(20)
        for j in range(0, len(zfilled_number), 4):
            chunk = zfilled_number[j:j + 4]
            resulted_card_number.append(chunk)

        yield ' '.join(resulted_card_number)


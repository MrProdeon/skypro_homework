import os

import pandas as pd

from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.readers import csv_reader, excel_reader
from src.utils import get_info_about_operation
from src.widget import get_date, mask_account_card


def main() -> None:
    menu = """
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
    """

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print(menu)

    while True:
        user_answer_str = input("Ваш выбор -> ")
        try:
            user_answer = int(user_answer_str)
            if user_answer in (1, 2, 3):
                break
            else:
                print("Выберите 1, 2 или 3")
                print(menu)
        except ValueError:
            print("Выберите ЦИФРУ 1, 2 или 3")
            print(menu)

    selected_file = "JSON" if user_answer == 1 else "CSV" if user_answer == 2 else "XLSX"
    print(f"Для обработки выбран {selected_file}-файл.")

    readers = {"JSON": get_info_about_operation, "CSV": csv_reader, "XLSX": excel_reader}

    path_to_file = {
        "JSON": os.path.join(os.path.dirname(__file__), "data", "operations.json"),
        "CSV": os.path.join(os.path.dirname(__file__), "data", "transactions.csv"),
        "XLSX": os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx"),
    }
    readed_file = readers[selected_file](path_to_file[selected_file])

    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
-> """
    )
    selected_status = input()
    while selected_status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
        print(f"Статус операции {selected_status} недоступен.")
        selected_status = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
-> """
        )
    selected_status = selected_status.upper()
    transactions = filter_by_state(readed_file, state=selected_status)

    is_sorted = (
        input("Отсортировать операции по дате? (Да, если отсортировать/Любой другой ответ, если нет) ->")
        .strip()
        .lower()
        == "да"
    )
    if is_sorted:
        is_desc_sorted = input("Отсортировать по возрастанию или по убыванию?").strip().lower() == "по убыванию"
    is_only_rub_transactions = (
        input("Выводить только рублевые транзакции?(Да, если отсортировать/Любой другой ответ, если нет) ->")
        .strip()
        .lower()
        == "да"
    )
    is_sorted_by_word = (
        input(
            """Отсортировать список транзакций по определенному слову в описании?
(Да, если отсортировать/Любой другой ответ, если нет) ->"""
        )
        .strip()
        .lower()
        == "да"
    )
    if is_sorted_by_word:
        word_for_sorting = input("По какому слову в описании отфильтровать транзакции? ->")

    if is_sorted:
        transactions = sort_by_date(transactions, is_desc_sorted)
    if is_only_rub_transactions:
        transactions = list(filter_by_currency(transactions, currency="RUB"))
    if is_sorted_by_word:
        transactions = process_bank_search(transactions, word_for_sorting)

    count_transactions = len(list(transactions))
    if count_transactions == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:

        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке : {count_transactions}")

        descriptions = transaction_descriptions(transactions)

        for operation in transactions:
            formated_date = get_date(operation.get("date", ""))
            description = next(descriptions)

            masked_from_requisites = ""
            masked_to_requisites = ""

            if pd.notna(operation.get("from")) and operation.get("from"):
                masked_from_requisites = mask_account_card(operation["from"])

            if pd.notna(operation.get("to")) and operation.get("to"):
                masked_to_requisites = mask_account_card(operation["to"])

            if user_answer == 1:
                amount = operation.get("operationAmount", {}).get("amount")
                currency = operation.get("operationAmount", {}).get("currency", {}).get("name")

            else:
                amount = operation.get("amount")
                currency = operation.get("currency_name")

            if not masked_from_requisites:
                print(
                    f"""
            {formated_date} {description}
            {masked_to_requisites}
            Сумма: {amount} {currency}
            """
                )
            else:
                print(
                    f"""
            {formated_date} {description}
            {masked_from_requisites} -> {masked_to_requisites}
            Сумма: {amount} {currency}
            """
                )


main()

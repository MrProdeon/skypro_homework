import re
from collections import Counter


def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей, каждый словарь это информация о совершённой операции.
    Функция возвращает список словарей с указанным ключом в параметре state
    Если ключ state явно не указан при вызове - вернет по умолчанию
    с ключом EXECUTED
    """
    filtered_by_state_lists = [
        current_dict for current_dict in list_of_dicts if "state" in current_dict and current_dict["state"] == state
    ]

    return filtered_by_state_lists


def sort_by_date(list_of_dicts: list[dict], is_reversed: bool = True) -> list[dict]:
    """
    Функция для сортировки списка словарей, состоящего из операций по дате
    По умолчанию возвращает отсортированный по убыванию список словарей из операций.
    Чтобы изменить порядок сортировки, необходимо явно указывать при вызове аргумент is_reversed=True
    """
    sorted_by_date_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=is_reversed)

    return sorted_by_date_list


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция для поиска операций с определенным описанием.
    :param data: Список словарей, в котором каждый словарь - это отдельная операция и данные о ней
    :param search: Строка, которую мы ищем в описании операции
    :return: Список словарей, в котором есть только те операции, у которых в описании есть search
    """
    pattern = re.compile(rf"{search}", re.IGNORECASE)

    return [operation for operation in data if pattern.search(operation["description"])]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция для определения количества категорий в операциях
    :param data: Список словарей, в котором каждый словарь - это отдельная операция и данные о ней
    :param categories: Список категорий для поиска и подсчета
    :return: Словарь, в котором ключ - название категории, а значение - её количество.
    """
    found_categories = [
        category
        for operation in data
        for category in categories
        if re.search(rf"{category}", operation.get("description", ""), re.IGNORECASE)
    ]

    return dict(Counter(found_categories))

import csv
import pandas as pd
import os
import json

path = os.path.join(os.path.dirname(__file__),"..","data", "transactions_excel.xlsx")

def csv_reader(path_to_csv_file : str) -> list[dict]:
    """
    Функция для преобразования информации из csv файла в список словарей.
    :param path_to_csv_file: Путь до csv файла, содержимое которого преобразуем в список словарей
    :return: Список словарей, в котором каждый словарь - это строка из csv файла, где ключ - название столбца, а
    значение - значение ячейки в строке по этому столбцу
    """
    with open(path_to_file, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def excel_reader(path_to_excel_file : str) -> list[dict]:
    """
    Фукнция для преобразования информации из excel файла в список словарей.
    :param path_to_excel_file: Путь до excel файла, содержимое которого бреобразуем в список словарей
    :return: Список словарей, в котором каждый словарь - это строка из excel файла, где ключ - название столбца, а
    значение - значение ячейки в строке по этому столбцу
    """
    reader_dataframe = pd.read_excel(path_to_excel_file)
    return reader_dataframe.to_dict(orient="records")


print(excel_reader(r"C:\my_python_projects\study\skypro_git_homework\data\transactions_excel.xlsx"))
import json
import os
def get_info_about_operation(path_to_file : str) -> list[dict] | list:
    """
    Принимает путь до JSON-файл с операциями и возвращает Python-объект из него
    Возвращает пустой список если :
    1) Файл пустой
    2) Вернулся объект, который не является списком
    3) Файл не найден
    """

    try:
        if os.path.getsize(path_to_file) == 0:
            return []

        with open(path_to_file, 'r', encoding='UTF-8') as file:
            json_file = json.load(file)
            if not isinstance(json_file, list):
                return []

            return json_file

    except FileNotFoundError:
        return []

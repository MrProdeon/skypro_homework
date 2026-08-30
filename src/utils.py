import json
import logging
import os

log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "logs.log")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_path, "w", encoding="UTF-8")
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_info_about_operation(path_to_file: str) -> list[dict] | list:
    """
    Принимает путь до JSON-файл с операциями и возвращает Python-объект из него
    Возвращает пустой список если :
    1) Файл пустой
    2) Вернулся объект, который не является списком
    3) Файл не найден
    """
    logger.info("Начинаем преобразование")
    try:
        if os.path.getsize(path_to_file) == 0:
            logger.info("Получен пустой файл, возвращаем пустой список")
            return []

        with open(path_to_file, "r", encoding="UTF-8") as file:
            json_file = json.load(file)
            if not isinstance(json_file, list):
                logger.info("Объект не является списком, возвращаем пустой список")
                return []

            logger.info("JSON-файл был успешно преоразован в Python-объект")
            return json_file

    except FileNotFoundError:
        logger.exception("Файл не найден")
        return []

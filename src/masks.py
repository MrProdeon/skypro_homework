import logging
import os

log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "logs.log")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_path, "w", encoding="UTF-8")
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """
    Функция для маскировки номера карты. Вернет строку, в которой после четырёх символов идет пробел
     и с 7 по 12 (включительно) символ маскировка ввиде звёздочек.
    """
    logger.info("Начало маскировки номера карты")

    try:
        masked_number = str(card_number)[:6] + "******" + str(card_number)[12:]
    except Exception as e:
        logger.error(f"Произошла ошибка : {e}")

    logger.info("Номер карты замаскирован, переходим в форматированию")
    parts_of_masked_number = []
    try:
        for i in range(0, len(masked_number), 4):
            chunk = masked_number[i : i + 4]
            parts_of_masked_number.append(chunk)

        masked_number_with_spaces = " ".join(parts_of_masked_number)

        logger.info("Форматорование окончено, карта успешно замаскирована и отфарматирована")
        return masked_number_with_spaces
    except Exception as e:
        logger.exception(f"Произошла ошибка {e}")
        raise ValueError(f"Произошла ошибка {e}")


def get_mask_account(account_number: int) -> str:
    """Функция для маскировки номера счёта.
    Вернёт две звёздочки и последние 4 цифры номера счёта.
    """
    logger.info("Начало максировки номера счёта")
    masked_account_number = "**" + str(account_number)[-4:]
    logger.info("Номер счёта замасикрован")
    return masked_account_number

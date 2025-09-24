from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """
    Функция для максировки карты или счета.
    По первому слову определит счет это или карта и замаскирует функциями из модуля masks.py
    Вернет замаскированную счет или карту.
    """
    data_about_number = card_or_account_number.split()
    if data_about_number[0] == "Счет" or len(data_about_number[-1]) > 16:
        resulted_mask = f"Счет {get_mask_account(int(data_about_number[-1]))}"
    else:
        resulted_mask = (
            f"{card_or_account_number[:card_or_account_number.index(data_about_number[-1])]}"
            f"{get_mask_card_number(int(data_about_number[-1]))}"
        )
    return resulted_mask


def get_date(full_date: str) -> str:
    """
    Функция для форматорования даты. Получает абсолютно полную дату,
    а возвращает в формате ДД.ММ.ГГГГ
    """
    splited_date = full_date.split("-")
    correct_date = f"{splited_date[2][:2]}.{splited_date[1]}.{splited_date[0]}"
    return correct_date

def get_mask_card_number(card_number: int) -> str:
    """
    Функция для маскировки номера карты. Вернет строку, в которой после четырх символов идет пробел
     и с 7 по 12 (включительно) символ маскировка ввиде звёздочек.
    """
    masked_number = str(card_number)[:6] + "******" + str(card_number)[12:]
    parts_of_masked_number = []

    for i in range(0, len(masked_number), 4):
        chunk = masked_number[i : i + 4]
        parts_of_masked_number.append(chunk)

    masked_number_with_spaces = " ".join(parts_of_masked_number)

    return masked_number_with_spaces


def get_mask_account(account_number: int) -> str:
    """Функция для маскировки номера счёта.
    Вернёт две звёздочки и последние 4 цифры номера счёта.
    """
    masked_account_number = "**" + str(account_number)[-4:]

    return masked_account_number

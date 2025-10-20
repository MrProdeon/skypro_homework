# mypy: ignore-errors
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account(get_account_1, get_account_2, get_account_3):
    assert get_mask_account(get_account_1) == "**3750"

    assert get_mask_account(get_account_2) == "**2016"

    assert get_mask_account(get_account_3) == "**9324"


def test_get_mask_card_number(get_card_number_1, get_card_number_2, get_card_number_3):
    assert get_mask_card_number(get_card_number_1) == "4242 42** **** 4242"

    assert get_mask_card_number(get_card_number_2) == "5555 55** **** 4444"

    assert get_mask_card_number(get_card_number_3) == "3891 72** **** 3456"

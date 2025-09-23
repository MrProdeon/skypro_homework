from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize("card_or_account_number, expected_result", [
    ('Visa 4242424242424242', 'Visa 4242 42** **** 4242'),
    ('Счет 48291530670418293750', 'Счет **3750'),
    ('Maestro 5555555555554444', 'Maestro 5555 55** **** 4444'),
    ('Счет 70913428560194732016', 'Счет **2016')])
def test_mask_account_card(card_or_account_number, expected_result):
    mask_account_card(card_or_account_number) == expected_result

from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize("card_or_account_number, expected_result", [
    ('Visa 4242424242424242', 'Visa 4242 42** **** 4242'),
    ('Счет 48291530670418293750', 'Счет **3750'),
    ('Maestro 5555555555554444', 'Maestro 5555 55** **** 4444'),
    ('Счет 70913428560194732016', 'Счет **2016')])
def test_mask_account_card(card_or_account_number, expected_result):
    mask_account_card(card_or_account_number) == expected_result


@pytest.mark.parametrize('date, expected_formated_date', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-01-12T02:26:18.671407', '12.01.2025'),
    ('2022-05-18T02:26:18.671407', '18.05.2022')
])
def test_get_date(date, expected_formated_date):
    assert get_date(date) == expected_formated_date
from src.widget import mask_account_card, get_date
import pytest

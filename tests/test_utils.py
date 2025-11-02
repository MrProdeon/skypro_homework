# mypy: ignore-errors
import os.path
from unittest.mock import patch

from src.utils import get_info_about_operation

path = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


@patch("src.utils.json.load")
def test_get_info_correct_file(mocked_load):
    mocked_load.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        }
    ]
    result = get_info_about_operation(path)
    assert result == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        }
    ]


@patch("src.utils.json.load")
def test_get_info_not_list(mocked_load):
    mocked_load.return_value = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }
    result = get_info_about_operation(path)
    assert result == []


@patch("src.utils.open")
def test_get_info_filenotfounderror(mocked_open):
    mocked_open.side_effect = FileNotFoundError
    result = get_info_about_operation(path)
    assert result == []


@patch("src.utils.os.path.getsize")
def test_get_info_empty_size(mocked_getsize):
    mocked_getsize.return_value = 0
    result = get_info_about_operation(path)
    assert result == []


@patch("src.utils.open")
@patch("src.utils.os.path.getsize")
def test_get_info_not_empty_size_but_filenotfounderror(mocked_getsize, mocked_open):
    mocked_getsize.return_value = 5
    mocked_open.side_effect = FileNotFoundError
    result = get_info_about_operation(path)
    assert result == []

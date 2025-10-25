# mypy: ignore-errors

from unittest.mock import patch

import pandas as pd

from src.readers import csv_reader, excel_reader

import os

path_csv = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
path_excel = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")

def test_csv_reader():
    mock_data = [{"id": 1, "state": "EXECUTED", "amount": 100}]

    with patch("csv.DictReader", return_value=mock_data):
        result = csv_reader(path_csv)
        assert result == mock_data


def test_excel_reader():
    mock_data = pd.DataFrame([{"id": 1, "state": "EXECUTED", "amount": 100}])

    with patch("pandas.read_excel", return_value=mock_data):
        result = excel_reader(path_excel)
        assert result == mock_data.to_dict(orient="records")

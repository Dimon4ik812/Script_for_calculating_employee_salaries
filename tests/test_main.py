import os
import tempfile

from utils.data_utils import calculate_payout, normalize_columns
from utils.file_utils import read_csv_files


def test_read_csv_files():
    # Создаем временный CSV-файл
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write("id,name,hours_worked,rate\n")
        tmp.write("1,Alice,160,50\n")
        tmp.write("2,Bob,150,40\n")
        tmp_path = tmp.name

    try:
        data = read_csv_files(tmp_path)
        assert len(data) == 2
        assert data[0]["name"] == "Alice"
        assert data[1]["rate"] == "40"
    finally:
        os.remove(tmp_path)


def test_normalize_columns_with_hourly_rate():
    rows = [
        {
            "id": "1",
            "name": "Alice",
            "department": "IT",
            "hours_worked": "160",
            "hourly_rate": "50",
        }
    ]
    normalized = normalize_columns(rows)
    assert len(normalized) == 1
    assert normalized[0]["hourly_rate"] == 50.0


def test_normalize_columns_with_rate():
    rows = [
        {
            "id": "1",
            "name": "Bob",
            "department": "Design",
            "hours_worked": "150",
            "rate": "40",
        }
    ]
    normalized = normalize_columns(rows)
    assert len(normalized) == 1
    assert "rate" not in normalized[0]
    assert normalized[0]["hourly_rate"] == 40.0


def test_normalize_columns_with_salary():
    rows = [
        {
            "id": "1",
            "name": "Carol",
            "department": "HR",
            "hours_worked": "170",
            "salary": "60",
        }
    ]
    normalized = normalize_columns(rows)
    assert len(normalized) == 1
    assert "salary" not in normalized[0]
    assert normalized[0]["hourly_rate"] == 60.0


def test_calculate_payout():
    row = {"hours_worked": "160", "hourly_rate": 50}
    calculate_payout(row)
    assert row["payout"] == 8000


def test_calculate_payout_invalid_value():
    row = {"hours_worked": "invalid", "hourly_rate": "wrong"}
    calculate_payout(row)
    assert row["payout"] == 0

from typing import Any, Dict, List


def normalize_columns(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Нормализует названия колонок: заменяет 'hourly_rate', 'rate', 'salary' на 'hourly_rate'.
    """
    normalized_data = []
    for row in data:
        if "hourly_rate" in row:
            row["hourly_rate"] = float(row["hourly_rate"])
        elif "rate" in row:
            row["hourly_rate"] = float(row.pop("rate"))
        elif "salary" in row:
            row["hourly_rate"] = float(row.pop("salary"))
        else:
            continue  # Пропускаем, если нет подходящего поля

        # Дополнительно проверяем обязательные поля
        if not all(key in row for key in ["hours_worked", "name", "department"]):
            continue

        normalized_data.append(row)

    return normalized_data


def calculate_payout(row: Dict[str, Any]) -> None:
    """
    Вычисляет заработную плату (payout) для сотрудника.
    """
    try:
        hours_worked = int(row.get("hours_worked", 0))
        hourly_rate = float(row.get("hourly_rate", 0))
        row["payout"] = hours_worked * hourly_rate
    except (ValueError, TypeError):
        row["payout"] = 0  # Если не удалось преобразовать, ставим 0

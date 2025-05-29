from typing import Dict, List


def read_csv_files(file_path: str) -> List[Dict[str, str]]:
    """
    Читает CSV-файл и возвращает список словарей с данными.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        headers = [header.strip() for header in lines[0].split(",")]
        data = []
        for line in lines[1:]:
            # Удаляем лишние символы (например, ')') и разделяем значения
            values = [value.strip().rstrip(")") for value in line.split(",")]
            row = dict(zip(headers, values))
            data.append(row)
        return data

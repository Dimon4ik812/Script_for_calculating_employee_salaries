import argparse

from reports.payout import generate_payout_report
from utils.data_utils import calculate_payout, normalize_columns
from utils.file_utils import read_csv_files


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate reports from employee data.")
    parser.add_argument("files", nargs="+", help="CSV files containing employee data")
    parser.add_argument(
        "--report",
        choices=["payout"],
        default="payout",
        help="Type of report to generate",
    )

    args = parser.parse_args()

    # Читаем данные из всех переданных файлов

    all_data = []
    for file_path in args.files:
        print(f"Reading {file_path}...")
        data = read_csv_files(file_path)
        print(f"Found {len(data)} entries in {file_path}")
        all_data.extend(data)

    # Нормализуем названия колонок
    normalized_data = normalize_columns(all_data)

    # Вычисляем заработную плату для каждого сотрудника
    for row in normalized_data:
        calculate_payout(row)

    # Генерируем отчет
    if args.report == "payout":
        generate_payout_report(normalized_data)
    else:
        print(f"Report type '{args.report}' is not supported.")


if __name__ == "__main__":
    main()

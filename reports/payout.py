from typing import Any, Dict, List


def generate_payout_report(data: List[Dict[str, Any]]) -> None:
    """
    Формирует отчет по зарплатам, группируя данные по отделам.
    """
    departments: Dict[str, List[Dict[str, Any]]] = {}
    for row in data:
        department = row.get("department", "Unknown")
        if department not in departments:
            departments[department] = []
        departments[department].append(row)

    for department, employees in departments.items():
        print(f"\n{department}")
        print("-" * len(department))
        total_payout = 0
        for employee in employees:
            name = employee.get("name", "N/A")
            hours_worked = int(employee.get("hours_worked", 0))
            hourly_rate = float(employee.get("hourly_rate", 0))
            payout = float(employee.get("payout", 0))
            total_payout += payout
            print(f"{name:<20} {hours_worked:>8} {hourly_rate:>8.2f} ${payout:>8.2f}")
        print(f"Total Payout: ${total_payout:.2f}")

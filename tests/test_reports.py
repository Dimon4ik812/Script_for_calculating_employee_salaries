from reports.payout import generate_payout_report


def test_generate_payout_report(capsys):
    data = [
        {
            "name": "Alice Johnson",
            "department": "Marketing",
            "hours_worked": "160",
            "hourly_rate": 50,
            "payout": 8000,
        },
        {
            "name": "Henry Martin",
            "department": "Marketing",
            "hours_worked": "150",
            "hourly_rate": 35,
            "payout": 5250,
        },
        {
            "name": "Bob Smith",
            "department": "Design",
            "hours_worked": "150",
            "hourly_rate": 40,
            "payout": 6000,
        },
        {
            "name": "Carol Williams",
            "department": "Design",
            "hours_worked": "170",
            "hourly_rate": 60,
            "payout": 10200,
        },
        {
            "name": "Grace Lee",
            "department": "HR",
            "hours_worked": "160",
            "hourly_rate": 45,
            "payout": 7200,
        },
        {
            "name": "Ivy Clark",
            "department": "HR",
            "hours_worked": "158",
            "hourly_rate": 38,
            "payout": 5999,
        },
        {
            "name": "Karen White",
            "department": "Sales",
            "hours_worked": "165",
            "hourly_rate": 50,
            "payout": 8250,
        },
        {
            "name": "Mia Young",
            "department": "Sales",
            "hours_worked": "160",
            "hourly_rate": 37,
            "payout": 5920,
        },
    ]

    generate_payout_report(data)

    captured = capsys.readouterr()
    output = captured.out

    assert "Marketing" in output
    assert "Design" in output
    assert "HR" in output
    assert "Sales" in output
    assert "Total Payout: $13250.00" in output
    assert "Total Payout: $16200.00" in output
    assert "Total Payout: $13199.00" in output
    assert "Total Payout: $14170.00" in output

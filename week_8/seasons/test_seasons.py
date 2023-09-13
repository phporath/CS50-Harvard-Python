from seasons import birthdate, calculate_minutes
from datetime import date


def test_valid_date():
    try:
        birthdate("2022-06-11")
        assert True
    except ValueError:
        raise ValueError("Invalid input format.")


def test_valid_minutes():
    bd = date.fromisoformat("2020-01-01")
    today = date.today()
    result = (today - bd).days * 24 * 60
    assert calculate_minutes(bd) == result

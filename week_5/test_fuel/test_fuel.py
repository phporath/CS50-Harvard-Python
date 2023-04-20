from fuel import convert, gauge
import pytest


def main():
    test_convert_zero_div_error()
    test_convert_value_error()
    test_convert_rights()
    test_gauge_rights()
    test_gauge_limits()


def test_convert_zero_div_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("J/F")


def test_convert_rights():
    assert convert("0/5") == 0
    assert convert("4/5") == 80
    assert convert("5/5") == 100


def test_gauge_rights():
    assert gauge(0) == "E"
    assert gauge(80) == "80%"
    assert gauge(100) == "F"


def test_gauge_limits():
    assert gauge(1) != "1%"
    assert gauge(99) != "99%"


if __name__ == "__main__":
    main()

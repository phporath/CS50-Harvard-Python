from working import convert


def test_valid_time_12_hour_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_valid_time_12_hour_2():
    assert convert("09:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_valid_time_others():
    assert convert("1:00 PM to 1:00 AM") == "13:00 to 01:00"


def test_invalid_time_format_1():
    try:
        convert("9AM to 5 PM")
        assert False
    except ValueError:
        pass


def test_invalid_time_format_2():
    try:
        convert("13:00 to 5:00 PM")
        assert False
    except ValueError:
        pass


def test_invalid_time_format_3():
    try:
        convert("9:60 AM to 5:00 PM")
        assert False
    except ValueError:
        pass


def test_invalid_time_format_4():
    try:
        convert("9:00 AM 5:00 PM")
        assert False
    except ValueError:
        pass

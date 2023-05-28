from numb3rs import validate

def test_multiple_invalid_segments():
    assert validate("275.3.6.28") == False
    assert validate("192.168.256.1") == False


def test_valid_ipv4_address():
    assert validate("183.154.0.2") == True


def test_invalid_ipv4_address():
    assert validate("295.5.10.218") == False


def test_invalid_format():
    assert validate("215.170.50") == False


def test_invalid_characters():
    assert validate("192.168.0.2b") == False


def test_out_of_range():
    assert validate("256.170.0.1") == False


def test_empty_string():
    assert validate("") == False
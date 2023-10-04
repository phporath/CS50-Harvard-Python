from plates import is_valid

def test_two_letters():
    assert is_valid("cs") == True
    assert is_valid("50") == False
    assert is_valid("5C") == False
    assert is_valid("0") == False


def test_min_character():
    assert is_valid("TO") == True


def test_max_character():
    assert is_valid("cs5000") == True
    assert is_valid("CSTOPP") == True
    assert is_valid("CSTOPPP") == False


def test_number():
    assert is_valid("cs50cs") == False
    assert is_valid("cscs50") == True
    assert is_valid("csc050") == False


def test_punctuation():
    assert is_valid("TEST!") == False


if __name__ == "main":
    main()

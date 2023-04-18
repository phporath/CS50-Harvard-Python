from plates import is_valid


def main():
    test_two_letters()
    test_min_character()
    test_max_character()
    test_number_middle()
    test_zero()
    test_space()


def test_two_letters():
    assert value("cs50") == True


def test_min_character():
    assert value("cs") == True


def test_max_character():
    assert value("cs5000") == True


def test_number_middle():
    assert value("cs50cs") == False


def test_zero():
    assert value("0cs50") == False


def test_space():
    assert value("Hi, CS50") == False


if __name__ == "main":
    main()

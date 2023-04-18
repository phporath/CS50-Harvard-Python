from bank import value


def main():
    test_hello()
    test_hello_upper()
    test_h()
    test_otherwise()


def test_hello():
    assert value("hello") == 0


def test_hello_upper():
    assert value("HELLO") == 0


def test_h():
    assert value("hi") == 20


def test_h_upper():
    assert value("HI") == 20


def test_otherwise():
    assert value("bye") == 100


def test_otherwise_upper():
    assert value("BYE") == 100


if __name__ == "main":
    main()

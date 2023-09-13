from jar import Jar


def test_default_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_init():
    jar = Jar(8)
    assert jar.capacity == 8
    assert jar.size == 0


def test_invalid_init():
    try:
        Jar(-5)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_str_deposit():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4


def test_deposit_full_capacity():
    try:
        jar = Jar()
        jar.deposit(15)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1


def test_withdraw_capacity():
    try:
        jar = Jar(5)
        jar.withdraw(10)
        assert False, "Expected ValueError"
    except ValueError:
        pass

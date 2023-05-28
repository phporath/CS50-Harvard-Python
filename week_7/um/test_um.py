from um import count


def test_count_occurrence_0():
    assert count("yummy") == 0


def test_count_occurrence_1():
    assert count("hello, um, world") == 1


def test_count_occurrence_multiple():
    assert count("um, um, um, um") == 4


def test_count_case_insensitive():
    assert count("Um, uM, UM") == 3


def test_count_occurrence_0_with_no_um():
    assert count("document") == 0

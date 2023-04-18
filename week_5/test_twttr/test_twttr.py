from twttr import shorten


def main():
    test_twttr_lower_without_vowel()
    test_twttr_upper_with_vowel()
    test_twttr_lower_with_vowel()


def test_twttr_lower_without_vowel():
    assert shorten("pdf") == "pdf"


def test_twttr_upper_with_vowel():
    assert shorten("PETER") == "PTR"


def test_twttr_lower_with_vowel():
    assert shorten("peter") == "ptr"


def test_twttr_numbers():
    assert shorten("peter8") == "ptr8"


def test_twttr_ponctuation():
    assert shorten("peter.") == "ptr."


if __name__ == "__main__":
    main()

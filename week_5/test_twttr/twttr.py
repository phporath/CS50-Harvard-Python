def main():
    phrase = input("Input: ")
    new_phrase = shorten(phrase)
    print(new_phrase)


def shorten(word):
    wrd = ""
    for x in word:
        if vogals(x) is True:
            wrd = wrd
        else:
            wrd = wrd + x
    return wrd


def vogals(a):
    list = ["A", "E", "I", "O", "U"]
    if a.upper() in list:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

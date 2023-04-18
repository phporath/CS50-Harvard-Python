def main():
    phrase = input('Input: ')
    new_phrase = nw_phrs(phrase)
    print(new_phrase)


def nw_phrs(old_phrase):
    new = ''
    for x in old_phrase:
        if vogals(x) is True:
            new = new
        else:
            new = new + x
    return new


def vogals(a):
    list = ['A', 'E', 'I', 'O', 'U']
    if a.upper() in list:
        return True
    else:
        return False


main()
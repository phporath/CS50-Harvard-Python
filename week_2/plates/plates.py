def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):

    if rule_one(s) is False:
        return False

    if rule_two(s) is False:
        return False

    if rule_three(s) is False:
        return False

    if rule_four(s) is False:
        return False
    
    return True


def rule_one(string):
    for c in string[:2]:
        if c.isalpha() is True:
            continue
        else:
            return False
    return True


def rule_two(string):
    if 2 <= len(string) <= 6:
        return True
    else:
        return False


def rule_three(string):
    previous = ''
    for c in string:
        if c == '0' and previous == '':
            return False
        if c.isnumeric() is True:
            previous = 'number'
        else:
            if previous == 'number':
                return False
    return True


def rule_four(string):
    list = [',', '.', ':', ';', '!', '?', ' ']
    for c in string:
        if c in list:
            return False
    return True


main()
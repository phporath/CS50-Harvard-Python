def main():
    question = input('What is the awnsear to the Great Question of Life, the Universe, and Everything? ')
    awnsear = find_awnsear(question)
    print(awnsear)


def find_awnsear(x):
    new_x = x.lower().strip()
    match new_x:
        case '42' | 'forty-two' | 'forty two':
            return 'Yes'
        case _:
            return 'No'

main()
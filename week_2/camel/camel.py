def main():
    camel = input('camelCase: ')
    snake = snake_case(camel)
    print(f'snake_case: {snake}')


def snake_case(name):
    new_name = ''
    for n in name:
        if n.isupper() == False:
            new_name = new_name + n
        else:
            new_name = new_name + '_' + n.lower()
    return new_name

main()
def main():
    question = input('Greeting: ')
    awnsear = greating(question)
    print(awnsear)


def greating(x):
    new_x = x.lower().strip()
    if new_x.startswith('hello'):
        return '$0'
    elif new_x.startswith('h'):
        return '$20'
    else:
        return '$100'
        

main()
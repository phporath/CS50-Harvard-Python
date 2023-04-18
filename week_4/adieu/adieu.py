import inflect


def main():
    adieu("Name: ")


def adieu(prompt):
    names = []
    while True:
        try:
            name = input(prompt)
            names.append(name)
        except EOFError:
            p = inflect.engine()
            mylist = p.join(names)
            print(f"\nAdieu, adieu, to {mylist}")
            break


main()

def main():
    dic_menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    item(dic_menu, "item: ")


def item(menu, prompt):
    total = 0
    while True:
        try:
            item = menu[input(prompt).title()]
            total += item
            print(f"${total:.2f}")

        except KeyError:
            pass

        except EOFError:
            break


main()

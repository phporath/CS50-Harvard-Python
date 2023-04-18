def main():
    item_list('')


def item_list(prompt):
    d = {}
    while True:
        try:
            item = input(prompt).upper()

            if item not in d.keys():
                d[item] = 1
            else:
                d[item] += 1
        except EOFError:
            d_list = list(d.keys())
            d_list.sort()
            for i in d_list:
                print(f'{d[i]} {i}')
            break


main()
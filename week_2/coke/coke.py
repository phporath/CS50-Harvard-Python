def main():
    coke = 50
    v_coin = insert_coin(coke)


def insert_coin(total):
    rest = total
    owed = 0
    while owed < total:
        print(f'Amount Due: {rest}')
        coin = int(input('Insert Coin: '))
        if accepted_coins(coin) is True:
            rest -= coin
            owed += coin
        else:
            print('coin is not accepable')
        change_owed = owed - total
    return print(f'Change Owed: {change_owed}')


def accepted_coins(x):
    list = [25, 10, 5]
    if x in list:
        return True
    else:
        return False


main()
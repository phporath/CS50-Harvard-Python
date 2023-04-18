def main():
    interpreter = input('Expression: ').split()
    calc = expression(interpreter)
    print('%.1f' % calc)

def expression(values):

    x = int(values[0])
    y = values[1]
    z = int(values [2])

    match y:
        case '+':
            return x + z
        case '-':
            return x - z
        case '*':
            return x * z
        case '/':
            return x / z

main()
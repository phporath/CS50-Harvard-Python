# define Python user-defined exceptions
class InvalidXValue(Exception):
    "x > y"
    pass


def main():
    teste = input("Fraction: ")
    fr = convert(teste)
    gg = gauge(fr)
    print(gg)


def convert(fraction):
    while True:
        try:
            list = fraction.split("/")
            x = int(list[0])
            y = int(list[1])
            n = round((x / y) * 100)
            if x > y:
                raise InvalidXValue
        except InvalidXValue:
            pass
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
        return n


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage < 99:
        return f"{percentage}%"
    else:
        return "F"


if __name__ == "__main__":
    main()

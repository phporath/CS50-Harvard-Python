# define Python user-defined exceptions
class InvalidXValue(Exception):
    "x > y"
    pass


def main():
    fraction = get_int("Fraction: ")
    print(fuel_gauge(fraction))


def get_int(prompt):
    while True:
        try:
            list = input(prompt).split("/")
            x = int(list[0])
            y = int(list[1])
            n = round((x / y) * 100)
            if x > y:
                raise InvalidXValue
        except InvalidXValue:
            pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return n


def fuel_gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage < 99:
        return f"{percentage}%"
    else:
        return "F"


main()

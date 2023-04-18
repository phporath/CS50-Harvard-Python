import random


def main():
    lv = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(lv)
        y = generate_integer(lv)
        correct_answer = x + y
        tries = 0

        while True:
            answer = input(f"{x} + {y} = ")
            if int(answer) == correct_answer:
                score += 1
                break
            elif not answer.isdigit():
                print("EEE")
            else:
                tries += 1
                if tries < 3:
                    print("EEE")
                else:
                    print(f"{x} + {y} = {x + y}")
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                raise ValueError
            return n
        except ValueError:
            print("Invalid input number. You should use 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level number. You should use 1, 2, or 3.")


if __name__ == "__main__":
    main()

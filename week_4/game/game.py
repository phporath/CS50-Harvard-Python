import random
import sys


def main():
    lv = level("Level: ")
    gs = guess(lv, "Guess: ")
    print(gs)


def level(prompt):
    nu_level = 0
    while nu_level <= 0:
        try:
            nu_level = int(input(prompt))
        except ValueError:
            continue
    rd = random.randint(1, nu_level)
    return rd


def guess(rd_value, prompt):
    nu_guess = 0
    while nu_guess != rd_value:
        try:
            nu_guess = int(input(prompt))

            if nu_guess < rd_value:
                print("Too small!")
            elif nu_guess > rd_value:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except EOFError:
            break
        except ValueError:
            continue


main()

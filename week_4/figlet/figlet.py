import sys
import random
from pyfiglet import Figlet

def main():

    figlet = Figlet()
    len_argv = len(sys.argv)

    if len_argv == 1:
        pass

    elif len_argv == 3:
        invalidArg1(sys.argv[1])
        invalidArg2(sys.argv[2], figlet)

    else:
        sys.exit('you should give 0 or 2 arguments')

    inp_figlet = input("Input: ")
    print(translate_figlet(figlet, len_argv, inp_figlet))


def translate_figlet(f, l, phrase):
    if l == 1:
        rd = random.choice(f.getFonts())
        f.setFont(font=rd)

    elif l == 3:
        f.setFont(font=sys.argv[2])

    return f"Output: {f.renderText(phrase)}"


def invalidArg1(x):
    list = ['-f', '--font']
    if x not in list:
        sys.exit('you should use -f or --font as second argument')


def invalidArg2(x, f):
    fonts = f.getFonts()
    if x not in fonts:
        sys.exit('you should write a valid font')

main()
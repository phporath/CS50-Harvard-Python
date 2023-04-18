import emoji


def main():
    inp_emoji = input("Input: ")
    print(translate_emoji(inp_emoji))


def translate_emoji(phrase):
    translate = emoji.emojize(phrase)
    return f"Output: {translate}"


main()

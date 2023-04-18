def main():
    test = input()
    new = convert(test)
    print(new)

def convert(emoticon):
    emoji = emoticon.replace(":)", '🙂')
    emoji2 = emoji.replace(":(", "🙁")
    return emoji2

main()
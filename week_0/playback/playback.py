def main():
    test = input("Write a phrase in: ")
    new = playback(test)
    print(new)

def playback(phrase):
    new_phrase = phrase.replace(' ', '...')
    return new_phrase

main()
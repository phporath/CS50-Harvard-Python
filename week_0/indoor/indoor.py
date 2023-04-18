def main():
    test = input("Write a phrase in: ")
    new = lowercase(test)
    print(new)

def lowercase(phrase):
    new_phrase = phrase.lower()
    return new_phrase

main()
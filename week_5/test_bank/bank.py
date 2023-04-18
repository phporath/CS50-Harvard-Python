def main():
    question = input("Greeting: ")
    awnsear = value(question)
    print(f"${awnsear}")


def value(greating):
    new_x = greating.lower().strip()
    if new_x.startswith("hello"):
        return 0
    elif new_x.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

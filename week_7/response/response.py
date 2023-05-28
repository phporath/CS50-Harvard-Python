import validators


def main():
    print(validate_email(input("What's your email adress? ")))


def validate_email(s):
    validate = validators.email(s)
    if validate == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()

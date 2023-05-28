import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"  # The small letter \b word boundary indicates that a pattern is bounded by a non-word character.
    value = re.findall(pattern, s, flags=re.IGNORECASE) # return a list
    print(value)
    return len(value)


if __name__ == "__main__":
    main()

from datetime import date
import re
import sys
import inflect


def main():
    bd = birthdate(input("Date of Birth: "))
    bd_iso = calculate_minutes(bd)
    print_minutes(bd_iso)


def birthdate(st_birth):
    pattern = r"^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])$"
    matches = re.search(pattern, st_birth)

    if matches:
        dt_iso = date.fromisoformat(st_birth)
        return dt_iso
    else:
        sys.exit("Invalid input format.")


def calculate_minutes(iso_birth):
    today = date.today()
    minutes = (today - iso_birth).days * 24 * 60
    return minutes


def print_minutes(dif_min):
    p = inflect.engine()
    words = p.number_to_words(dif_min).replace(" and ", " ").capitalize()
    print(f"{words} minutes")


if __name__ == "__main__":
    main()

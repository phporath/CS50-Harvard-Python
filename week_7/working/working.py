import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = (r"(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s*to\s*(\d{1,2})(?::(\d{2}))?\s+(AM|PM)")
    matches = re.search(pattern, s)

    if matches:
        start_hour = int(matches.group(1))
        start_minute = matches.group(2) or "00"
        start_period = matches.group(3)

        end_hour = int(matches.group(4))
        end_minute = matches.group(5) or "00"
        end_period = matches.group(6)

        if int(start_minute) == 60:
            raise ValueError("Invalid input format.")

        if int(end_minute) == 60:
            raise ValueError("Invalid input format.")

        if start_hour == 12 and start_period == "AM":
            start_hour = 0
        elif start_hour < 12 and start_period == "PM":
            start_hour += 12

        if end_hour == 12 and end_period == "AM":
            end_hour = 0
        elif end_hour < 12 and end_period == "PM":
            end_hour += 12

        return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"

    else:
        raise ValueError("Invalid input format.")


if __name__ == "__main__":
    main()

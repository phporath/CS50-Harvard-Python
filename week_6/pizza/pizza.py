import sys
import os
import csv
from tabulate import tabulate


def main():
    len_argv = len(sys.argv)

    if len_argv == 1:
        sys.exit("Too few command-line arguments")
    elif len_argv == 2:
        filename = sys.argv[1]
        if not filename.endswith(".csv"):
            sys.exit("Not a CSV file")
        table = create_tabulate(filename)
        print(table)
    elif len_argv > 2:
        sys.exit("Too many command-line arguments")


def create_tabulate(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            file_tabulate = tabulate(rows, headers="firstrow", tablefmt="grid")

        return file_tabulate
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

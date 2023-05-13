import sys
import os
import wget
import csv
from tabulate import tabulate


def main():
    len_argv = len(sys.argv)

    if len_argv == 1:
        sys.exit("Too few command-line arguments")
    elif len_argv == 2:
        csv = sys.argv[1]
        download_wget_csv(csv)
        table = create_tabulate(csv)
        print(f'\n')
        print(table)
    elif len_argv > 2:
        sys.exit("Too many command-line arguments")


def download_wget_csv(file_name):
    if file_name == 'sicilian.csv':
        url = 'https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv'
    elif file_name == 'regular.csv':
        url = 'https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv'
    elif file_name[-3:] != '.csv':
        sys.exit('Not a CSV file')
    else:
        sys.exit('File does not exist')

    dir_name = os.path.dirname(__file__)
    file_path = dir_name + '/' + file_name

    if os.path.exists(file_path):
        os.remove(file_path)

    filename = wget.download(url)

    return filename


def create_tabulate(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            #header = next(reader)
            #file_tabulate = tabulate(reader, header, tablefmt='grid')
            file_tabulate = tabulate(rows, headers='firstrow', tablefmt='grid')

        return file_tabulate
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()

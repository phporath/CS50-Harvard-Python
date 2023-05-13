import sys
import csv


def main():
    len_argv = len(sys.argv)

    if len_argv <= 2:
        sys.exit("Too few command-line arguments")

    elif len_argv == 3:
        file_before = sys.argv[1]
        file_after = sys.argv[2]
        create_new_csv(file_before, file_after)

    elif len_argv > 3:
        sys.exit("Too many command-line arguments")


def create_new_csv(fb, fa):
    try:
        with open(fb, "r") as orig_file:
            reader = csv.DictReader(orig_file)
            with open(fa, "w", newline="") as new_file:
                writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    split_name = row["name"].split(",")
                    first = split_name[1].strip()
                    last = split_name[0].strip()
                    writer.writerow(
                        {"first": first, "last": last, "house": row["house"]}
                    )
    except FileNotFoundError:
        sys.exit(f'Could not read {fb}')


if __name__ == "__main__":
    main()

import sys


def main():
    len_argv = len(sys.argv)

    if len_argv == 1:
        sys.exit("Too few command-line arguments")

    elif len_argv == 2:
        invalidArg1(sys.argv[1])
        cl = count_lines(sys.argv[1])
        print(cl)

    elif len_argv > 2:
        sys.exit("Too many command-line arguments")


def count_lines(py_file):
    try:
        with open(py_file, "r") as file:
            lines = file.readlines()

        line_counter = 0

        for line in lines:
            line = line.strip()

            if not line:  # to skip blank lines
                continue

            if not line.startswith("#"):
                line_counter += 1

        return line_counter

    except FileNotFoundError as e:
        sys.exit("File does not exist")


def invalidArg1(py_file):
    check_ext = py_file[-3:]
    if check_ext != ".py":
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()

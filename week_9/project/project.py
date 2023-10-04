import pandas as pd


def main():
    csv_file = input("Insert the name of csv's input: ")
    df = read_csv_file(csv_file)
    df["gms_latitude"] = ""
    df["gms_longitude"] = ""

    for row in df.index:
        new_lat = coordinate_calc(df["latitude"][row], "latitude")
        new_long = coordinate_calc(df["longitude"][row], "longitude")

        df.loc[row, "gms_latitude"] = new_lat
        df.loc[row, "gms_longitude"] = new_long

    output_csv = print_csv(df)


def read_csv_file(file):
    df = pd.read_csv(file, skiprows=0)
    df.columns = ["id", "latitude", "longitude"]

    return df


def coordinate_calc(coordinate, type):
    try:
        coord = float(coordinate)
        degree = int(abs(coord))
        minute = int((abs(coord) - degree) * 60)
        second = (((abs(coord) - degree) * 60) - minute) * 60

        gms = coordinate_gms(coord, degree, minute, second, type)
    except ValueError:
        raise ValueError(f"Value from coordinates is not a number. Coordinate = {coordinate}")

    return gms


def coordinate_gms(coordinate, degree, minute, second, type):
    str_deg = check_number(degree)
    str_min = check_number(minute)
    str_sec = check_number(round(second, 4))

    dms_temp = f"{str_deg}°{str_min}'{str_sec}"

    if coordinate >= 0 and type == "latitude":
        dms = f'{dms_temp}N'
    elif coordinate >= 0 and type == "longitude":
        dms = f'{dms_temp}E'
    elif coordinate < 0 and type == "latitude":
        dms = f'{dms_temp}S'
    elif coordinate < 0 and type == "longitude":
        dms = f'{dms_temp}W'

    return dms


def check_number(number):
    if number >= 10:
        return str(number)
    else:
        return f"0{str(number)}"


def print_csv(df):
    output = input("Insert the name of csv's output: ")
    df.to_csv(output, index=False)

    return f"File {output} was created."


if __name__ == "__main__":
    main()

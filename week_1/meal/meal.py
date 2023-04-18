def main():
    string_time = input('What time is it? ')
    number_time = convert(string_time)
    meal = meal_time(number_time)
    print(meal)


def convert(s_time):
    hours, minutes = s_time.split(':')
    f_minutes = int(minutes)/60
    f_time = float(hours)+ f_minutes
    return f_time


def meal_time(f_time):
    if 7 <= f_time <= 8:
        return 'breakfast time'
    elif 12 <= f_time <= 13:
        return 'lunch time'
    elif 18 <= f_time <= 19:
        return 'dinner time'


if __name__ == "__main__":
    main()
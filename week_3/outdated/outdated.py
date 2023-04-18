# define Python user-defined exceptions
class InvalidDay(Exception):
    "int(day) > 31"
    pass

class InvalidMonth(Exception):
    "int(month) > 12"
    pass

class InvalidSeparator(Exception):
    "sep in ['/', ',']"
    pass

def main():

    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

    new_date('Date: ', month_list)

def new_date(prompt, m_l):
    while True:
        try:
            input_list = input(prompt)

            if input_list.find('/') >= 0:
                date = type_one(input_list)
            elif input_list.find(',') >= 0:
                date = type_two(input_list, m_l)
            else:
                raise InvalidSeparator

            print(f'{date[0]}-{date[1]}-{date[2]}')
            break

        except InvalidMonth:
            pass
        except InvalidDay:
            pass
        except InvalidSeparator:
            pass
        except ValueError:
            pass
        except EOFError:
            break

def type_one(i_list):
    date_list = i_list.replace(' ','').split('/')
    year = date_list[2]
    month = int(date_list[0])
    day = date_list[1]

    new = validation_month_day(month, day)
    n_month = new[0]
    n_day = new[1]

    return year, n_month, n_day


def type_two(i_list, m_list):
    date_list = i_list.split(',')
    year = date_list[1]
    month_day = date_list[0].split(' ')
    if month_day[0] in m_list:
        month = m_list.index(month_day[0]) + 1
    day = int(month_day[1])

    new = validation_month_day(month, day)
    n_month = new[0]
    n_day = new[1]

    return year, n_month, n_day


def validation_month_day(m, d):
    if int(m) < 10:
        m = f'0{m}'
    elif int(m) > 12:
        raise InvalidMonth

    if int(d) < 10:
        d = f'0{d}'
    elif int(d) > 31:
        raise InvalidDay

    return m, d

main()


from datetime import datetime


def format_date(day, month, year):
    day = int(day)
    month = int(month)
    if 1 <= month <= 12:
        m = (1, 3, 5, 7, 8, 10, 12)
        if (month in m and 0 < day <= 31) or (month not in m and 0 < day <= 30):
            if month == 2 and 1 < day > 28:
                return
            else:
                return datetime(year, month, day).strftime("%d %B %y")
        else:
            return
    else:
        return


print(format_date(29, 10, 2022))

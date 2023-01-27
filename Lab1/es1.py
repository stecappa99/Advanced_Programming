# This is a sample Python script.
import calendar
import datetime


def next_leap(year):
    """Restituisce il prossimo anno bisestile"""
    return year if calendar.isleap(year) else next_leap(year+1)


def count_leap_years(start_year, end_year):
    """Restituisce il numero di anni bisestili in un range di anni"""
    print(calendar.leapdays(start_year, end_year))


if __name__ == '__main__':
    print(next_leap(datetime.datetime.now().year))
    count_leap_years(2000, 2050)
    print(calendar.day_name[calendar.weekday(2016, 7, 29)])

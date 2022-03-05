from calendar import month

def is_leap(year):
    """This function will be used to check if a year is aleap year or not.
    Created by Dan Isaaka
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if year < 1:
        return "Invalid Year."
    if month > 12 or month < 1:
        return "Invalid month:"    

    month_days = [31,28,31,30,31,30,31,31,30,31,30,30]

    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

year = int(input("Enter Year:\n"))
month =int(input("Enter Month:\n"))
days = days_in_month(year,month)

print(days)

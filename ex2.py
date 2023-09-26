# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку

import sys
import argparse

# date_str = input('Enter date in DD.MM.YYYY: ')

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        
        days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day < 1 or day > days_in_month[month - 1]:
            return False
        return True
    except ValueError:
        return False

def main():
    parser = argparse.ArgumentParser(description="Checking date in format DD.MM.YYYY.")
    parser.add_argument("date", help="Date for checking DD.MM.YYYY")
    args = parser.parse_args()
    date_str = args.date
    if is_valid_date(date_str):
        print(f"{date_str} - correct date")
    else:
        print(f"{date_str} - error date")

if __name__ == "__main__":
    main()
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) 
# действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

date_str = input('Enter date in DD.MM.YYYY: ')

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

if __name__ == "__main__":
    if is_valid_date(date_str):
        print(f"{date_str} - correct date")
    else:
        print(f"{date_str} - error date")

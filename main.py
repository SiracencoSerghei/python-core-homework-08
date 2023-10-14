"""main"""
from datetime import date, datetime, timedelta

def update_birthday(birthday: datetime, current_date: date) -> datetime:
    """update birthday year"""
    # Порівнюємо рік дня народження з поточним роком
    is_birthday_month = birthday.month < current_date.month
    is_birthday_day = (birthday.month == current_date.month and birthday.day < current_date.day)
    if is_birthday_month or is_birthday_day:
        # Якщо день народження вже минув у поточному році, збільшуємо рік на 1
        birthday = birthday.replace(year=current_date.year + 1)
    else:
        # Інакше залишаємо рік без змін
        birthday = birthday.replace(year=current_date.year)
    return birthday

def calc_current_period(current_date):
    """calculate current period of week"""
    current_date_index = current_date.weekday()
    if current_date_index == 0:
        start_period = current_date - timedelta(2)
        end_period = current_date +timedelta(4)
    elif current_date_index >0:
        start_period = current_date
        end_period = current_date + timedelta(6)
    return start_period, end_period

def get_birthdays_per_week(users):
    """main function"""
    # Реалізуйте тут домашнє завдання
    # Створення порожнього словника для зберігання інформації про дні народження
    birthdays = {}
    # Поточна дата
    current_date = date.today()
    start_period, end_period = calc_current_period(current_date)
    users_to_congratulate = []
    for user in users:
        birthday = update_birthday(user['birthday'], current_date)
        if start_period <= birthday <= end_period:
            users_to_congratulate.append(user)
    if not users_to_congratulate:
        print('No users to congratulate')
        return {}
    for user in users_to_congratulate:
        current_birthday = update_birthday(user['birthday'], current_date)
        day_of_the_week = current_birthday.strftime('%A')
        if day_of_the_week in ('Saturday','Sunday'):
            day_of_the_week = 'Monday'
        birthdays[day_of_the_week] = birthdays.get(day_of_the_week, [])
        birthdays[day_of_the_week].append(user['name'])
    return birthdays

if __name__ == "__main__":
    users_list = [
    {"name": "Bill Gates", "birthday": date(1955, 10, 28)},
    {"name": "Elon Musk", "birthday": date(1971, 6, 28)},
    {"name": "Mark Zuckerberg", "birthday": date(1984, 5, 14)},
    {"name": "Warren Buffett", "birthday": date(1930, 8, 30)},
    {"name": "Oprah Winfrey", "birthday": date(1954, 1, 29)},
    {"name": "Jeff Bezos", "birthday": date(1964, 1, 12)},
    {"name": "Steve Jobs", "birthday": date(1955, 2, 24)},
    {"name": "Larry Page", "birthday": date(1973, 3, 26)},
    {"name": "Sergey Brin", "birthday": date(1973, 8, 21)},
    {"name": "Larry Ellison", "birthday": date(1944, 8, 17)},
    {"name": "Larry Ellison", "birthday": date(1957, 10, 28)},
    {"name": "Bill Clinton", "birthday": date(1946, 8, 19)},
    {"name": "George W. Bush", "birthday": date(1946, 7, 6)},
    {"name": "Barack Obama", "birthday": date(1961, 8, 4)},
    {"name": "Donald Trump", "birthday": date(1946, 6, 14)},
    {"name": "User for October 1", "birthday": date(2000, 10, 1)},
    {"name": "User for October 2", "birthday": date(2000, 10, 2)},
    {"name": "User for October 3", "birthday": date(2000, 10, 3)},
    {"name": "User for October 4", "birthday": date(2000, 10, 4)},
    {"name": "User for October 5", "birthday": date(2000, 10, 5)},
    {"name": "User for October 6", "birthday": date(2000, 10, 6)},
    {"name": "User for October 7", "birthday": date(2000, 10, 7)},
    {"name": "User for October 8", "birthday": date(2000, 10, 8)},
    {"name": "User for October 9", "birthday": date(2000, 10, 9)},
    {"name": "User for October 10", "birthday": date(2000, 10, 10)},
    {"name": "User for October 11", "birthday": date(2000, 10, 11)},
    {"name": "User for October 12", "birthday": date(2000, 10, 12)},
    {"name": "User for October 13", "birthday": date(2000, 10, 13)},
    {"name": "User for October 14", "birthday": date(2000, 10, 14)},
    {"name": "User for October 15", "birthday": date(2000, 10, 15)},
    {"name": "User for October 16", "birthday": date(2000, 10, 16)},
    {"name": "User for October 17", "birthday": date(2000, 10, 17)},
    {"name": "User for October 18", "birthday": date(2000, 10, 18)},
    {"name": "User for October 19", "birthday": date(2000, 10, 19)},
    {"name": "User for October 20", "birthday": date(2000, 10, 20)},
    {"name": "User for October 21", "birthday": date(2000, 10, 21)},
    {"name": "User for October 22", "birthday": date(2000, 10, 22)},
    {"name": "User for October 23", "birthday": date(2000, 10, 23)},
    {"name": "User for October 24", "birthday": date(2000, 10, 24)},
    {"name": "User for October 25", "birthday": date(2000, 10, 25)},
    {"name": "User for October 26", "birthday": date(2000, 10, 26)},
    {"name": "User for October 27", "birthday": date(2000, 10, 27)},
    {"name": "User for October 28", "birthday": date(2000, 10, 28)},
    {"name": "User for October 29", "birthday": date(2000, 10, 29)},
    {"name": "User for October 30", "birthday": date(2000, 10, 30)},
    {"name": "User for October 31", "birthday": date(2000, 10, 31)}
    ]

    result = get_birthdays_per_week(users_list)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

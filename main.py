from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    
    # Поточна дата
    current_date = date.today()
    # Знайдемо день тижня для поточної дати (0 - понеділок, 6 - неділя) і рік
    current_weekday = current_date.weekday()
    current_year = current_date.year
    print(f'current_date: {current_date}')
    print(f'current_weekday: {current_weekday}')
    
    # Якщо поточний день - понеділок, включаємо попередню суботу і неділю
    if current_weekday == 0:
        start_date = current_date - timedelta(days=current_weekday + 2)
        
        # Знайдемо дату на тиждень вперед плюс 2 дня що додали в start_date
        end_date = start_date + timedelta(days=7 + 2)
    else:
        start_date = current_date
        # Знайдемо дату на тиждень вперед
        end_date = start_date + timedelta(days=7)
        
    # Знайдемо користувачів, чиї дні народження входять в цей діапазон
    users_with_upcoming_birthdays = []
    print(f'start_date: {start_date}')
    print(f'end_date: {end_date}')
    for user in users:
        birthday = user["birthday"]
        upcoming_birthday = birthday.replace(year=current_year)
        print(f'birthday: {birthday}')
        if start_date <= upcoming_birthday <= end_date:
            print(f'user: {user}')
            users_with_upcoming_birthdays.append(user)
    print(users_with_upcoming_birthdays)
    
     # Виводимо результат
    for user in users_with_upcoming_birthdays:
        print(f"Name: {user['name']}, Birthday: {user['birthday']}")
        
    # return users_with_upcoming_birthdays




# if __name__ == "__main__":
#     users = [
#         {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
#     ]

#     result = get_birthdays_per_week(users)
#     print(result)
    # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {', '.join(names)}")

#============================================================


if __name__ == "__main__":
    
    users = [
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


    result = get_birthdays_per_week(users)

    # # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {', '.join(names)}")
        
        
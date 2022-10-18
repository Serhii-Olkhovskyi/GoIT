from datetime import datetime, timedelta
import calendar

users = [
    {"name": 'Jim', "birthday": datetime(year=1982, month=10, day=1)},
    {"name": 'JANET', "birthday": datetime(year=1981, month=10, day=3)},
    {"name": 'VALERIYA', "birthday": datetime(year=1980, month=10, day=8)},
    {"name": 'ADELINA', "birthday": datetime(year=1980, month=10, day=8)},
    {"name": 'MIKAS', "birthday": datetime(year=1977, month=10, day=23)},
    {"name": 'Sergi', "birthday": datetime(year=1980, month=10, day=24)},
    {"name": 'Oleg', "birthday": datetime(year=1990, month=10, day=26)},
    {"name": 'Ann', "birthday": datetime(year=1982, month=10, day=26)},
    {"name": 'Karen', "birthday": datetime(year=1988, month=10, day=27)},
    {"name": 'LEO', "birthday": datetime(year=1980, month=10, day=29)},
    {"name": 'Dmitriy', "birthday": datetime(year=1985, month=10, day=30)},
    {"name": 'Marina', "birthday": datetime(year=1985, month=10, day=31)},
    {"name": 'Danila', "birthday": datetime(year=1985, month=11, day=1)},
    {"name": 'Leonardo', "birthday": datetime(year=1985, month=11, day=2)},
    {"name": 'VADIM', "birthday": datetime(year=1975, month=11, day=3)}
]

res_dict = {"Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": []}


#  функция определяет сегод.дату
def current_date():
    current_date_def = datetime.today().date()
    return current_date_def


#  функция определяет интервал дат в зависимости от дня недели
def define_timedelta(today):
    if today.weekday() == 5:
        res_timedelta = timedelta(days=6)
    elif today.weekday() == 6:
        res_timedelta = timedelta(days=5)
    else:
        res_timedelta = timedelta(days=7)
    return res_timedelta


def get_birthdays_per_week(users_data):
    today = current_date()  # Определяем сегодняшнюю дату
    # today = datetime(year=2022, month=10, day=25).date()
    days_interval = define_timedelta(today)
    new_data = today + days_interval

    for user in users_data:
        if new_data >= new_birthday(user["birthday"]) >= today:
            weak = weak_birthday(new_birthday(user["birthday"]))
            weak = week_replacement(weak)
            res_dict[weak].append(user['name'])

    out_resault(res_dict)


#  функция создает дату ДР на сегод.год
def new_birthday(data):
    new_data = datetime(year=current_date().year, month=data.month, day=data.day).date()
    return new_data


# функция выводит результат
def out_resault(data):
    for key, value in data.items():
        if value:
            print(f"{key}: {', '.join(value)}")


#  функция определяет в какой день недели ДР
def weak_birthday(data):
    birthday_weak = calendar.day_name[data.weekday()]
    return birthday_weak


#  функция меняет выходные дни недели на понедельник
def week_replacement(data):
    if data == 'Saturday' or data == 'Sunday':
        data = 'Monday'
    return data


if __name__ == '__main__':
    get_birthdays_per_week(users)

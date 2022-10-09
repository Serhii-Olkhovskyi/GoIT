from datetime import datetime, timedelta
import calendar
from pprint import pprint

users = [
    {'MIKAS': '1 November 1980'},
    {'VALERIYA': '1 November 1980'},
    {'ADELINA': '30 October 1980'},
    {'JANET': '28 October 1980'},
    {'LEO': '26 October 1980'},
    {'Sergi': '25 October 1980'},
    {'Karen': '24 October 1980'},
    {'Oleg': '23 October 1982'},
    {'Ann': '23 October 1982'},
    {'Jim': '22 October 1980'},
    {'Dmitriy': '17 October 1982'},
    {'VADIM': '15 October 1982'},
]

rez_dict = {

}

pprint(users)


def get_birthdays_per_week(users):

    def dict_calendar(weak, name):  # Заполняем словарь имениннками
        rez_dict.setdefault(weak, [])
        rez_dict[weak].append(name)

    # current_date = datetime.today().date()  # Определяем сегодняшнюю дату
    current_date = datetime(year=2022, month=10, day=24).date()
    print('------------------------------')
    print(f'Сегодня дата: {current_date}')
    print('------------------------------')
    current_weak = current_date.isoweekday()  # Определяем сегод день недели
    day_delta = current_weak + 1
    day_start = current_date - timedelta(
        days=day_delta)  # Определяем число с которого будем начинать выводить именниников
    day_stop = day_start + timedelta(days=6)  # Определяем число до которого будем выводить именниников

    if current_weak == 6 or current_weak == 7:
        print('Запустите программу в рабочий день.')
    else:
        for elem in users:
            for key, value in elem.items():
                birthday_data = datetime.strptime(value, '%d %B %Y').date()  # формируем из str дату
                new_data = datetime(year=current_date.year, month=birthday_data.month, day=birthday_data.day).date()
                # определяем какие др попадают на эту неделю и прошлые выходные
                if day_start <= new_data <= day_stop:
                    if new_data.weekday() == 5 or new_data.weekday() == 6:
                        a = 0
                        a = calendar.day_name[a]
                        dict_calendar(a, key)
                    else:
                        a = calendar.day_name[new_data.weekday()]
                        dict_calendar(a, key)

    for key, value in rez_dict.items():  # Выводим результат
        print(key, ':', value)


if __name__ == '__main__':
    get_birthdays_per_week(users)

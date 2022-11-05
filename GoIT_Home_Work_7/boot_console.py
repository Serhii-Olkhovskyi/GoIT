import os
import pickle
import sys
from datetime import datetime
from boot_class import AddressBook, Name, Phone, Record, Birthday, address_book
from manual import all_commands

input_user = []
if os.path.exists('dump.pickle'):
    with open('dump.pickle', 'rb') as file:
        address_book = pickle.load(file)

else:
    address_book = AddressBook()


def input_error(func):
    """
    Декоратор для обработки возникших ошибок из-за некорректного ввода данных пользователем.

    Параметры
    ---------
    :param func: Функция ввода от пользователя.
    :return: Вывод результата функции ввода или вывод ошибки с повторным вводом данных
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This name doesn't exist"
        except TypeError:
            return "Wrong command type"
        except IndexError:
            return "Input name and phone number"
        except ValueError:
            return "This name already exist"

    return wrapper


@input_error
def add_birthday():
    """
    Функция добавляет день рождения контакта.
    :return:
    """
    key_message = 2
    name = Name(input_user[1])
    birthday_data = date_formation(input_user[2])
    if check_for_name(name) and Birthday.correct_data(birthday_data):
        contact_search(key_message, name, birthday_data).add_birthday(birthday_data)
        return message()
    return message(name.value, key_message=0)


@input_error
def add_contact():
    """
    Функция добавляет в адресную книгу введенное имя контакта с большой буквы и его номер телефона.
    :return:
    """
    name = Name(input_user[1])
    phone_num = Phone(input_user[2:])
    record = Record(name, phone_num)
    if not address_book.add_record(record):
        return f'contact with {name.value}and phone number: {phone_num.value} ' \
               f'not added to address book'
    print(f'contact with {name.value} and phone number: {phone_num.value} added to address book')
    return message()


@input_error
def add_phone():
    """
    Функция добавляет к существующему контакту еще один номер телефона.
    :return:
    """
    key_message = 1
    name, new_number, input_number = obj_name_phone(input_user)
    if check_for_name(name) and Phone.correct_number(input_number):
        contact_search(key_message, name, new_number).add_phone(new_number)
        return message()
    return message(name.value, key_message=0)


def contact_search(key, name, number):
    """
    Функция ищет контакт, с которым в дальнейшем необходимо будет произвести действия.
    :return: contact
    """
    for contact in address_book.values():
        if name.value == contact.name.value:
            return contact
    return message(number.value, key)


@input_error
def change_phone():
    """
    Функция замены номера телефона существующего контакта.
    :return:
    """
    key_message = 3
    name, old_number, new_number, input_number = obj_name_phone(input_user)
    if check_for_name(name) and Phone.correct_number(input_number):
        contact_search(key_message, name, old_number.value).change(old_number, new_number)
        return message()
    return message(name.value, key_message=0)


def check_for_name(name):
    """
    Функция проверяет есть ли имя в адресной книге.
    :param: name - имя контакта вводимое пользователем
    :return: True or False
    """
    for users in address_book.values():
        if users.name.value == name.value:
            return True
    return False


def date_formation(data):
    """
    Функция формирует вводимую дату пользователем,
    в дату необходимого формата(формат datetime) для дальнейшей работы.
    :return: входящая дата
    """
    year_data, month_data, day_data = parsing_birthday(data)
    contact_birthday = datetime(year=int(year_data), month=int(month_data), day=int(day_data))
    contact_birthday = datetime.date(contact_birthday)
    return contact_birthday


@input_error
def dell_phone():
    """
    Функция удаляет номер телефона у контакта.
    :return:
    """
    key_message = 3
    name, dell_number, input_number = obj_name_phone(input_user)
    if check_for_name(name) and Phone.correct_number(input_number):
        contact_search(key_message, name, dell_number.value).remove(dell_number)
        return message()
    return message(name.value, key_message=0)


def message(inline_value=None, key_message=None):
    """
    Функция выводит строковое результирующее сообщение
    :return: строка.
    """
    if key_message == 0:
        return f'No name {inline_value}'
    elif key_message == 1:
        return f'phone number {inline_value} not added'
    elif key_message == 2:
        return f'Birthday {inline_value} not added'
    elif key_message == 3:
        return f'phone number {inline_value} not removed'
    print('...')
    return 'Completed! Enter new command.'


@input_error
def func_show_all():
    """
    Функция выводит всю адресную книгу.
    :return:
    """

    for users in address_book.values():
        print(users)
    return message()


@input_error
def func_show_birthday():
    """
    Функция выводит количество дней до следующего дня рождения контакта.
    :return:
    """
    name = obj_name_phone(input_user)
    if check_for_name(name):
        for contact in address_book.values():
            if name.value == contact.name.value:
                days_to_birthday = contact.days_to_birthday(contact.birthday.value)
                print(f'Number of days until {name.value} birthday: {days_to_birthday}')
                return message()
    return message(name.value, key_message=0)


def good_bye(func):
    """
    Декоратор который прощается с клиентом
    :return: Good bye!
    """

    def print_quit():
        print('Good bye!')
        func()

    return print_quit


def hello():
    """
    Функция приветствия.
    :return: How can I help you?
    """
    return "How can I help you?"


def main():
    """
    Основная функция для запуска программы.
    :return:
    """
    global input_user

    CONSOLE_COMMANDS = {
        'add': add_contact,
        'add_phone': add_phone,
        'add_birthday': add_birthday,
        'dell_phone': dell_phone,
        'change': change_phone,
        'phone': show_phone,
        'show_all': func_show_all,
        'show_birthday': func_show_birthday,
        'show_page': page,
        'search': search_matches,
        'hello': hello,
        'close': quit_func_handler,
        'exit': quit_func_handler,
        'good_bye': quit_func_handler,
        'help': all_commands
    }

    while True:
        print('-' * 20)
        print('Тo display all commands on the screen type: help')
        input_user = input('input command: ')
        print('-' * 20)
        input_user = parsing_input(input_user)
        if input_user[0] not in CONSOLE_COMMANDS:
            print('Wrong commands: ')
            continue
        print(CONSOLE_COMMANDS[input_user[0]]())


def obj_name_phone(user_input):
    """
    Функция принимает ввод пользователя и возвращает имя и номер телефона
    как объект в зависимости от условия.
    :return: name, phone, old_phone
    """
    if len(user_input) == 1:
        return user_input
    if len(user_input) == 2:
        name = user_input[1]
        return Name(name)
    if len(user_input) == 3:
        name = user_input[1]
        phone = user_input[2]
        return Name(name), Phone(phone), phone
    if len(user_input) == 4:
        name, old_phone, phone = user_input[1:]
        return Name(name), Phone(old_phone), Phone(phone), phone
    return 'Incorrect data entered. Use the help command'


def output_loop(page_book, number):
    """
    Функция показывает контакты частями.
    :param: page_book - адресная книга. Number - число контактов которое выводится на экран
    :return: выводит адресную книгу частями
    """
    for _ in range(int(number)):
        print(next(page_book))


def page():
    """
    Функция показывает контакты частями.
    :return: выводит адресную книгу частями
    """
    input_page = obj_name_phone(input_user)
    pages = address_book.iterator()

    while True:
        try:
            output_loop(pages, input_page.value)
            show_next = input(f'Show {input_page.value} contacts? (y/n)')
            if show_next == 'y':
                continue
            if show_next == 'n':
                break
        except StopIteration:
            print('Address book completed')
            break
    return message()


def parsing_birthday(data):
    """
    Функция разбивает по точкам консольный ввод пользователя и записывает его в list data_birthday[]
    :return: Возвращает list data_birthday[]:
            data_birthday[0] - год в формате YYYY
            data_birthday[1] - месяц в формате MM
            data_birthday[2] - день в формате DD
    """
    data_birthday = data.split('.')
    return data_birthday


def parsing_input(input_elem):
    """
    Функция разбивает по пробелам консольный ввод пользователя и записывает его в list user_input[]
    :return: Возвращает list user_input[]:
            user_input[0] - команда для выполнения нужных действий
            user_input[1] - имя контакта
            user_input[2] - номер телефона (не обязательный аргумент)
            user_input[3] - дата рождения (не обязательный аргумент)
    """
    user_input = input_elem.split()
    if len(user_input) == 1:
        user_input[0] = user_input[0].lower()
        return user_input
    user_input[1] = user_input[1].capitalize()
    return user_input


def search_matches():
    """
    Функция ищет совпадения по введенным данным
    :return:
    """
    text = input_user[1]
    resault = []
    for user in address_book.values():
        if text in user.name.value:
            resault.append(user)
        if text in user.phones.value:
            resault.append(user)
    if len(resault) == 0:
        print('No matches')
        return message()
    for i in resault:
        print(i)
    return message()


@input_error
def show_phone():
    """
    Функция поиска номера по имени.
    :return:
    """
    name = obj_name_phone(input_user)
    if check_for_name(name):
        for contact in address_book.values():
            if name.value == contact.name.value:
                print(f'Name: {name.value} Phone: {contact.phones.value}')
                return message()
    return message(name.value, key_message=0)


@good_bye
def quit_func_handler():
    """
    Функция сохраняет адресную книгу и завершает программу.
    :return:
    """
    with open('dump.pickle', 'wb') as dump_file:
        pickle.dump(address_book, dump_file)

    sys.exit()


if __name__ == '__main__':
    main()

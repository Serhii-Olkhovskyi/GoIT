from datetime import datetime
from boot_class import Record
from boot_decorator import input_error
from boot_help import all_commands
from boot_load_save import save_address_book, address_book

input_user = []


@input_error
def add_birthday():
    """
    Функция добавляет день рождения контакта.

    Параметры
    ---------
    :param:
    :return:
    """

    name, data = parsing_name_phone(input_user)
    birthday_data = date_formation(data)
    if not search_by_name(name):
        return message(name, key_message=0)
    record = address_book[name]
    record.add_birthday(birthday_data)
    return message()


@input_error
def add_contact():
    """
    Функция добавляет в адресную книгу введенное имя контакта с большой буквы и его номер телефона.

    Параметры
    ---------
    :param:
    :return str: Возвращает сообщение о результате функции.
    """

    name, phone_num = parsing_name_phone(input_user)

    if search_by_name(name):
        raise ValueError(f'Contact {name} already exist')

    record = Record(name)
    address_book.add_record(record)
    record.phone_add(phone_num)

    print(f'contact with {name} and phone number: {phone_num} added to address book')
    return message()


@input_error
def add_phone():
    """
    Функция добавляет к существующему контакту еще один номер телефона.

    Параметры
    ---------
    :param:
    :return:
    """

    name, new_number = parsing_name_phone(input_user)

    if not search_by_name(name):
        return message(name, key_message=0)
    record = address_book[name]
    record.phone_add(new_number)
    return message()


# def contact_search(key, name, number):
#     """
#     Функция ищет контакт, с которым в дальнейшем необходимо будет произвести действия.

#     Параметры
#     ---------
#     :param:
#     :return: contact
#     """

#     for contact in address_book.values():
#         if name.value == contact.name.value:
#             return contact
#     return message(number.value, key)


# @input_error
def change_phone():
    """
    Функция замены номера телефона существующего контакта.

    Параметры
    ---------
    :param:
    :return:
    """

    # key_message = 3

    name, old_number, new_number = parsing_name_phone(input_user)
    if not search_by_name(name):
        return message(name.value, key_message=0)

    record = address_book[name]
    record.phone_remove(old_number)
    record.phone_add(new_number)
    return message()


def date_formation(data):
    """
    Функция формирует вводимую дату пользователем, в дату необходимого формата(формат datetime)

    для дальнейшей работы.

    Параметры
    ---------
    :param:
    :return: входящая дата
    """

    print(f'data: {data}')
    year_data, month_data, day_data = parsing_birthday(data)
    contact_birthday = datetime(year=int(year_data), month=int(month_data), day=int(day_data))
    contact_birthday = datetime.date(contact_birthday)
    return contact_birthday


@input_error
def dell_phone():
    """
    Функция удаляет номер телефона у контакта.

    Параметры
    ---------
    :param:
    :return:
    """

    # key_message = 3
    name, dell_number = parsing_name_phone(input_user)

    if not search_by_name(name):
        return message(name, key_message=0)

    record = address_book[name]
    record.phone_remove(dell_number)

    return message()


def message(inline_value=None, key_message=None):
    """
    Функция выводит строковое результирующее сообщение

    Параметры
    ---------
    :param:
    :return str:
    """

    if key_message == 0:
        raise ValueError(f'No name {inline_value}')
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

    Параметры
    ---------
    :param:
    :return:
    """

    show_table_header()
    for users in address_book.values():
        print(users.get_user_details, )

    return message()


@input_error
def func_show_birthday():
    """
    Функция выводит количество дней до следующего дня рождения контакта.

    Параметры
    ---------
    :param:
    :return:
    """

    name = parsing_name_phone(input_user)

    if not search_by_name(name):
        return message(name.value, key_message=0)

    record = address_book[name]
    print(f'{name} birthday will be in {record.days_to_birthday()} days')
    return message()


def hello():
    """
    Функция приветствия.

    Параметры
    ---------
    :param:
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
        'close': save_address_book,
        'exit': save_address_book,
        'good_bye': save_address_book,
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


def parsing_name_phone(user_input):
    """
    Функция принимает ввод user и return имя и номер телефона в зависимости от условия.

    Параметры
    ---------
    :param: user input
    :return: name, phone, old_phone
    """

    if len(user_input) == 1:
        return user_input
    if len(user_input) == 2:
        name = user_input[1]
        return name
    if len(user_input) == 3:
        name = user_input[1]
        phone = user_input[2]
        return name, phone
    if len(user_input) == 4:
        name, old_phone, phone = user_input[1:]
        return name, old_phone, phone
    return 'Incorrect data entered. Use the help command'


def output_loop(book, number):
    """
    Функция печатает контакты блоком из кол-ва number.

    Параметры
    ---------
    :param: page_book - адресная книга. number - число контактов которое выводится на экран.
    :return: выводит адресную книгу частями
    """

    for _ in range(int(number)):
        print(next(iter(book)))


# @input_error
def page():
    """
    Функция показывает контакты частями.

    Параметры
    ---------
    :param:
    :return: выводит адресную книгу частями
    """

    input_page = parsing_name_phone(input_user)
    pages = address_book.iterator()

    while True:
        try:
            show_more = input(f'Show {input_page} contacts? (y/n): ')
            show_table_header()
            if show_more == 'y':
                output_loop(pages, input_page)
            if show_more == 'n':
                break
        except StopIteration:
            print('')
            print('Book is over')
            break

    return message()


def parsing_birthday(data):
    """
    Функция разбивает по точкам консольный ввод пользователя и записывает его в list data_birthday[]

    Параметры
    ---------
    :param data: input data
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

    Параметры
    ---------
    :param: str - user input
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


def search_by_name(name):
    """
    Функция проверяет есть ли имя в адресной книге.

    Параметры
    ---------
    :param: name - имя контакта вводимое пользователем
    :return: True or False
    """

    if name in address_book:
        return True
    return False


@input_error
def search_matches():
    """
    Функция проверяет адресную книгу на совпадения с введенными данными.

    Параметры
    ---------
    :param:
    :return:
    """


    match_list = []
    element = parsing_name_phone(input_user)

    if element.isalpha() or element.isalnum():
        if search_by_name(element):
            record = address_book[element]
            match_list.append(record.get_user_details)

    for elem in element:
        if elem == '.':
            a = 'its data'
            match_list.append(a)
            break





    # print(f'address_book: {address_book.values()}')
    #
    # for user in address_book.values():
    #
    #     print(f'user.phones: {user.phones}')
        # match_list.append(user)

    if match_list:
        show_table_header()
        for i in match_list:
            print(i)
        return message()
    else:
        print(match_list)
        return message(element, key_message=0)


@input_error
def show_phone():
    """
    Функция поиска номера по имени.

    Параметры
    ---------
    :param:
    :return str: Возвращает сообщение о результате функции.
    """

    name = parsing_name_phone(input_user)

    if not search_by_name(name):
        return message(name.value, key_message=0)

    record = address_book[name]

    show_table_header()
    print(record.get_user_details)
    return message()


def show_table_header():
    """
    Функция печатает шапку таблицы.

    Параметры
    ---------
    :param:
    :return:
    """

    print(f"{'Name':^10} | {'Birthday':^15} | {'Phone':^20}")
    print('-' * 55)


if __name__ == '__main__':
    main()

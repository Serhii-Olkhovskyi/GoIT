import os
import pickle
import sys
from boot_class import AddressBook

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

    def wrapper(*args, **kwags):
        try:
            return func(*args, **kwags)
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
def add():
    """
    Функция добавляет в адресную книгу введенное имя контакта с большой буквы и его номер телефона.
    :return:
    """
    name = input_user[1]
    phone_num = find_phone(input_user)
    name.capitalize()
    address_book.add_record(name, phone_num)
    return 'Completed! Enter new command.'


@input_error
def change():
    """
    Функция замены номера телефона существующего контакта.
    :return:
    """

    name = input_user[1]
    phone_number = input_user[2]
    if name in address_book:
        address_book.change(name, phone_number)
        return f'Contact changed. Enter new command.'
    return f'No contact found in address book.'


def find_phone(list_input):
    """
    Функция определяет ввел ли пользователь номер телефона.
    :return: возвращает номер телефона
    """

    if len(list_input) < 3:
        return None
    return list_input[2]


@input_error
def func_show_all():
    """
    Функция выводит всю адресную книгу.
    :return:
    """

    for key, value in address_book.items():
        print(key, ':', value)
    return 'Completed! Enter new command.'


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
        'add': add,
        'change': change,
        'close': quit_func_hendler,
        'exit': quit_func_hendler,
        'good_bye': quit_func_hendler,
        'hello': hello,
        'phone': phone,
        'show_all': func_show_all
    }

    while True:
        print('-' * 20)
        input_user = input('input command: ')
        print('-' * 20)
        input_user = parsing_input(input_user)
        if input_user[0] not in CONSOLE_COMMANDS:
            print('Wrong commands: ')
            continue
        print(CONSOLE_COMMANDS[input_user[0]]())


def parsing_input(input_elem):
    """
    Функция разбивает по пробелам консольный ввод пользователя и записывает его в list user_input[]
    :return: Возвращает list user_input[]:
            user_input[0] - команда для выполнения нужных действий
            user_input[1] - имя контакта
            user_input[2] - номер телефона (не обязательный аргумент)
            user_input[3] - дата рождения (не обязательный аргумент)
    """
    # Разбиваем по пробелам ввод пользователя
    user_input = input_elem.split()
    user_input[0] = user_input[0].lower()
    return user_input


@input_error
def phone():
    """
    Функция поиска номера по имени.
    :return:
    """
    name = input_user[1]
    address_book.find_number(name)
    return 'Completed! Enter new command.'


@good_bye
def quit_func_hendler():
    """
    Функция сохраняет адресную книгу и завершает программу.
    :return:
    """
    with open('dump.pickle', 'wb') as dump_file:
        pickle.dump(address_book, dump_file)

    sys.exit()


if __name__ == '__main__':
    main()

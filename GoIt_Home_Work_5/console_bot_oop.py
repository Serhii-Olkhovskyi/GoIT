from class_boot_oop import *

address_book = AddressBook()
input_list = []


def input_error(func):
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
    name = input_list[1]
    phone_num = find_phone(input_list)
    name.capitalize()
    address_book.add_record(name, phone_num)
    return 'ok'


@input_error
def change():
    name = input_list[1]
    old_number = input_list[2]
    new_number = input_list[-1]
    address_book.data[name].update_phone(old_number, new_number)
    return 'ok'


def find_phone(list_input):
    if len(list_input) < 3:
        return None
    else:
        return list_input[-1]


@input_error
def func_show_all(): # Вывод всей адресной книги

    for key, value in address_book.items():
        print(key, ':', value)

    # return address_book


def good_bye(func):
    def print_quit():
        print('Good bye!')
        func()

    return print_quit


def hello():
    return "How can I help you?"


def main():
    global input_list
    while True:
        input_user = input('input command: ')
        input_list = parsing_input(input_user)
        if input_list[0] not in CONSOLE_COMMANDS:
            print('Wrong commands: ')
            continue
        else:
            print(CONSOLE_COMMANDS[input_list[0]]())


def parsing_input(input_elem):  # Разбиваем по пробелам ввод пользователя
    user_input = input_elem.split()
    user_input[0] = user_input[0].lower()
    return user_input


@input_error
def phone(): # Поиск номера по имени
    name = input_list[1]
    address_book.find_number(name)



@good_bye
def quit_func():
    quit()


CONSOLE_COMMANDS = {
    'add': add,
    'change': change,
    'close': quit_func,
    'exit': quit_func,
    'good_bye': quit_func,
    'hello': hello,
    'phone': phone,
    'show_all': func_show_all
}

if __name__ == '__main__':
    main()

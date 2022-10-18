address_book = {
    'name': 'phone',
    '------': '-------',
    'Sergii': '+380978141867'
}

input_list = []


def input_error(func):
    def wrapper(*args, **kwags):
        try:
            resault = func(*args, **kwags)
        except Exception as e:
            print('Input Error. Enter once again.')
        return resault

    return wrapper


@input_error
def add():
    name = input_list[1].capitalize()
    address_book[name] = input_list[-1]
    return 'ok'


@input_error
def func_show_all():
    for key, value in address_book.items():
        print('{:^15}:{:^20}'.format(key, value))
    return 'ok'


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
def phone():
    for key, value in address_book.items():
        if key.lower() == input_list[1].lower():
            return value


def run_command(command):
    return CONSOLE_COMMANDS[command]


@good_bye
def quit_func():
    quit()


CONSOLE_COMMANDS = {
    'add': add,
    'change': add,
    'close': quit_func,
    'exit': quit_func,
    'good_bye': quit_func,
    'hello': hello,
    'phone': phone,
    'show_all': func_show_all
}

if __name__ == '__main__':
    main()

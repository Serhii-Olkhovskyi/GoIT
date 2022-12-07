def good_bye(func):
    """
    Декоратор который прощается с клиентом.

    Параметры
    ---------
    :param func: Функция ввода от пользователя.
    :return: Good bye!
    """

    def print_quit():
        print('Good bye!')
        func()

    return print_quit


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
        except ValueError as exception:
            return exception.args[0]

    return wrapper

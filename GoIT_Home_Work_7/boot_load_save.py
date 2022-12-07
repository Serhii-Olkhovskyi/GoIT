"""
Были импортированы следующие модули:

    os: позволяет запускать команду в скрипте Python, как если бы я запускал ее в своей оболочке.
    pickle: Используем pickle.dump и pickle.load - сериализации и десериализации структуры объекта
    (сохранения и загрузки).
    sys: Используем  sys.exit() - метод заставляет интерпретатор
    внезапно завершать текущий поток выполнения.
    AddressBook: Используется для создания address_book ели нет сохраненной книги.
    good_bye: Используется для вывода сообщения "good bye" при завершении работы файла.
"""
import os
import pickle
import sys
from boot_class import AddressBook
from boot_decorator import good_bye


def load_address_book():
    """
    Функция загружает адресную книгу при старте.

    Параметры
    ---------
    :param:
    :return:
    """

    if os.path.exists('dump.pickle'):
        with open('dump.pickle', 'rb') as file:
            address_book = pickle.load(file)
            return address_book

    else:
        address_book = AddressBook()
        return address_book


address_book = load_address_book()


@good_bye
def save_address_book():
    """
    Функция сохраняет адресную книгу и завершает программу.

    Параметры
    ---------
    :param:
    :return:
    """

    with open('dump.pickle', 'wb') as dump_file:
        pickle.dump(address_book, dump_file)

    sys.exit()

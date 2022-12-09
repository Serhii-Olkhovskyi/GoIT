"""
В модуле разработаны следующие классы:
    AddressBook - который наследуется от UserDict, и добавлена логика поиска по записям.
    Field - родительский для всех полей.
    Name - имя контакта. Класс Name, обязательное поле с именем
    Phone - телефонный номер. Класс Phone, необязательное поле с телефоном
    Birthday - день рождения. Класс Birthday, необязательное поле с датой
    Record - отвечает за логику добавления/удаления/редактирования необязательных полей
    и хранения обязательного поля Name
"""

import pickle
import sys
from collections import UserDict
from datetime import datetime
from boot_decorator import good_bye


class AddressBook(UserDict):
    """
    Класс AddressBook, который наследуется от UserDict, и добавлена логика поиска по записям

    Параметры
    ---------
    :param:
    :return:
    """

    def address_book_load(self):
        """
        Функция загружает адресную книгу при старте.

        Параметры
        ---------
        :param:
        :return:
        """

        with open('dump.pickle', 'rb') as dump_file:
            archive_book = pickle.load(dump_file)
            return archive_book

    def address_book_save(self, archive_book):
        """
        Функция сохраняет адресную книгу и завершает программу.

        Параметры
        ---------
        :param:
        :return:
        """

        with open('dump.pickle', 'wb') as dump_file:
            pickle.dump(archive_book, dump_file)

        sys.exit()

    def add_record(self, record):
        """
        Добавление контакта в адресную книгу

        Параметры
        ---------
        :param:
        :return:
        """

        self.data[record.name.value] = record

    def find_input(self, value):
        """
         Функция ищет совпадения по имени / части имени

         или по номеру телефона / части номера телефона
         и выводит все совпадения

         Параметры
         ---------
         :param: value - искомое значение.
         :return: find_list_class - лист со всеми совпадениями по запросу.
         """

        find_list_class = []

        for name in self.data:
            if value in name:
                find_list_class.append(self.find_name(name))
        if find_list_class:
            return find_list_class

        for record in self.data.values():
            for phone in record.phones:
                if value in phone.value:
                    find_list_class.append(record)
        if find_list_class:
            return find_list_class

        raise ValueError('No matches found')

    def find_name(self, name):
        """
          Возвращает запись с искомым именем.

          Параметры
          ---------
          :param: name - искомое имя
          :return:
          """

        return self.data.get(name)

    def iterator(self):
        """
        Пагинация (постраничный вывод)

        Параметры
        ---------
        :param: int: entry - кол-во записей за раз
        :return:
        """

        for record in self.data.values():
            yield record


class Field:  # pylint: disable=too-few-public-methods
    """
    Класс Field, который будет родительским для всех полей

    Параметры
    ---------
    :param:
    :return:
    """

    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        """
        pass

        Параметры
        ---------
        :param:
        :return:
        """

        return self._value

    @value.setter
    def value(self, value):
        """
        pass

        Параметры
        ---------
        :param:
        :return:
        """

        self._value = value


class Name(Field):  # pylint: disable=too-few-public-methods
    """
    Создаем класс для имени контакта. Класс Name, обязательное поле с именем.

    Параметры
    ---------
    :param:
    :return:
    """


class Phone(Field):  # pylint: disable=too-few-public-methods
    """
    Создаем класс для телефонного номера. Класс Phone, необязательное поле с телефоном

    Параметры
    ---------
    :param:
    :return:
    """

    @Field.value.setter
    def value(self, value):
        """
        Метод проверяет правильно ли ввел пользователь номер телефона

        Параметры
        ---------
        :param:
        :return:
        """

        if not value[1:].isnumeric():
            raise ValueError('Wrong phones.')

        if len(value) == 10 or len(value) == 13:
            self._value = value
        else:
            raise ValueError('Phone must be 10 or 13 characters')


class Birthday(Field):  # pylint: disable=too-few-public-methods
    """
    Создаем класс для дня рождения. Класс Birthday, необязательное поле с датой

    Параметры
    ---------
    :param:
    :return:
    """

    @Field.value.setter
    def value(self, value):
        """
        Метод проверяет правильно ли ввел пользователь день рождения

        Параметры
        ---------
        :param:
        :return:
        """

        if value > datetime.date(datetime.today()):
            raise ValueError(f'Date entered incorrectly: {value}')
        self._value = value


class Record:
    """
    Класс отвечает за логику добавления/удаления/редактирования полей и хранения поля Name.

    Параметры
    ---------
    :param:
    :return:
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, day):
        """
        Метод для добавления объектов Birthday

        Параметры
        ---------
        :param:
        :return:
        """

        self.birthday = Birthday(day)

    def change(self, old_number, new_number):
        """
        Метод для редактирования объектов Phone

        Параметры
        ---------
        :param:
        :return:
        """

        self.phone_remove(old_number)
        self.phone_add(new_number)

    def days_to_birthday(self):
        """
        Метод высчитывает количество дней до следующего дня рождения.

        Параметры
        ---------
        :param:
        :return:
        """

        if self.birthday is None:
            return 'Date of birth missing'

        today = datetime.today()
        date_object = datetime(year=today.year, month=self.birthday.value.month, day=self.birthday.value.day + 1)
        difference = date_object - today

        if int(difference.days) > 0:
            return difference.days
        return 365 + int(difference.days)

    def find_phone(self, element):
        """
        Метод для поиска совпадений по номерам телефонов

        Параметры
        ---------
        :param: str: element - искомый номер телефона
        :return:
        """

        for phone in self.phones:
            if phone.value == element:
                return phone
        raise ValueError(f'No matches {element}')

    @property
    def get_user_details(self):
        """
        Метод преобразует phones и дату в строку

        Параметры
        ---------
        :param:
        :return: str phone
        """

        show_phone = ''
        show_birthday = ''

        for phone in self.phones:
            show_phone += f"{phone.value}  "
        if self.birthday is None:
            show_birthday = ''
        else:
            show_birthday += f'{self.birthday.value}'

        return f'{self.name.value:<10} | {show_birthday:^15} | {show_phone:<20}'

    def phone_add(self, number):
        """
        Метод для добавления записи в phones.

        Параметры
        ---------
        :param:
        :return:
        """

        self.phones.append(Phone(number))

    def phone_remove(self, number):
        """
        Метод для удаления записи в phones

        Параметры
        ---------
        :param:
        :return:
        """

        phone = self.find_phone(number)
        self.phones.remove(phone)

    def __str__(self):
        return self.get_user_details


address_book = AddressBook()

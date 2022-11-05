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
from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    """
    Класс AddressBook, который наследуется от UserDict, и добавлена логика поиска по записям
    """

    def add_record(self, record):
        """
        Добавление контакта в адресную книгу
        """
        self.data[record.name.value] = record
        return True

    def iterator(self):
        """
        Пагинация (постраничный вывод)
        """
        for record in self.data.values():
            yield record


class Field:  # pylint: disable=too-few-public-methods
    """
    Класс Field, который будет родительским для всех полей
    """

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        """
        pass
        """
        return self.__value

    @value.setter
    def value(self, new_value):
        """
        pass
        """
        self.__value = new_value


class Name(Field):  # pylint: disable=too-few-public-methods
    """
    Создаем класс для имени контакта. Класс Name, обязательное поле с именем.
    """

    def __init__(self, value):
        super().__init__(value)
        self.value = value


class Phone(Field):  # pylint: disable=too-few-public-methods
    """
    Создаем класс для телефонного номера. Класс Phone, необязательное поле с телефоном
    """

    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @staticmethod
    def correct_number(phone_number):
        """
        Метод проверяет правильно ли ввел пользователь номер телефона
        """
        if len(phone_number) == 10 or len(phone_number) == 13:
            return phone_number
        print('Phone must be 10 or 13 characters')
        return False


class Birthday(Field):  # pylint: disable=too-few-public-methods
    """
    Создаем класс для дня рождения. Класс Birthday, необязательное поле с датой
    """

    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @staticmethod
    def correct_data(data):
        """
        Метод проверяет правильно ли ввел пользователь день рождения
        """
        if data < datetime.date(datetime.today()):
            return True
        print(f'Date entered incorrectly: {data}')
        return False


class Record:
    """
    Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей
    и хранения обязательного поля Name.
    """

    def __init__(self, name, phones=None, birthday=None):
        self.name = name
        self.phones = phones
        self.birthday = birthday
        self.difference = None

    def add_birthday(self, day):
        """
        Метод для добавления объектов Birthday
        """
        if self.birthday is None:
            self.birthday = Birthday(day)
            return True
        return False

    def add_phone(self, new_phone):
        """
        Добавляем еще один номер телефона в существующий контакт
        """
        self.phones.value.append(new_phone.value)

    def days_to_birthday(self, date_birthday):
        """
        Метод высчитывает количество дней до следующего дня рождения.
        """
        today = datetime.today()
        birthday = date_birthday
        new_data = datetime(year=today.year, month=birthday.month, day=birthday.day + 1)
        self.difference = new_data - today
        if int(self.difference.days) > 0:
            return self.difference.days
        return 365 + int(self.difference.days)

    def change(self, old_number, new_number):
        """
        Метод для редактирования объектов Phone
        """
        self.remove(old_number)
        self.add_phone(new_number)

    def is_not_used(self):
        """
        Метод - заглушка, что б не мозолила глаза ошибка "Method 'add_phone' may be 'static'"
        """

    def remove(self, dell_phone):
        """
        Метод для удаления записи в phones
        """
        self.phones.value.remove(dell_phone.value)

    def __repr__(self):
        if not self.birthday:
            return str(f'Name: {self.name.value} Phone: {self.phones.value}')
        return str(f'Name: {self.name.value} Phone: {self.phones.value}, '
                   f'Birthday: {self.birthday.value}')


address_book = AddressBook()

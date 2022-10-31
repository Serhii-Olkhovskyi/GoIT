"""
В модуле разработаны следующие классы:
    AddressBook - создание адресной книги
"""
from collections import UserDict


class AddressBook(UserDict):
    """
    Класс AddressBook, который наследуется от UserDict, и добавлена логика поиска по записям
    """

    def add_phone(self, name, phone):
        """
        Добавление добавляем еще один номет телефона в существующий контакт
        """
        phone = Phone(phone)
        if name in self.data:
            record = self.data.get(name)  # -> Record:
            record.add(phone)

    def add_record(self, name, phone=None):
        """
        Добавление контакта в адресную книгу
        """
        name = Name(name)
        phone = Phone(phone)
        record = Record(name=name)
        record.add(phone)
        self.data[record.name.value] = record
        print(f'add contact: {record.name.value} is completed')

    def dell_number(self, name, phone):
        """
        Удаляем номер телефона у контакта
        """
        if name in self.data:
            record = self.data.get(name)  # -> Record:
            record.remove(phone)

    def find_number(self, name):
        """
        Поиск номера по имени
        """
        if name in self.data:
            print(self.data[name])
        else:
            print('contacts not found')

    def change(self, name, old_number, new_number):
        """
         Изменение контакта в адресной книге
        """

        if name in self.data:
            record = self.data.get(name)  # -> Record:
            record.change(old_number, new_number)


class Field:
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


class Name(Field):
    """
    Создаем класс для имени контакта. Класс Name, обязательное поле с именем.
    """

    def __init__(self, value):
        super().__init__(value)
        self.value = value


class Phone(Field):
    """
    Создаем класс для телефонного номера. Класс Phone, необязательное поле с телефоном
    """

    def __init__(self, value):
        super().__init__(value)
        self.value = value


class Record:
    """
    Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей
    и хранения обязательного поля Name.
    """

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add(self, phone):
        """
        Метод для добавления объектов Phone
        """
        self.phones.append(phone)

    def change(self, old_phone, new_number):
        """
        Метод для редактирования объектов Phone
        """
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_number

    def remove(self, dell_phone):
        """
        Метод для удаления записи в phones
        """
        for phone in self.phones:
            if phone.value == dell_phone:
                self.phones.remove(phone)

    def __repr__(self):
        return f"{', '.join([phone.value for phone in self.phones])}"

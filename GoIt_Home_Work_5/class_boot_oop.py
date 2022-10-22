from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def __str__(self):
        return f'{self.data}'


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, name, phones):
        self.name = name
        self.phones = [phones]

    def add(self, phone):
        self.phones.append(Phone(phone))



from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, name, phone=None):
        name = Name(name)
        phone = Phone(phone)
        record = Record(name=name)
        record.add(phone)
        self.data[record.name.value] = record
        print(f'add contact: {record.name.value} is completed')

    def change_number(self, name):
        if name in self.data:
            print(self.data[name])
        else:
            print('contacts not found')

    def __repr__(self):
        return f'{self.data}'


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add(self, phone):
        self.phones.append(phone)

    def remove(self, phone):
        self.phones.remove(phone)

    def update_phone(self, old_phone, new_phone):
        for find_phone in self.phones:
            if find_phone == Phone(old_phone):
                self.remove(Phone(old_phone))
                self.add(Phone(new_phone))

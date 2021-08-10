from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, record):
        self.data = record
    
class Record:
    def __init__(self, name):
        self.name = name
        self.phone = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, phone, new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)


class Field:
    pass

class Name(Field):
    record_name = 'name'
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
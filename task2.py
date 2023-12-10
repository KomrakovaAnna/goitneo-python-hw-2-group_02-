from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError:
            return "Invalid phone number format"
        return f"{phone} is added"

    def delete_phone(self, phone):
        for stored_phone in self.phones:
            if str(stored_phone) == phone:
                self.phones.remove(stored_phone)
                return f"{phone} deleted"
        return f"{phone} was not found!"

    def find_phone(self, phone):
        for stored_phone in self.phones:
            if str(stored_phone) == phone:
                return stored_phone
        return f"{phone} was not found"

    def edit_phone(self, phone, new_phone):
        for old_phone in self.phones:
            if str(old_phone) == phone:
                old_phone.value = new_phone
                break

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record
        return f"{record.name.value} added"

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            return f"{name} was not found"

    def find(self, name):
        if name in self.data:
            return self.data[name]
        return f"{name} was not found"

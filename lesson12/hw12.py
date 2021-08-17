import hw121
import inspect
import pathlib
import signal
import sys


def fadd(name, phone, birthday=None):
    if name.value in [key.value for key in list(contact_list.keys())]:
        raise ValueError(f'The new contact cannot be saved because the name "{name.value}" already exists. '
                         f'Please enter a different name.\n')
    record = hw121.Record(name, birthday) + phone
    contact_list.add_record(name, record)
    return f'New contact is saved: name "{name.value}", phone "{phone.value}", date of birth ' \
           f'"{birthday.value if birthday else "-"}".\n'


def fchange(name, phone, new_phone):
    if not name in [key.value for key in list(contact_list.keys())]:
        raise ValueError(f'Сontact by name "{name}" does not exist. Enter the correct name.\n')
    for nam, rec in contact_list.items():
        if nam.value == name:
            for ph in rec.phones:
                if ph.value == phone:
                    rec.change_phone(ph, new_phone)
                    return f'Saved a new phone number "{new_phone.value}" for a contact with the name "{name}".\n'
                else:
                    raise ValueError(f'The contact "{name}" does not have a phone number {phone}.\n')


def fexit():
    return 'Good bye!\n'


def fhello():
    return 'How can I help you?\n'


def fjoin(name, phone):
    if not name in [key.value for key in list(contact_list.keys())]:
        raise ValueError(f'Сontact with name "{name}" does not exist. Enter the correct name.\n')
    for nam, rec in contact_list.items():
        if nam.value == name:
            record = rec + phone
            contact_list.add_record(nam, record)
    return f'A new phone number "{phone.value}" has been added for the contact with the name "{name}".\n'


def fphone(name):
    for nam, rec in contact_list.items():
        if nam.value == name:
            return ' '.join([phone.value for phone in rec.phones])
    raise ValueError(f'Contact with the name "{name}" does not exist.\n')


def fshow_all():
    return contact_list.iterator()


def fsearch(pattern):
    result = ''
    for nam, rec in contact_list.items():
        phone_list = [phone.value for phone in rec.phones]
        for p in phone_list:
            if p.find(pattern) != (-1) or nam.value.find(pattern) != (-1):
                result += f'name: {nam.value}, phone: {" ".join([phone.value for phone in rec.phones])}, ' \
                          f'birtday: {rec.birthday.value if rec.birthday else "-"} ' \
                          f'{"("+str(rec.days_to_birthday())+" days)" if rec.days_to_birthday() else ""}\n'
    if not result:
        raise ValueError(f'No matches.\n')
    return result

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f'Command {e} not found'
        except ValueError as e:
            return e
        except IndexError as e:
            return f'Command not full'
    return inner

@ input_error
def get_command_handler(user_input):
    if user_input[:2] == ['show', 'all']:
        return fshow_all()
    elif user_input[:2] == ['good', 'bye'] or user_input[0] in ('close', 'exit', 'q', 'quit', 'cya'):
        return fexit()
    elif user_input[0] == 'search':
        return fsearch(user_input[1])
    elif user_input[0] == 'hello':
        return fhello()
    elif user_input[0] == 'phone':
        return fphone(user_input[1])
    elif user_input[0] == 'join':
        return fjoin(user_input[1], hw121.Phone(user_input[2]))
    elif user_input[0] == 'add':
        birthday = hw121.Birthday(user_input[3]) if len(user_input) > 3 else None
        return fadd(hw121.Name(user_input[1]), hw121.Phone(user_input[2]), birthday)
    elif user_input[0] == 'change':
        return fchange(user_input[1], user_input[2], hw121.Phone(user_input[3]))
    else:
        raise KeyError(user_input[0])


def signal_handler(signal, frame):
    contact_list.save_dumped_data()
    sys.exit(0)


contact_list = hw121.AddressBook()


if __name__ == '__main__':
    path = pathlib.Path('contact_list.txt')

    if path.exists() and path.stat().st_size > 0:
        contact_list = contact_list.read_dumped_data()

    print(f"""Hello. Please enter a command to do the following:
    show all - show contacts in the book
    search 'number' or 'phone' - to locate a person by number or phone
    phone 'name' - to show all phone numbers associated with a contact
    join 'name' 'phone' - to add a phone number to a contact
    add 'name' 'phone' 'birthday yyyy-mm-dd'(date is optional) - to add a new contact
    good bye, close or exit - to quit the application""")

    while True:
        user_input = input('Enter command: ').lower().split()
        result = get_command_handler(user_input)
        if result == 'Good bye!\n':
            print(result)
            break
        elif inspect.isgenerator(result):
            for n in result:
                for rec in n:
                    print(f'name: {rec.name.value}; phone: {", ".join([phone.value for phone in rec.phones])}; '
                          f'birthday {rec.birthday.value if rec.birthday else "-"} '
                          f'{"("+str(rec.days_to_birthday())+" days)" if rec.days_to_birthday() else ""}. ')
        else:
            print(result)
            signal.signal(signal.SIGINT, signal_handler)

    serialized_list = contact_list.save_dumped_data()


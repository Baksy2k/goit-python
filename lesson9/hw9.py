import re

exit_commands = ['good bye', 'close', 'exit', 'bye', 'cya', 'q', 'farewell', "i'm done", 'shoo']
phone_book = {'mark':'+380501234578', 'bark':'+380214578965'}

def say_hello():
    return 'Hey! How can I be at service?'

def add_contact(name, number):
    if name in phone_book:
        raise IndexError
    else:
        phone_book[name] = number
        return f'Contact {name.capitalize()} is in your phone book now!'


def change_contact(name, number):
    if name in phone_book:
        phone_book[name] = number
        return f'Contact {name.capitalize()} number is changed now!'        
    else:
        raise ValueError

def find_contact(name):
    if name in phone_book:
        return f"{name.capitalize()}'s number is {phone_book[name]}"
    else:
        raise ValueError

def print_contacts():
    contact_list = []
    for name, number in phone_book.items():
        contact_list.append(f'{name.capitalize()}: {number}')
    return '\n'.join(contact_list)

def input_error(command):
    def exceptions(*args):
        try:            
            return command(*args)        
        except KeyError:
            return 'There is no such command'
        except ValueError: 
            return 'Input data is invalid'
        except IndexError:
            return 'This contact already exists'
    return exceptions

commands = {
        'hi' : say_hello,
        'hello': say_hello,
        'add': add_contact,
        'change': change_contact,
        'phone': find_contact,
        'show all': print_contacts,
    }

@input_error
def parse_command(user_input):
    if user_input.startswith('show all'):
        command = 'show all'
    else:
        user_input_list = re.split(' ', user_input)
        if len(user_input_list) > 0:
            if user_input_list[0] in commands:
                command = user_input_list[0]
            else:
                raise KeyError
    return command

def parse_name(user_input):
    user_input_list = re.split(' ', user_input)
    if len(user_input_list) > 1:
        name = user_input_list[1]
    return name

@input_error
def parse_number(user_input):
    user_input_list = re.split(' ', user_input)
    if len(user_input_list) == 3:
        if user_input_list[2].isdigit and len(user_input_list[2]) == 12:
            number = '+' + user_input_list[2]
        elif user_input_list[2].isdigit and len(user_input_list[2]) == 10:
            number = '+38' + user_input_list[2]
        elif user_input_list[2][1:-1].isdigit and len(user_input_list[2]) == 13:
            number = user_input_list[2]
        else:
            raise ValueError
    return number

@input_error
def handle_command(command, user_input):
    if command in ['add','change']:
        name = parse_name(user_input)
        number = parse_number(user_input)
        result = commands[command](name, number) 
        return result
    elif command == 'phone':
        name = parse_name(user_input) 
        return commands[command](name)
    else:
        return commands[command]()        


def main():
    print("Hi! I'm a contact book bot and I recognize the following commands:")
    print('hello - just to be polite,')
    print('add - to add a new contact (add name number),')
    print('change - to change an existing number (change name number),')
    print('phone - to look up the number using name (phone name),')
    print('show all - to see the whole contact book.')
    print('To close the bot simply type: good bye, close or exit.')
    
    while True:
        try:
            user_input = input('').lower()
            if user_input in exit_commands:
                print('Good bye!')
                break
            else:
                print(handle_command(parse_command(user_input),user_input))
        except:
            print(f"Sorry, I cannot modify the phone book with this: '{user_input}'. Please be more clear.")

if __name__ == '__main__':
    main()
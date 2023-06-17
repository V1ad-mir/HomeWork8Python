from .text import *


def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)


def print_message(message: str):
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')


def show_contacts(book: list[dict[str, str], ]):
    my_heard = list(book[0])
    my_list = []
    for j in range(len(my_heard)):
        max_len = 0
        for i in range(len(book)):
            if max_len < (len(book[i].get(my_heard[j]))):
                max_len = (len(book[i].get(my_heard[j])))
        my_list.append(max_len)
    print(my_list)
    if book:
        print('\n' + '=' * (my_list[0]+my_list[1]+my_list[2]+my_list[3]+4))
        for contact in book:
            uid = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{uid:>{my_list[0]}}. {name:<{my_list[1]}} {phone:<{my_list[2]}} {comment:<{my_list[3]}}')
        print('=' * (my_list[0]+my_list[1]+my_list[2]+my_list[3]+4) + '\n')
        return True
    else:
        print(book_error)
        return False


def input_contact(message: str) -> dict[str, str]:
    print(message)
    name = input(new_contact[0])
    phone = input(new_contact[1])
    comment = input(new_contact[2])
    return {'name': name, 'phone': phone, 'comment': comment}


def input_return(message: str) -> str:
    return input(message)


def corect_data(incorrect_data: str) -> str:
    print(incorrect_data)


phone_book = []
path = 'phones.txt'


def open_file():
    if not phone_book:
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            user_id, name, phone, comment, *_ = contact.strip().split(':')
            phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})


def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': str(max(uid_list) + 1)}


def add_contact(new: dict):
    if not phone_book:
        open_file()
    new_1 = check_id() | new
    phone_book.append(new_1)


def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field


def del_contact(index: int):
    del_name = (phone_book.pop(index - 1))
    return del_name


def open_file_write():
    phones = open('phones.txt', 'w', encoding='UTF-8')
    for i in range(len(phone_book)):
        my_line = (list(dict(phone_book[i])))
        for j in range(len(my_line)):
            phones.write(dict(phone_book[i]).get(my_line[j]))
            if j < len(my_line) - 1: phones.write(':')
        phones.write('\n')
    phones.close()


def rename_id():
    for index in range(len(phone_book)):
        phone_book[index]['id'] = str(index + 1)


def corect_data_user():
    count = 1
    my_line = (list(phone_book[len(phone_book) - 1]))
    for i in range(len(my_line)):
        if not phone_book[len(phone_book) - 1].get(my_line[i]):
            count += 1
    if count == len(my_line):
        del_contact(len(phone_book))
        return False
    else:
        return True


def max_line():
    my_heard = list(phone_book[0])
    max_len = 0
    my_list = []
    for j in range(len(my_heard)):
        for i in range(len(phone_book)):
            if max_len < (len(phone_book[i].get(my_heard[j]))):
                max_len = (len(phone_book[i].get(my_heard[j])))
        my_list.append(max_len)

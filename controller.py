from view import menu, show_contacts, print_message, input_contact, input_return
import model
from view import text


def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                print_message(text.open_successful)
            case 2:
                model.open_file_write()
            case 3:
                show_contacts(model.phone_book)
            case 4:
                new = input_contact(text.input_new_contact)
                model.add_contact(new)
                if not model.corect_data_user(): break
                print_message(text.contact_saved(new.get('name')))


            case 5:
                word = input_return(text.search_word)
                result = model.search(word)
                my_list = model.max_line()
                show_contacts(result)
            case 6:
                word = input_return(text.search_word)
                result = model.search(word)
                if not show_contacts(result): break
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.phone_book[int(index) - 1].get('name')
                print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))

            case 7:
                word = input_return(text.search_word)
                result = model.search(word)
                if not show_contacts(result): break
                index = input_return(text.input_del_contact)
                if index == 0: break
                del_name = model.del_contact(int(index))
                print_message(text.dell_contact(del_name.get('name')))
                model.rename_id()

            case 8:
                break

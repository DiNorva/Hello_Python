import controller

phone_book = []
path = 'Workshop/lesson8/'


def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path 
    path += file

def open_file():
    global path 
    global phone_book
    with open (path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)

def save_file():
    global path 
    global phone_book
    with open (path, 'w', encoding='UTF-8') as file:
        file.write(('\n'.join(phone_book)))

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id, choise, value):
    global phone_book
    phone_book [int(id)][int(choise)] = value

def remove_contact():
    global path 
    global phone_book
    # with open (path, 'w', encoding='UTF-8') as file:
    #     file.write(('\n'.join(phone_book)))



    



    


    




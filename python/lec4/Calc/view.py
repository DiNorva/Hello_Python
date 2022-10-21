""" Модуль взаимодейсвия с пользователем: в рамках к-го пользователь может нажать на кнопочку """

def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    return int(input('value = '))

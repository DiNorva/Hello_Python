""" 2. Создайте программу для игры с конфетами человек против человека.
Правила: На столе лежит 150 конфет. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
1. Добавьте игру против бота
2. Подумайте как наделить бота 'интеллектом'
Оба задания обязательны """


# from random import randint



# i = 150
# while i > 0:
#     a = int(input('Игрок 1 введите количество конфет '))
#     if a > 28 or a < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a > 0:
#         if i - a == 0:
#             print('Победил 1 игрок')
#             break
#         elif i - a <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - a
#             print(f'Осталось {i} конфет')
#     if i > 28:
#         b = randint(1,28)
#         i = i - b
#         print(f'Бот забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#     elif i - b == 0:
#         print('Победил 2 игрок')
#         break
#     elif i < 28:
#         b = randint(1,i)
#         print(f'Бот Арсений забрал {b} конфет')
#         i = i - b
#         print(f'Осталось {i} конфет')
#     elif i - b <= 0:
#         raise ValueError('Неверный ход')
#     else:
#         i = i - b
#         print(f'Осталось {i} конфет')
""" 
1. Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет 
"""

# day = int(input('Введите день недели числом: '))
# if day > 7 or day < 1:
#     print('Пожалуйста, введите корректное число дня недели')
# elif day == 6 or day == 7:
#     print('Да, это выходной!')
# else:
#     print('Нет, это не выходной.')


# задача с семинара

# day = int(input("Введите цифру дня: "))

# match day:
#     case 1:
#         print("Понедельник день тяжелый")
#     case 2:
#         print("Вторник")
#     case 3:
#         print("Среда")
#     case 4:
#         print("Четверг")
#     case 5:
#         print("Пятница")
#     case 6:
#         print("Суббота")
#     case 7:
#         print("Воскресенье")
#     case _:
#         print("Такого дня недели нет")



""" 
2. Напишите программу для проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
"""


# x t t t t f f f f 
# y t t f f t t f f
# z t f t f t f t f

for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            not(x or y or z) != (not x and not y and not z)
            print('Не выполняется')
            break
        
else:
    print('Выполняется')



""" 
3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 
"""

# x = int(input('Введите число координаты x: '))
# y = int(input('Введите число координаты y: '))
# if x > 0 and y > 0:
#     print('Находится на оси 1')
# elif x < 0 and y > 0:
#     print('Находится на оси 2')
# elif x < 0 and y < 0:
#     print('Находится на оси 3')
# elif x > 0 and y < 0:
#     print('Находится на оси 4')



""" 
4. Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y). 
"""

# n = int(input('Введите номер четверти от 1 до 4: '))

# if n == 1:
#     print('Диапазон точек в этой четверти x > 0 и y > 0')
# elif n == 2:
#     print('Диапазон точек в этой четверти x < 0 и y > 0')
# elif n == 3:
#     print('Диапазон точек в этой четверти x < 0 и y < 0')
# elif n == 4:
#     print('Диапазон точек в этой четверти x > 0 и y < 0')
# else:
#     print('Значение не корректно')


""" 
5. Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 
"""


# print('Введите координаты точек A: ')
# xA = float(input('X: '))
# yA = float(input('Y: '))
# print('Введите координаты точек B: ')
# xB = float(input('X: '))
# yB = float(input('Y: '))

# print('Дистанция между А и В: ',(float((xB - xA)**2 + (yB - yA)**2)**(1/2))) # теорема Пифагора


# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int(input('Введите число: '))

if (n%10 == 0 or n%15 == 0) and n%30 !=0:
    print('Выполняется')
else:
    print('Выполняется')
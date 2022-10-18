""" 
<Задание 3>
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов. 
Если число целое, то его дробная часть не считается за 0 
и оно (число) в сравнении не участвует

Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
from decimal import Decimal
from random import randint as rI
from random import uniform as uI

number = int(input('Введите размер списка: '))

myList = []

for i in range(number):
    coef = rI(1,4)
    number = Decimal(f'{round(uI(-10,10), coef)}')
    myList.append(number)
print(myList)

numList = []
mantissa = []

for num in myList:
    numList.append(float(num))
    if abs(num) - int(abs(num)) != 0.0:
        mantissa.append(abs(num) - abs(int(num)))

print(numList)
print(f'Максимальная {max(mantissa)} и минимальная {min(mantissa)} мантиссы')
print(f'Разница мантисс {max(mantissa) - min(mantissa)}')
""" 
<Задание 1>
Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.

Пример:
[2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12
"""

from random import randint as rI


number = int(input('Введите размер списка: '))

myList = []

for i in range(number):
    myList.append(rI(-10,10))

print(myList)

oddList = []
for i in range(1, len(myList), 2):
    oddList.append(myList[i])


print(oddList)
print(sum(oddList))

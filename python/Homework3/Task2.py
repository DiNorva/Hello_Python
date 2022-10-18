""" 
<Задание 2>
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
[2, 3, 4, 5, 6] => [12, 15, 16]
[2, 3, 5, 6] => [12, 15]
"""

from random import randint as rI

number = int(input('Введите размер списка: '))

myList = []

for i in range(number):
    myList.append(rI(-10,10))

print(myList)

listLenght = len(myList)

multiList = []
for i in range(listLenght//2+1):
    element = myList[i]*myList[listLenght-i-1]
    multiList.append(element)

print(multiList)
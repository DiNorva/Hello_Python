""" 
<Задание 4>
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:
45 => 101101
3 => 11
2 => 10
"""



number = int(input('Введите число в десятичной системе: '))

num = number
binaryNumber = []

while number > 0:
    binaryNumber.insert(0, str(number%2))
    number //=2

print(f"Число {num} в двоичной системе {''.join(binaryNumber)}")

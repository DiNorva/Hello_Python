""" 
2. Напишите программу, которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)
Задайте список из n чисел последовательности (1+1/n)^n
"""

n = int(input('Введите число N: '))
lst = [1]

for i in range(2, n+1):
    lst.append(lst[i-2]* i)
print(lst)

# улучшение, используем List Comprehension

lst = [lst[i-2] * i if lst[i-2] != 0 else 1 for i in range(2, n+1, )]
print(f'Итог {lst}')








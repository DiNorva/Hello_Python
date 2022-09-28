""" 
1. Напишите программу, которая принимает на вход два числа и проверяет, я
вляется ли одно число квадратом другого.
    *Примеры:* 
    - 5, 25 -> да
    - 4, 16 -> да
    - 25, 5 -> да
    - 8,9 -> нет 
"""


# a = int(input('Введите число a = '))
# b = int(input('Введите число b = '))

# if a == b * b or b == a * a:
#     print('ДА')
# else:
#     print('НЕТ')



# a = int(input('Введите a '))
# b = int(input('Введите b '))

# if a == pow(b, 2):
#     print('a == pow(b, 2)') # а является квадратом b
# elif b == pow(a, 2):
#     print('b == pow(a, 2)') # b является квадратом a
# else:
#     print('Числа не являются квадратами друг друга')


""" 
2. Напишите программу, которая на вход принимает 5 чисел 
и находит максимальное из них.
    
    Примеры:
    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90
"""

# a = int(input('Введите a '))
# b = int(input('Введите b '))
# c = int(input('Введите c '))
# d = int(input('Введите d '))
# e = int(input('Введите e '))
# fmax = a
# if b > fmax:
#     fmax = b
# if c > fmax:
#     fmax = c
# if d > fmax:
#     fmax = d
# if e > fmax:
#     fmax = e
# print(fmax)



# a, b, c, d, e = int(input('Введите a ')), int(input('Введите b ')), int(input('Введите c ')), int(input('Введите d ')), int(input('Введите e '))
# fmax = max(a, b, c, d, e)
# print(fmax) 



# arrayInt = []
# for i in range(5):
#     arrayInt.append(int(input('Введите число ')))
# print(arrayInt)

# maxx = arrayInt[0]

# for i in range(len(arrayInt)):  # дает целочисленное нашего диапазона в начале
#     if maxx <= arrayInt[i]:
#         maxx = arrayInt[i]
# print(f'Максимальное значение в списке {arrayInt} будет {maxx}')


""" Второй вариант """
# arrayInt = []
# for i in range(5):
#     arrayInt.append(int(input('Введите число ')))
# print(arrayInt)

# maxx = arrayInt[0]

# for i in arrayInt:  # дает целочисленное нашего диапазона в начале
#     if maxx <= i:
#         maxx = i
# print(f'Максимальное значение в списке {arrayInt} будет {maxx}')

# list = [5, 17, 15, 3, -1]
# max = 0
# for i in range(5):
#     if list[i] > max:
#         max = list[i]
# print(max)


""" 
3. Напишите программу, которая будет на вход принимать число N
и выводить числа от - N до N
Примеры:
5 -> 5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 
"""

"""решение при помощи списка"""

# N = int(input('Введите число N '))
# arrayX = []                     # список пустой
# for i in range(-N, N + 1):
#     arrayX.append(i)    # append - добавляет значения из начего списка
# print(arrayX)



# a = int(input('Введите a = '))
# arr = []
# for i in range(-a, a+1):
#     arr.append(i)
# print(arr)

""" простой вариант """
# N = int(input('Введите N: '))
# for i in range(-N, N):
#     print(i, end=', ')
# print(N)

""" сложнее вариант """
# N = int(input('Введите N: '))
# for i in range(-N, N+1):
#     if i != N:
#         print(i, end=', ')
#     else:
#         print(i)



""" 
4.  Напишите программу, которая будет принимать на вход дробь
и показывать первую цифру дробной части числа.
Например:
6,78 -> 7
0,5 -> 5
5 -> нет
0, 34 -> 3
"""


number = float(input('Введите вещественное число: '))
if number == int(number):     
    print('Число целое')  
else: 
    print(int((number*10)%10))



















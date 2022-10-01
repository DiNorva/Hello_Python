""" 
1. Напишите программу, которая принимает на вход число N и 
выдаёт последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81 
"""

# 1 решение
# NumberN = int(input('Введите число N: '))
# result = []
# for i in range(NumberN):
#     result.append((-3)**i)
# print(result)

#  2 решение
# NumberN = int(input('Введите число N: '))
# result = []
# for i in range(NumberN):
#     result.append(pow(-3, i))
# print(result)



""" 
2. Для натурального n создать словарь индекс-значение, 
состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    
    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} 
"""

# решение
# n = int(input("Введите число: "))

# dict = {}

# for i in range(1, n+1):
#     dict[i] = 3*i+1

# print(dict)
# dict[4] = "Мы изменили тебя"
# print(dict)
# print(dict.get(8))

# dict = {}   # словарь
# list = [3, 4, 5, 6, 7, 7]
# list = [[3, 4], [5, 6], [7, 7]]  # вложенные списки

# dict = {3: 'Привет', 8: 'Пока'}

# print(dict.get(8))



""" 
3. Напишите программу, в которой пользователь будет задавать две строки, 
а программа - определять количество вхождений одной строки в другой. 
"""


# from itertools import count


# string1 = input('Введите первую строку ')
# string2 = input('Введите вторую строку ')
# count = 0
# for i in range(len(string1)):
#     if string1 [i] == string2 [i]:
        
#         for

#         count += 1

# первое решение
# string = "hsgfcwenwentfasfdasdfsagfgjfwenjkwwqfdgwenvdsfwent"
# substring = "went"
# count = 0
# buffer = 0
# lengthSubstring = len(substring)
# lengthString = len(string)
# for i in range(lengthString - lengthSubstring+1):
#     for j in range(lengthSubstring):
#         if string[i+j] != substring[j]:
#             buffer = 0
#             break
#         elif string[i+j] == substring[j]:
#             buffer += 1
#             if buffer == lengthSubstring:
#                 count += 1
#                 buffer = 0
#             continue
# print(count)


# второе решение

# string = input('Введите строку: ')
# substring = input('Введите строку для поиска: ')
# n = 0

# if string.find(substring) == -1:
#     print("Совпадений нет")
# else:
#     n = 1
#     new_string = string[(string.find(substring) + len(substring)):]
#     while new_string.find(substring) != -1:
#         n += 1
#         new_string = new_string[(new_string.find(substring) + len(substring)):]
        
# print(n)


# третье решение

string = "afgakwenwenhja;uicaweniuwgweneawen"
subString = "wen"

print(string.count(subString))



total = 0

for i in range(len(string)-len(subString)+1):
    count = 0
    if string[i] == subString[0]:
        for j in range(len(subString)):
            if string[i+j] == subString[j]:
                count += 1
        if count == len(subString):
            total += 1

print(f"Строка '{subString}' входит в строку '{string}' - {total} раз")



counter = 0

for i in range(len(string)):
    if string[i:i+len(subString)] == subString:
        counter += 1

print(f'Количество вхождений - {counter}')

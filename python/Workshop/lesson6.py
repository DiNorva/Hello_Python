""" Задача 1. Вводим 2 числа с клавиатуры и находим НОК (наименьшее общее кратное), 
такое число, которое бы делилось и на то, и на то без остатка (минимальное и макисмальное) """



# a, b = 16, 20 # ответ 80
# number = max(a, b)
# print(number)
# print()
# while True:
#     if number % a == 0 and number % b == 0:
#             break
#     number+=1

# print(f'Наименьшее общее кратное: {number}')





# numA = int(input('Введите первое число: '))
# numB = int(input('Введите второе число: '))

# i = 1

# while (min(numA, numB)*i)%max(numA, numB) !=0:
#     i +=1

# print(f'НОК чисел {numA} и {numB} равен {min(numA, numB)*i} (за {i} итераций)')




""" Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. Приоритет операций стандартный.

Пример:
2+2 => 4
1+2*3 => 7
1-2*3 => 5 """


# data = input('Введите выражение: ')
# prioritet = ['*', '/', '+', '-']

# listResult = []
# listResult = data.replace('+', ' + ')\
#         .replace('-', ' - ')\
#         .replace('*', ' * ')\
#         .replace('/', ' /')

# listResult = listResult.split()
# print(listResult)

# while len(listResult)>1:
#     if prioritet[0] in listResult or prioritet[1] in listResult:
#         for i in range(1,len(listResult)-1):
#             if listResult[i] == prioritet[0]:
#                 listResult[i-1] = int(listResult[i-1]) * int(listResult[i+1])  
#                 print(listResult)
#                 break
#             elif listResult[i] == prioritet[1]:
#                 listResult[i-1] = int(listResult[i-1]) / int(listResult[i+1])  
#                 print(listResult)
#                 break
#     else:  
#         for i in range(1,len(listResult)-1):    
#             if listResult[i] == prioritet[2]:
#                 listResult[i-1] = int(listResult[i-1]) + int(listResult[i+1])  
#                 print(listResult)
#                 break
#             elif listResult[i] == prioritet[3]:
#                 listResult [i-1]= int(listResult[i-1]) - int(listResult[i+1])  
#                 print(listResult)
#                 break
#     listResult.pop(i)
#     listResult.pop(i)

# print(f'{data} = {listResult[0]}')






# string = input('Введите выражение: ')

# opSelect = {
#     "*": lambda x, y: int(x) * int(y),
#     "/": lambda x, y: (int(x) / int(y)) if int(y) != 0 else division_be_zero(),
#     "+": lambda x, y: int(x) + int(y),
#     "-": lambda x, y: int(x) - int(y)}

# string = string.replace(' ', '').strip()
# string = string.replace('+', ' + ')\
#     .replace('-', ' - ')\
#     .replace('*', ' * ')\
#     .replace('/', ' / ')
# string = string.split()

# def division_be_zero():
#     print('Деление на ноль!')
#     exit()

# def deleteElement(string, i):
#     string.pop(i + 1)
#     string.pop(i)

# def operation(string, i, oper):
#     if string[i] == oper:
#         string[i - 1] = opSelect.get(oper)(int(string[i - 1]), int(string[i + 1]))
#         deleteElement(string, i)
#         return True

# example = ''.join(string)

# while len(string)>1:
#     if '*' in string or '/' in string:
#         for i in range(len(string)):
#             if operation(string, i, '*'): break
#             if operation(string, i, '/'): break

#     elif '+' in string or '-' in string:
#         for i in range(len(string)):
#             if operation(string, i, '+'): break
#             if operation(string, i, '-'): break

# print(f'{example}={string[0]}')
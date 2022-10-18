""" # типы данных и переменная
# int, float, boolean, str, list, None
value = None
print(type(value))

# print(type(a))
# print(type(b))

value = 12334
# print(type(value))
s = 'hello world'

a = 123
b = 1.23
print(s)  # вывод строки

# способы вывода
print(a, '-', b, '-', s)
print('{1} - {2} - {0}'.format (a, b, s))
print(f'{a} - {b} - {s}')

f = False
print(f) """


# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5, True]
# print(list)
# print(col)

""" # ВВод и вывод данных
# print, input

print('Введите a');
a = float(input())
print('Введите b');
b = float(input())
print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}') """



""" # # Арифметические операции
# +,-,*,/,%,//,**
# Приоритет операций 
# **,⊕,⊖,*,/,//,%,+,-
# (), Сокращенные операции
#  Скобки меняют приоритет

# a = 1.31231223
# b = 3
# c = round(a * b, 7)
# print(c)

a = 3
a *= 5

print(a) """


# Логические операции
# >,>=,<,<=,==,!=
# not, and, or – не путать с &, |, ^ 
# Кое-что ещё: is, is not, in, not in
# gen

# a = [1,2]
# b = [1,2]
# print(a == b)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2  # обращаемся к самому первому элементу из списка [1]
# print(is_odd)


""" # Управляющие конструкции
# if, if-else

# if condition1:
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# elif condition2:
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет,', username) """

# Управляющие конструкции: while
# original = 23
# inverted = 0 
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)


# Управляющие конструкции: for
# Когда мы знаем, что хотим


# for i in 'qwerty':
#     print(i)


""" text = 'съешь ещё этих мягких французских булок'
print(len(text))                 # 39
print('ещё' in text)             # True
print(text.isdigit())            # False
print(text.islower())            # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)
 """

# Списки
# Список - пронумерованная, изменяемая коллекция объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]

# ran = range(1,6)
# print(type(ran))
# numbers = list(ran) # 
# print(type(numbers))

# print(numbers) # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers) # [10, 2, 3, 4, 5]

# for i in numbers:
#     i *= 2
#     print(i)   # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]


""" colors = ['red', 'green', 'blue']

for e in colors:
    print(e) # red green blue 

for e in colors:
    print(e*2) # redred greengreen blueblue

colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент
   """

# Функции

# def function_name(x):
     # body line 1
     #.. .
     # body line n
     # optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 2
# print(f(arg))
# print(type(f(arg)))

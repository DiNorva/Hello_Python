""" 
Ускоренная обработка данных: lambda, filter, map,
zip, enumerate, List Comprehension 
"""


""" Анонимные, lambda функции
Идея: часто описывать функции некогда и не зачем """

# def f(x):
#     x**2

# g = f      # берем одну переменную g и кладем значение второй переменной
# print(f(1))
# print(g(1))



# def f(x):
#     return x**2
# print(f(2))  # 4



# def f(x):
#     return x**2

# g = f

# print(type(f))  # <class 'function'>
# print(type(g))  # <class 'function'>

# print(f(4))  # 16
# print(g(4))  # 16




# def calc1(x):
#     return x+10

# print(calc1(10))  # 20


# def calc2(x):
#     return x*10

# print(calc2(10))  # 100





# def calc1(x):
#     return x+10

# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)




""" пример функции с двумя переменными """

# def sum(x,y):
#     return x+y

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):      # в качестве аргумента может быть целая функци op
#     print(op(a,b))
#     # return op(a,b)

# calc(mylt, 4, 5)  # 20



# def sum(x,y):
#     return x+y

# f = sum

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):      
#     print(op(a,b))
#     # return op(a,b)

# calc(f, 4, 5)  # 9





# def sum(x,y):
#     return x+y

# sum = lambda x, y: x+y  # тоже самое, что и выше написано
# # sum = lambda x, y: x+y + 1

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):      
#     print(op(a,b))
#     # return op(a,b)

# calc(sum, 4, 5)  # 9



""" # сокращаем функцию, избавляясь от переменной sum """

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):      
#     print(op(a,b))
#     # return op(a,b)

# calc(lambda x, y: x+y, 4, 5)  # 9





""" List Comprehension """

""" 
[exp for item in iterable]
[exp for item in iterable (if conditional)]
[exp <if conditional> for item in iterable (if conditional)] 
"""

""" # создаем список, состоящий из четных чисел в диапазоне от 1 до 100 """

# list = []

# for i in range(1, 101):
#     if(i%2 == 0):       # остаток от деления на 2 = 0
#         list.append(i)
# print(list)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]



""" # равносильно функции выше """

# list = [i for i in range(1,21) if i % 2 == 0]
# print(list)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




# list = []

# for i in range(1, 101):
#         list.append(i)
# print(list)  # от 1 до 100


""" # равносильно функции выше """

# list = [i for i in range(1,21)]
# print(list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]



""" # создаем пару каждого из чисел, список картежей """

# list = [(i,i) for i in range(1,21) if i % 2 == 0]
# print(list)  # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]


""" возводим числа в степень, где числа четные """

# def f(x):
#     return x**3

# list = [f(i) for i in range(1,21) if i % 2 == 0]
# print(list)  # [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]


""" поключаем картежы в задачу выше """

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1,21) if i % 2 == 0]
# print(list)  # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]




""" Подключаем lambda """

""" задача
В файле хранятся числа, нужно выбрать четные 
и составить список пар (число; квадрат числа). Пример:
1 2 3 5 8 15 23 38
Получить:
[(2, 4), (8, 64), (38, 1444)] """


# with open('f.txt', 'a') as data:
#      data.write('1 2 3 5 8 15 23 38')

# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close

# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)  # [(2, 4), (8, 64), (38, 1444)]


""" делаем код лучше 
 """
# def select(f, col):    # некоторая функция select, которая будет принимать заниматься следующим: она будет принимать какую-то функцию и какой то набор данных
#     return [f(x) for x in col] # формируем новый список и будем его возращать

# def where(f, col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)  # [(2, 4), (8, 64), (38, 1444)]


""" преобразование с функцией map и избавление функции select"""

# def where(f, col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)  # [(2, 4), (8, 64), (38, 1444)]




""" 
Функция map


Функция map() применяет указанную функцию 
к каждому элементу итерируемого объекта 
и возвращает итератор с новыми объектами. 


f(x) ⇒ x + 10
map(f, [ 1,  2,   3,  4,  5])
         ↓   ↓    ↓   ↓   ↓ 
       [ 11, 12,  13, 14, 15]
Нельзя пройтись дважды

"""


# li = [x for x in range(1,20)]

# li = list(map(lambda x:x+10, li))

# print(li)  # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]



# data = map(int, input().split())
# print(data)  # <map object at 0x10300f4f0>

""" # преобразование """
# data = list(map(int, input().split()))
# print(data)  # [1, 2, 3, 4, 5]



# data = map(int, input().split())

# for e in data:
#     print(e)  # цифры стали в столбик

# или 
# data = map(int,'1 2 3 4 5'.split())

# for e in data:
#     print(e) # цифры преобразовались в столбик




# data = list(map(int,'1 2 3'.split()))

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e) 




""" 
Функция filter

Функция filter() применяет указанную функцию 
к каждому элементу итерируемого объекта и возвращает итератор
с теми объектами, для к-х ф-я вернула True.
f(x) => x - четное
filter(f, [1, 2, 3, 4 , 5])
                    ↓
           [  2,    4   ]
нельзя пройтись дважды 

"""


# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)  # [0, 2, 4, 6, 8]


""" преобразовываем нашу задачу вместо where вставляем filter """

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)  # [(2, 4), (8, 64), (38, 1444)]



""" 
Функция zip


Функция zip() применяется к набору итерируемых объектов 
и возвращает итератор с кортежами из элементов входных данных.

функция zip пробегается по мин входящему набору

Количество элементов в результате равно минимальному количеству 
элементов входного набора
 zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
                        ↓
 [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
 Нельзя пройтись дважды 
 
"""

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]

# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

   
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]
 




""" 

Функция enumerate


Функция enumerate применяется к итерируемому объекту и возвращает
новый итератор с кортежами из индекса и элементов входных данных.

enumerate(['Казань'], ['Смоленск'], ['Рыбки'], ['Чикаго'])

[(0, 'Казань'), (1,'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
 Нельзя пройтись дважды  
 
"""

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]
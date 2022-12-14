# Как работать с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+



# with open('file.txt', 'a') as data:
#      data.write('line 1111\n')
#      data.write('line 2222\n')



# colors = ['red', 'green', 'blue3']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('LINE 121\n') 
# data.write('LINE 131\n') 
# data.close()





# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()


""" 
import hello as h

print(h.f(1))
"""


# def new_string(symbol, count = 3):
#      return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12



# def concatenatio(*params):
#     res = 0
#     for item in params:
#          res += item
#     return res

# print(concatenatio(1, 2, 3, 4)) # 10




# def concatenatio(*params):
#      res: str = ""
#      for item in params:
#          res += item
#      return res
# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2



""" рекурсия - ф-я вызывающая сама себя """

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#      list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


""" Кортеж – это неизменяемый “список” """
""" идея кортежа: если требуется создание какой-то пары """

# a = (3, 1, 41, 4) 
# print(a)
# print(a[0])
# a[0] = 12 # для кортежа не работает, только для списка


# a = (3, 1, 41, 4) 
# for item in a:
#     print(item)


# t = ()
# print(type(t))
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors)            # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)                 # ('red', 'green', 'blue')



# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue



""" Словари
Неупорядоченные коллекции произвольных объектов с доступом по ключу """

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# # print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left'])  # ←
# # типы ключей могут отличаться

# for k in dictionary.values():    #values: ↑←↓→  keys: up left down right
#     print(k)



# print(dictionary['up'])   # ↑
#  # типы ключей могут отличаться

# dictionary['left'] = '⇐' 
# print(dictionary['left']) # ⇐ 
# #print(dictionary['type']) # KeyError: 'type' 
# del dictionary['left'] # удаление элемента

# for item in dictionary:       # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
#  # up: ↑
#  # down: ↓
#  # right: →



""" Множества
Неупорядоченная совокупность элементов """
# идея: если мы определяем некоторую переменную и кладем какое то значение


# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a))  # set
# print(type(b))  # set



# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a))  # set
# print(type(b))  # set
# print(type(c))  # set
# a = {1, 1, 1, 1, 1}
# print(a)  # {1}


# colors = {'red', 'green', 'blue'}

# print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'red', 'blue', 'green', 'gray'}
# colors.remove('red')
# print(colors)  # {'green', 'blue', 'gray'}
# colors.discard('red')
# print(colors)   # {'green', 'blue', 'gray'}
# colors.clear()
# print(colors)   # set()





# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()            # c = {1, 2, 3, 5, 8}
# u = a.union(b)          # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)   # i = {8, 2, 5}
# dl = a.difference(b)    # dl = {1, 3}
# dr = b.difference(a)    # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}



""" список """


# list1 = [1,2,3,4,5]
# list2 = list1
# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

""" каким образом можно удалять последний элемент нашего списка """

# list1 = [1,2,3,4,5]

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

""" если нужно удалить какой-то конкретный элемент в списке """

# list1 = [1,2,3,4,5]

# print(list1.pop(2))  # [1, 2, 4, 5]
# print(list1)

""" если нужно вставить на нужную позицию """

# list1 = [1,2,3,4,5]

# print(list1.insert(2, 11))  # [1, 2, 11, 3, 4, 5]
# print(list1)

""" если нужно добавить в конец списка """

# list1 = [1,2,3,4,5]

# print(list1.append(11))  # [1, 2, 3, 4, 5, 11]
# print(list1)

""" 
4. Реализуйте алгоритм перемешивания списка, без использования 
встроеных методов (особенно SHUFFLE, без него) можно (нужно) 
использовать библиотеку Random 
"""
# Первое решение

# использовала zip

import random 

lst = ['7', 'True', '1.10', 'Капуста']
ids = [0,1,2,3]
data = list(zip(lst, ids))
print(data)
res = random.sample(data, len(data))
print(res)


# Второе решение

# import random

# list = []

# for _ in range(10):
#     list.append(random.randint(0,50))
# print('Оригинальный список: ' + str(list))

# for i in range(len(list)-1):
#     j = random.randint(0, len(list)-1)
#     list[i], list[j] = list[j], list[i]

# print('Перемешенный список: ' + str(list))

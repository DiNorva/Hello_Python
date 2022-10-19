""" 
3. Задайте последовательность цифр. 
Напишите программу, которая выведет список неповторяющихся элементов
исходной последовательности.
Пример:
47756688399943 -> [5]
1113384455229 -> [8,9]
1115566773322 -> [] 
"""


list_numbers = list(map(int, input("Введите числа через пробел:\n").split()))

def get_unique_numbers(arr_numbers):
    unique_list = []
    for i in arr_numbers:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(get_unique_numbers(list_numbers))





# решение с семинара

# import random

# uniqueList = {}
# finalStr = ''

# listStr = ''.join(list(map(str, [random.randint(0,9) for i in range(40)])))
# print(f'Задана последовательность цифр {listStr}')

# for c in listStr:
#     if uniqueList.get(c):
#         uniqueList[c] = uniqueList.get(c) + 1
#     else:
#         uniqueList[c] = 1

# # print(uniqueList)

# for k,v in uniqueList.items():
#     if v == 1:
#         finalStr += str(k) + ' '

# print(f'Уникальные цифры {finalStr}') if finalStr else print('Уникальных позиций нет')











# import random

# myList = []
# for i in range(10):
#     myList.append(random.randint(0,10))

# for i in range(len(myList)):
#     myList[i] =str(myList[i])

# print(myList)

# # myList = list(map(lambda x: str(x) + '1', myList))

# # myList = list(map(lambda x: str(x) * 3, myList))

# # print(myList)

# myList = ''.join(myList)

# myList2 = ''.join (list(map(str, [random.randint(0,10) for i in range(10)])))

# # myList2 = list(map(str, myList2))

# print(myList)
# print(myList2)




# zip

# myList1 = [random.randint(0,10) for _ in range(10)]
# myList2 = [random.randint(0,10) for _ in range(5)]
# myList3 = [random.randint(0,10) for _ in range(20)]

# myList = list(zip(myList1, myList2, myList3))

# print(myList1)
# print(myList2)
# print(myList3)
# print()
# myList = list(map(sum, myList))
# print(myList)

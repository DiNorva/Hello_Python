""" 
1. Задайте список. Напишите программу, которая определит, 
присутствует ли в заданном списке строк некое число. 
"""
# первое решение


# g = ["fsvs4s45vs342f236", "235n234wqfe", "rdwqh352527asfs", "dahfw324"]

# num = input("Введите искомое число: ")

# flag=True

# for i in g:
#     for j in i:
#         if num==j:
#             print("Число присутствует в элементе " +i)
#             flag=False
#             break
# if flag:
#     print("Число не найдено!")




""" 
3. Напишите программу, которая определит позицию второго вхождения
строки в списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1 
"""
# первое решение

list = ["qwe", "asd", "zxc", "qwe", "ячс", "asd", "цук", "123", "234", 123,]
print(list)
a = input('Введите искомый элемент: ')
count = 0
for i in range(len(list)):
    if list[i] == a:
        count += 1
        if count == 2:
            print (i)
            break
else:
    print("нет")


# второе решение

# myList = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# num=input("Введите искомую строку: ")
# buffer = 0
# count = 0
# for element in range(0,len(myList)-1):
#     if num==myList[element]:
#         count+=1
#     if count == 2:
#         buffer = element
# if count == 2:
#     print(buffer)
# else:
#     print("-1")


# третье решение

# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# find_list = "йцу"
# sum = 0
# for i in range(len(my_list)):
#     if my_list[i] == find_list:
#         sum += 1
#         if sum == 2:
#            print(f'индекс элемента второго вхождения -> {i}') 
#            break
# else:
#     print(-1)
""" 
2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. 
"""

number = int(input('Введите число: '))

i = 2
list = []
old = number
while i <= number:
    if number % i == 0:
        list.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(set(list))






# решение с семинара

# numbers = int(input('Введите число: '))

# devList = []
# dev = 2
# while numbers>2:
#     if numbers%dev != 0:
#         dev += 1
#     else:
#         numbers //= dev
#         devList.append(dev)

# print(set(devList))






# tuple = {1,2,3,4,4,5,6,6,6,7,7}
# print(tuple)






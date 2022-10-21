"""  Задача 0
Написать программу сложения двух чисел """


""" самое простое решение """

# x = int(input('x= '))
# y = int(input('y= '))
# print(f'{x} + {y} = {x + y}')



""" посложнее - решение для тех кто только начинает знакомиться с методами  """

# def sum(a, b):
#     return a + b

# x = int(input('x= '))
# y = int(input('y= '))
# print(f'{x} + {y} = {sum(x, y)}')


""" решение через lambda, не отличается от def """

# sum = lambda a, b: a+b

# x = int(input('x= '))
# y = int(input('y= '))
# print(f'{x} + {y} = {sum(x, y)}')


""" создание приложения через модули """



x = 0
y = 0

def init(a, b):  # описали метод, к-й отвечает на инициализацию x и y
    global x
    global y
    x = a
    y = b

def sum():   # метож,к-й будет складывать два этих числа
    return x + y 

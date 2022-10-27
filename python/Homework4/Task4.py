""" 
4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
многочлена и записать в файл многочлен степени k
k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
Пример:
k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0 
"""



# не поняла как решать самой, поэтому посмотрела урок с семинара и разобрала 

# решение с семинара

import random


def createDict():
    equation = {}
    degree = int(input('Введите максимальную степень многочлена: '))
    for i in range(degree, -1, -1):
        equation[i] = random.randint(-10,10)
    return equation


def createEquation(equation: dict):
    strEquation = ''
    first = True

    for k,v in equation.items():
        if first:
            first = False
            if v > 0:
                strEquation += f'{v}*x^{k}'
            elif v < 0:
                strEquation += f'-{abs(v)}*x^{k}'    # v взять по модулю abs
        else:
            if v > 0:
                strEquation += f' + {v}*x^{k}'
            elif v < 0:
                strEquation += f' - {abs(v)}*x^{k}'

    return strEquation

def printEquation(equation: str):
    print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0')


def parseEquation(equation: str):
    eqDict = {}
    equation = equation.replace(' + ', ' ').replace(' - ', ' -')
    equation = equation.split()


    for i in equation:
        element = i.split('*x^')
        eqDict[int(element[1])] = int(element[0])
    
    return eqDict


def summEquation(equation1: dict, equation2: dict):
    finalEquation = {}

    for i in range(max(len(equation1), len(equation2)), -1, -1):
        if equation1.get(i) or equation2.get(i):
            finalEquation[i] = (equation1.get(i) if equation1.get(i) else 0) + (equation2.get(i) if equation2.get(i) else 0)
    return finalEquation

equation1 = createDict()
equation2 = createDict()

finalEquation = summEquation(equation1, equation2)

printEquation(createEquation(equation1))
printEquation(createEquation(equation2))
printEquation(createEquation(finalEquation))

""" Добавить в калькулятор строчный формат
пример: вводим строку 1+10/2 + 3*8 и получить в ответ 30 """

import controller, model

model.string = input('Введите выражение: ')

controller.solutionExpression(model.string)
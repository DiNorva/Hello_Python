# консоль, отображается результат операции

import tkinter as tk


def inputData(string: str):  # даты
    number = int(input(f'Введите {string} число: '))
    return number

def outputResult(a, b, oper, number):    # вывод даты
    print(f'Результат операции {a} {oper} {b} = {number}')

def inputOperator():    # оператор
    oper = input(f'Введите оператор: ')
    return oper

def devision_by_zero():
    print('Деление на ноль!')

def print_window(result):
    win = tk.Tk()
    win.geometry('300x300+600+600')
    my_label = tk.Label(win, text=result)
    my_label.pack()
    win.mainloop()
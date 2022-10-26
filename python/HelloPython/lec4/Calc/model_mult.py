""" модель для перемножения чисел """

x = 0
y = 0

def init(a, b):  # описали метод, к-й отвечает на инициализацию x и y
    global x
    global y
    x = a
    y = b

def do_it():   
    return x * y 
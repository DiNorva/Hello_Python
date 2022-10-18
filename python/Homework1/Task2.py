""" 
2. Напишите программу для проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
"""


# x t t t t f f f f 
# y t t f f t t f f
# z t f t f t f t f

for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            not(x or y or z) != (not x and not y and not z)
            print('Не выполняется')
            break
        
else:
    print('Выполняется')



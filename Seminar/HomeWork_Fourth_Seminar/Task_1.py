# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141
# Ввод: 0.01
# Вывод: 3.14

# Ввод: 0.001
# Вывод: 3.141

import math
i = float(input('Введите точность для числа π :'))
step = 0
while i !=1:
    i *=10
    step +=1
    print(f'i = {i}, step = {step}')
print(f'Число π получилось - {round(math.pi, step)}')

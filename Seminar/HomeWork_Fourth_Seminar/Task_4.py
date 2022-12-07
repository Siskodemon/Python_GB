# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random
k = random.randint(0,10)
print(f'Выбрана степень k = {k}')
if k ==0:
    print(f'0')
else:
    while k !=0:
        N = random.randint(0,100)
        if N != 0:
            if k == 1:
                print(f'{N}(x**{k}) ', end='')
                k -= 1
            else:
                print(f'{N}(x**{k}) + ', end='')
                k -=1
        else:
            k -=1
    else:
        N = random.randint(0,100)
        if N != 0:
            print(f'+ {N} = 0')
        else:
            print(f'= 0')

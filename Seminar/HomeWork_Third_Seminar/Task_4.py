# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

chislo = int(input('Введите число: '))
result = ''
if chislo > 1:
    while chislo//2 !=1:
        result = str(chislo%2)+result
        chislo = chislo//2
    else:
        result = '1' + str(chislo % 2) + result
else:
    result = str(chislo)
print(f'Результат - {result}')




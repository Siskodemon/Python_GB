# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(list:list,i: int):
    if i < 2:
        return i
    else:
        return list[i-1]+list[i-2]

chislo = int(input('Введите число: '))
array=[]
result = []
for index in range(0,chislo+1):
    array.append(fib(array,index))
for index in range(1, chislo+1):
    if (index%2 == 1 and chislo%2 == 0) or (index % 2 == 0 and chislo % 2 == 1):
        result.append(array[index*-1]*-1)
    else:
        result.append(array[index*-1])
for index in range(0, chislo+1):
    result.append(array[index])
print(f'Результат - {result}')

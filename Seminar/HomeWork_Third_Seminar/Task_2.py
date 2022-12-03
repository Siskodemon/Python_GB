# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def input_array(list:list,str:str,kol:int):
    if str == 'y':
        for i in range(0,kol-1):
            list.append(int(input(f'Введите {i}-ый элемент списка: ')))
    else:
        from random import randint
        for i in range(0, kol):
            list.append(randint(1,9))
    return list

count = int(input('Введите кол-во элементов в списке: '))
list = []
answer = input('Вводим числа самостоятельно? (y/n): ')
list = input_array(list,answer,count)
print(f'Полученный список - {list}')
sum=[]
import math
for i in range(0,(math.ceil(len(list)/2))):
    sum.append(int(list[i]*list[-(i+1)]))
print(f'Полученный список сумм - {sum}')

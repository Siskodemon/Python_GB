# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def rec(list:list, i:int):
    if i+2<=len(list)-1:
        return int(list[i]) + int(rec(list,i+2))
    else:
        return list[i]

def input_array(list:list,str:str,kol:int):
    if str == 'y':
        list = [int(input(f'Введите {i}-ый элемент списка: ')) for i in range(0, kol)]  # list comprehension
        # for i in range(0,kol-1):
        #     list.append(int(input(f'Введите {i}-ый элемент списка: ')))
    else:
        from random import randint
        list = [randint(0, 10) for i in range(0, kol)]  # list comprehension
        # for i in range(0, kol):
        #     list.append(randint(0,100))
    return list

count = int(input('Введите кол-во элементов в списке: '))
list = []
answer = input('Вводим числа самостоятельно? (y/n): ')
list = input_array(list,answer,count)
print(f'Полученный список: {list}')
print(f'Сумма элементов списка нечётных индексов - {rec(list,1)}')
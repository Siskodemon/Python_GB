# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19
def input_array(list: list, str: str, kol: int):
    if str == 'y':
        for i in range(0, kol):
            list.append(float(input(f'Введите {i}-ый элемент списка: ')))
    else:
        import random
        for i in range(0, kol):
            list.append(round(random.randint(1, 9)+random.uniform(0,1),2))
    return list

count = int(input('Введите кол-во элементов в списке: '))
list = []
answer = input('Вводим числа самостоятельно? (y/n): ')
list = input_array(list, answer, count)
print(f'Полученный список - {list}')
max = round(list[0] - (list[0]*10) // 10, 2)
min = round(list[0] - (list[0]*10) // 10, 2)
if count < 3:
    if (round(list[1] - (list[1]*10) // 10, 2)) > max:
        max = round(list[1] - (list[1]*10) // 10, 2)
    elif (round(list[1] - (list[1]*10) // 10, 2)) < min:
        min = round(list[1] - (list[1]*10) // 10, 2)
else:
    for i in range(1, count):
        if (round(list[i] - (list[i]*10) // 10, 2)) > max:
            max = round(list[i] - (list[i]*10) // 10, 2)
        elif (round(list[i] - (list[i]*10) // 10, 2)) < min:
            min = round(list[i] - (list[i]*10) // 10, 2)
print(f'max = {max}, min = {min}, разность = {max-min}')

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

def input_array(list: list, str: str, kol: int):
    if str == 'y' or str == 'yes':
        for i in range(0, kol):
            list.append(int(input(f'Введите {i}-ый элемент списка: ')))
    else:
        import random
        for i in range(0, kol):
            list.append(random.randint(1, 9))
    return list


count = int(input('Введите кол-во элементов в списке: '))
list,list2 = [],[]
answer = input('Вводим числа самостоятельно? (y/n): ')
list = input_array(list, answer, count)
print(f'Полученный список - {list}')
for i in range(0,len(list)):
    for j in range(0,len(list)):
        if list[i] == list[j] and i != j:
            break
        elif j == len(list)-1:
            list2.append(list[i])
            break
print(f'Отобранный список - {list2}')



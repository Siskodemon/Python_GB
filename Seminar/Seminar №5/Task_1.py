# my_string = 'Я люблю абвЖаву иабв Питон'

# my_li = my_string.split()
# print(my_li)

# my_li = list(filter(lambda el: not "абв" in el, my_li))
# print(my_li)

# my_string = ' '.join(my_li)
# print(my_string)

# Решение вариант №2

# res = [i for i in s.split() if 'абв' not in i]

# res_filt = filter(lambda item: 'абв' not in item, [i for i in s.split()])

# 2. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 4 5 7 8 9


# string_ = '1 2 3 4 5 6 8 9'
# li = list(map(int,string_.split()))
# print(li)
# for i in range(1,len(li)-1):
#     if li[i]-1 != li[i-1]:
#         li.insert(i,li[i]-1)
# print(li)


# 3. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

#     *Пример:*
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

ch = int(input('Введите количесто числе: '))
list = []
list2 = [0]
import random
for item in range(0,ch):
    list.append(random.randint(1,100))
print(list)
list2[0] = list[0]
for item in range(1,ch):
    if list2[len(list2)-1]<list[item]:
        list2.append(list[item])
print(list2)
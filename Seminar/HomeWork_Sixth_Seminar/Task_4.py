# Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# - -> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

N = int(input('Введите число: '))
# list=[]
# for i in range(-N,N+1):
#     list.append(i)
list1 = [i for i in range(-N, N+1)]  # list comprehension
print(f'Полученный список - {list1}')
list2=[]
j='1'
while j !="":
    j = input('Введите индекс или просто нажмите Enter: ')
    if j !="":
        list2.append(int(j))
sum=1
for i in range(0,len(list2)):
    sum *= list1[list2[i]]
print(f'Сумма индексов - {sum}')

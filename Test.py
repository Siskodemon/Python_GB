import random

def index(count):
    l=[]
    l.append(random.randint(0,count-1))
    b = random.randint(0,count-1)
    while b == l[0]:
        b = random.randint(0,count-1)
    l.append(b)
    return l

def meshaem(list1, list2):
    buf = list1[list2[0]]
    list1[list2[0]] = list1[list2[1]]
    list1[list2[1]] = buf
    return list1

kol = int(input(f'Введите кол-во элементов - '))
list = [random.randint(0,9) for i in range(0,kol)]
print(f'Список элекментов - {list}')

while i = index(kol)
print(f'Список индексов - {i}')
print(f'Перемешанный список - {meshaem(list,i)}')
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
nat_chislo = int(input('Введите натуральное число: '))
list = set()
list2 = set()
if nat_chislo != 1:
    while nat_chislo !=1:
        if nat_chislo != 2 and nat_chislo != 3 and nat_chislo != 5 and nat_chislo != 7:
            if nat_chislo % 2 == 0:
                list.add(nat_chislo // 2)
                nat_chislo //= 2
                list2.add(2)
                print(f' Делитель 2, nat_chislo - {nat_chislo}')
            elif nat_chislo % 3 == 0:
                list.add(nat_chislo // 3)
                nat_chislo //= 3
                list2.add(3)
                print(f' Делитель 3, nat_chislo - {nat_chislo}')
            elif nat_chislo % 5 == 0:
                list.append(nat_chislo // 5)
                list2.add(5)
                nat_chislo //= 5
                print(f' Делитель 5, nat_chislo - {nat_chislo}')
            elif nat_chislo % 7 == 0:
                list.add(nat_chislo // 7)
                list2.add(7)
                nat_chislo //= 7
                print(f' Делитель 7, nat_chislo - {nat_chislo}')  
            else:
                nat_chislo = 1
        else:
            list2.add(nat_chislo)
            nat_chislo=1
    else:
        list2.add(1)
else:
    list.add(1)
    print(f'1-ца делица нацело только сама на себя...')
print(f'{list.union(list2)}')

# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

str1 = input('Введите строку №1 - ')
str2 = input('Введите строку №2 - ')
count=0
k=0
chislo=0
if len(str1)>len(str2):
    for i in range(0,len(str1)):
        for j in range(0, len(str2)):
            k=i
            if str1[k] == str2[j]:
                count += 1
                k += 1
                if count == len(str2):
                    chislo += 1
                    count = 0
            else:
                count = 0
                k=i
else:
    for i in range(0, len(str2)):
        for j in range(0, len(str1)):
            k = i
            if str2[k] == str1[j]:
                count += 1
                k += 1
                if count == len(str1):
                    chislo += 1
                    count = 0
            else:
                count = 0
                k = i

print(f'Число вхождений - {chislo}')
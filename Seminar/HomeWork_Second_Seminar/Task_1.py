# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

chislo = float(input('Введите вещественное число: '))
sum=0.0
a = (chislo*10) % 10
chislo = (chislo*10) // 10
while chislo%10 != chislo:
    sum = sum + chislo % 10
    chislo = chislo//10
else:
    sum = sum + chislo % 10
while (round(a, 1)*10) % 100 != 0:
     sum = sum + (round(a,1)*10) // 10
     a = round((a*10) % 10,3)
else:
    sum = sum + (round(a, 1)*10) // 10
print(f'Сумма чисел вещественного числа - {int(sum)}')



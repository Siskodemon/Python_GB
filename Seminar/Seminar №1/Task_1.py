# Напишите программу которая принемает на вход два числа и проверяет не является ли одно число квадратом другого
a = int(input('Введите первое число - '))
b = int(input('Введите второе число - '))
if a == b**2 or b == a**2:
    print('Да является')
else:
    print('Нет не является')
# Напишите программу, которая будет принимать на вход число N и выводить в терминал  промежуток от -N до N
numbers = []
N = int (input('Введите число N - '))
for _ in range((N*2)+1):
    numbers.append(-N) # команда .append довалят значение в конец массива(списка)
    N -=1
print(numbers)
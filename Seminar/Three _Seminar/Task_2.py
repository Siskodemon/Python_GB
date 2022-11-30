# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел(time).
from datetime import datetime


def get_random_number(n):
    now = datetime.now()
    random_number = now.time().second ** now.time().minute * now.time().microsecond
    return random_number % 10**n


print(get_random_number(3))


# import time
# x = time.time() * 1000
# x %= 1000
# print(round(x))


# Разница записи передаваемых значений в картежи и словари (в словарь передаються ключи со значения)
# по умолчанию ввсе передаваемые значения записываються попорядку введения в функцию при описании
#
# def func(a_1, a_2, *args, **kwargs):
#     return a_1, a_2, args, kwargs
# print(func(1, 2, 3, 4, 542, 124, 'wetwet', key_1=10, key_2=30))

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_string = 'Я люблю абвЖаву иабв Питон'

str = my_string.split()
print(str)

str = list(filter(lambda el: not "абв" in el, str))
print(str)

my_string = ' '.join(str)
print(my_string)

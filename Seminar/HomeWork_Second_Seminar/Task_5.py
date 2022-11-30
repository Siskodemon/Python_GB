#Реализуйте алгоритм перемешивания списка.
from random import randint
def input_List():
    list=[]
    symbol = 'Yes'
    while symbol !='':
        symbol = input('Введите  следующий элемент списка, либо просто нажмите Enter для завершение ввода: ')
        if symbol != '':
            list.append(symbol)
    print(list)
    return list
  
ch = input('Список будем сами вводить или выберем готовый?(y/n): ')
list=[]
if ch == 'y' or ch == 'yes':
    list = input_List()
else:
    list = ['1q','2w','3e','4r','5t']
    print(list)
ch=''
from random import randint
while ch == '':
    ch = input('Мешаем? Если да просто нажми Enter, или введите что-нибудь для завершения = ')
    if ch == '':
        i1 = randint(0, len(list)-1)
        i2 = randint(0, len(list)-1)
        if i1 == i2:
            while i1 == i2:
                i2 = randint(0, len(list))
        buf = list[i1]
        list[i1] = list[i2]
        list[i2] = buf
        print(list)
    else:
        print(f'Перемешивание завершено. окончательный список - {list}')


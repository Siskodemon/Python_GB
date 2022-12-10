# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def open_file(file: str, f=str()):
    date = open(file, 'r', encoding='cp1251')
    for i in date:
        f = f+i
    date.close()
    return f

chois = int(input('Восстанавливаем или архивируем?(1 - восстанавливаем,0 - архивируем) - '))
if chois == 0:
    with open('archiv.txt', 'w') as arc:
        arc.write('')
    file = open_file('file.txt', str())
    print(f'Полученная строка  - {file}')
    count=0
    symbol = file[0]
    for i in range(0,len(file)):
        if file[i] == symbol and i != len(file):
            count +=1
        else:
            with open('archiv.txt', 'a') as arc:
                arc.write(symbol+str(count))
                count=1
                symbol=file[i]

    with open('archiv.txt', 'a') as arc:
        arc.write(symbol+str(count))
        count = 1
        symbol = file[i]
else:
    with open('file.txt', 'w') as arc:
        arc.write('')
    file = open_file('archiv.txt', str())
    print(f'Полученная строка  - {file}')
    count,i=0,0
    symbol = file[count]
    while count < len(file)-1:
        with open('file.txt', 'a') as arc:
            while i != int(file[count+1]):
                arc.write(symbol)
                i +=1
        count +=2
        i=0
        if count<=len(file)-2:
            symbol = file[count]
    

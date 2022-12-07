# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов(складываются числа, у которых "х" в одинаковых степенях). 
# Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

def insert_file(file:str):
    import random
    k = random.randint(0, 9)
    if k == 0:
        with open(file, 'a') as f:
            f.write('0')
    else:
        max = k
        while k != 0:
            N = random.randint(0, 100)
            if N != 0:
                if k == max:
                    with open(file, 'a') as f:
                        f.write(f'{N}*(x**{k})')
                    k -= 1
                else:
                    with open(file, 'a') as f:
                        f.write(f' + {N}*(x**{k})')
                    k -= 1
            else:
                k -= 1
        else:
            N = random.randint(0, 100)
            if N != 0:
                with open(file, 'a') as f:
                    f.write(f' + {N} = 0')
            else:
                with open(file, 'a') as f:
                    f.write(f' = 0')

def open_file(file:str,f=str()):
    date = open(file, 'r', encoding='cp1251')
    for i in date:
        f=f+i
    date.close()
    return f

def kof(f:str,index:int):
    print(f'Степень = {index}; ',end='')
    if f.find(f'*(x**{index}) ') > 1:
      if f[f.find(f'*(x**{index}) ')-2] != ' ':
        x = int(f[f.find(f'*(x**{index}) ')-2] + f[f.find(f'*(x**{index}) ')-1])
      else:
        x = int(f[f.find(f'*(x**{index}) ')-1])
    else:
        x = int(f[f.find(f'*(x**{index}) ')-1])
    return x

def file3(f1:str,f2:str):
    for i in range(0, 9):
        if f1[i] == '(':
            count = int(f1[i+4])
    for i in range(count, 0, -1):
        if f1.find(f'*(x**{i}) ') != -1:
            k1 = kof(f1, i)
            print(f'k1 = {k1}')
        else:
            k1=0
        if f2.find(f'*(x**{i}) ') != -1:
            k2 = kof(f2, i)
            print(f'k2 = {k2}')
        else:
            k2=0
        with open('mas3.txt', 'a') as file:
            if k1 !=0 or k2 !=0:
                file.write(f'{k1+k2}*(x**{i}) + ')
    if f1[f1.find(f' =')-2] != ' ' and f1[f1.find(f' =')-1] != ')':
        k1 = int(f1[f1.find(f' =')-2]+f1[f1.find(f' =')-1])
    elif f1[f1.find(f' =')-1] != ')':
        k1 = int(f1[f1.find(f' =')-1])
    else:
        k=0
    if f2[f2.find(f' =')-2] != ' ' and f2[f2.find(f' =')-1] != ')':
        k2 = int(f2[f2.find(f' =')-2]+f2[f2.find(f' =')-1])
    elif f2[f2.find(f' =')-1] != ')':
        k2 = int(f2[f2.find(f' =')-1])
    else:
        k2=0

    with open('mas3.txt', 'a') as file:
        if k1 !=0 or k2 !=0:
            file.write(f'{k1+k2} = 0')
    
with open('mas1.txt', 'w') as file:
    file.write('')
with open('mas2.txt', 'w') as file:
    file.write('')
with open('mas3.txt', 'w') as file:
    file.write('')
insert_file('mas1.txt')
file1 = open_file('mas1.txt', str())
insert_file('mas2.txt')
file2 = open_file('mas2.txt', str())

print(file1)
print(file2)
if file1 != '0' and file2 != '0':
    if len(file1)>=len(file2):
        file3(file1,file2)
    else:
        file3(file2,file1)
else:
    print(f'Упс... Одно из складываемых множеств оказалось равно 0... попробуй ещё раз))')
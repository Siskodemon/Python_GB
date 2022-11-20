# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and
# ⋁ - or
# ¬ - not
# Переменные X, Y и Z могут принемать значения 1 или 0

X = False
Y = False
Z = False
a = not (X or Y or Z)
b = not X and not Y and not Z
while not (X != 0 and Y !=0 and Z != 0):
#    print(not (X or Y or Z))
#    print(not X and not Y and not Z)
    print(f'not({X} or {Y} or {Z}) = not({X}) and not({Y}) and not ({Z}) == > {a == b}')
    if Z == False:
        Z = True
    elif Y == False:
        Y = True
        Z = False
    else:
        X = True
        Y = False
        Z = False
#print(not (X or Y or Z))
#print(not X and not Y and not Z)
print(f'not({X} or {Y} or {Z}) = not({X}) and not({Y}) and not ({Z}) == > {a == b}')

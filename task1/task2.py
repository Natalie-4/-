# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and, ⋁ - or, ¬ - not

print('Для каждой переменной введите значение на выбор: 0 или 1')
X = bool(input())
Y = bool(input())
Z = bool(input())

if (X == 1 or X == 0) and (Y == 1 or Y == 0) and (Z == 1 or Z == 0):
    print(f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z -> {(not (X or Y or Z)) == ((not X) and (not Y) and (not Z))}')
else:
    print('введено неверно')
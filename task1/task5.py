# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

Ax = float(input('Введите координату x точки A: '))
Ay = float(input('Введите координату y точки A: '))
Bx = float(input('Введите координату x точки B: '))
By = float(input('Введите координату y точки B: '))

distanceAB = ((Ax - Bx)**2 + (Ay - By)**2)**0.5

print(f'Расстояние между точками A и B равно {distanceAB}')
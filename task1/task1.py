# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите число, соответствующее дню недели, от 1 до 7')
N = int(input())

if 1<= N <= 7:
    if N == 7 or N == 6:
        print('выходной')
    else:
        print('нет')
else:
    print('Попробуйте ещё раз')
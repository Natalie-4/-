# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quarter = input('введите номер координатной четверти: ')
if quarter == 'I':
    print('x > 0, y > 0')
elif quarter == 'II':
    print('x < 0, y > 0')
elif quarter == 'III':
    print('x < 0, y < 0')
elif quarter == 'IV':
    print('x > 0, y < 0')
else:
    print('введено неверно')
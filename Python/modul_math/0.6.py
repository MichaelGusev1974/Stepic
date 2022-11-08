# Квадратное уравнение 🌶️🌶️
# Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения
# ax^2 + bx + c = 0.

# Формат входных данных
# На вход программе подается три вещественных числа a != 0,b,c, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
#
# Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

from math import *
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    print(- b / (2 * a))
elif d > 0:
    x1 = (-b + sqrt(d))/(2 * a)
    x2 = (-b - sqrt(d))/(2 * a)
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    print(min_x)
    print(max_x)
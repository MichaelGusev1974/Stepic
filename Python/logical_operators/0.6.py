# Ход короля 🌶️
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
#
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
#
#
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 4
# 4
# 5
# 5
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 4
# 4
# 5
# 4
# Sample Output 2:
#
# YES
# Sample Input 3:
#
# 4
# 4
# 2
# 4
# Sample Output 3:
#
# NO

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((c - 1) <= a <= (c + 1)) and ((d - 1) <= b <= (d + 1)):
    print('YES')
else:
    print('NO')
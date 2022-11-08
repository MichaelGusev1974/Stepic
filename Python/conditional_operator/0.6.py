# Арифметическая прогрессия
# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными
# членами арифметической прогрессии.
#
# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1
# 2
# 3
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 1
# 2
# 4
# Sample Output 2:
#
# NO
# Sample Input 3:
#
# 2
# 4
# 8
# Sample Output 3:
#
# NO

a = int(input())
b = int(input())
c = int(input())
if b - a == c - b:
    print('YES')
else:
    print('NO')
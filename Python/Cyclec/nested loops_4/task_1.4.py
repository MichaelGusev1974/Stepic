# Таблица-3
# Дано натуральное число n  (n ≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n
# в соответствии с примером.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести таблицу сложения для всех чисел от 1 до n.
#
# Примечание. В конце строки может быть пробел.

n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j,)
    print()
# вывод:

# 2 - это n
# 1 + 1 = 2
# 1 + 2 = 3
# 1 + 3 = 4
# 1 + 4 = 5
# 1 + 5 = 6
# 1 + 6 = 7
# 1 + 7 = 8
# 1 + 8 = 9
# 1 + 9 = 10
#
# 2 + 1 = 3
# 2 + 2 = 4
# 2 + 3 = 5
# 2 + 4 = 6
# 2 + 5 = 7
# 2 + 6 = 8
# 2 + 7 = 9
# 2 + 8 = 10
# 2 + 9 = 11
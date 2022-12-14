# Звездный треугольник 🌶️🌶️
# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n в соответствии с примером:
#
# *
# **
# ***
# ****
# ***
# **
# *
# Формат входных данных
# На вход программе подается одно нечетное натуральное число.
#
# Формат выходных данных
# Программа должна вывести треугольник в соответствии с условием.
#
# Примечание. Используйте вложенный цикл for.
n = int(input())
for i in range(n // 2):
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(n // 2, 0, -1):
    for j in range(i - 1):
        print('*', end='')
    print()

# 8 - это n, вывод: 

# *
# **
# ***
# ****
# ***
# **
# *
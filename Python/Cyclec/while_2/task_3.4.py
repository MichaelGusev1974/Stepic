# Пока делимся
# На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке.
# Концом последовательности является любое число не делящееся на 7. Напишите программу, которая выводит члены данной
# последовательности.
#
# Формат входных данных
# На вход программе подается последовательность чисел, каждое число на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести члены данной последовательности.

# n = int(input())
# while n % 7 == 0:
#     print(n)
#     n = int(input())

# Сумма чисел

# На вход программе подается последовательность целых чисел, каждое число на отдельной строке. Концом последовательности
# является любое отрицательное число. Напишите программу, которая выводит сумму всех членов данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность чисел, каждое число на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сумму членов данной последовательности

# n = int(input())
# counter = 0
# while n >= 0:
#     counter += n
#     n = int(input())
# print(counter)

# Количество пятерок
# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на
# отдельной строке. Концом последовательности является любое отрицательное число, либо число большее 5.
# Напишите программу, которая выводит количество пятерок.
#
# Формат входных данных
# На вход программе подается последовательность чисел, каждое число на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести количество пятерок.

n = int(input())
counter = 0
while 0 < n <= 5:
    if n == 5:
        counter += 1
    n = int(input())
print(counter)
# Площадь треугольника
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
#
#
#
# Формат входных данных
# На вход программе подаётся два числа с плавающей точкой – длины катетов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести одно число – площадь треугольника.

a = float(input())
b = float(input())
print(1/2 * a * b)

# Две старушки
# Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч. Определите, через какое время старушки
# встретятся, если расстояние между ними равно S км.

# Формат входных данных
# На вход программе подаются три числа с плавающей точкой S, V1, V2, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести одно число в соответствии с условием задачи.
#
# Примечание. Это очень быстрые старушки.

S = float(input())
V1 = float(input())
V2 = float(input())
print(S / (V1 +V2))

# Обратное число

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с
# клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

# Формат входных данных
# На вход программе подается одно действительное число.
#
# Формат выходных данных
# Программа должна вывести действительное число обратное данному, либо текст в соответствии с условием задачи.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 2.5
# Sample Output 1:
#
# 0.4
# Sample Input 2:
#
# -55.6
# Sample Output 2:
#
# -0.017985611510791366
# Sample Input 3:
#
# 0
# Sample Output 3:
#
# Обратного числа не существует

n = float(input())
if n == 0:
    print('Обратного числа не существует')
else:
    print(n ** (-1))
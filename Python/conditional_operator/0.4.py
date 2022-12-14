# Соотношение
# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.
#
# Формат входных данных
# На вход программе подаётся одно целое положительное четырёхзначное число.
#
# Формат выходных данных
# Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1614
# Sample Output 1:
#
# ДА
# Sample Input 2:
#
# 1234
# Sample Output 2:
#
# НЕТ
# Sample Input 3:
#
# 7911
# Sample Output 3:
#
# ДА

n = int(input())
if ((n % 10) + (n % 10 ** 4) // 10 ** 3) == ((n % 10 ** 3) // 10 ** 2) - (n % 10 ** 2) // 10:
    print('ДА')
else:
    print('НЕТ')

num = int(input())
a = num % (10 ** 4) // 10 ** 3
b = num % (10 ** 3) // 10 ** 2
c = num % (10 ** 2) // 10 ** 1
d = num % 10
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')
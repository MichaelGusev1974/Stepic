# Значение функции
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции f(x) = x**2 + 2x + 1, каждое на
# отдельной строке.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.
#
# Примечание. Для первого теста имеем:
# f(1) = 1**2 + 2*1 + 1 = 4, f(2) = 2**2 + 2*2 + 1 = 9,  f(3) = 3**2 + 2*3 + 1 = 16, ......
n = int(input())
ls = []
for i in range(n):
    x = int(input())
    print(x)
    ls.append(x)
print()
ls2 = []
for x in range(len(ls)):
    f = ls[x] ** 2 + 2 * ls[x] + 1
    ls2.append(f)
    print(f)

# вход: 3 - это n; 10, 20, 30
# выход:
# 10
# 20
# 30
#
# 121
# 441
# 961

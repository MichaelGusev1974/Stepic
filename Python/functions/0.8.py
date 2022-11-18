# Делители 1
# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех
# делителей данного числа.
#
# Примечание. Следующий программный код:
#
# print(get_factors(1))
# print(get_factors(5))
# print(get_factors(10))
# должен выводить:
#
# [1]
# [1, 5]
# [1, 2, 5, 10]
# Тестовые данные 🟢
# 1 вариант
# def get_factors(num):
#     Ls = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             Ls.append(i)
#     return Ls
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))

# 2 вариант
def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]
n = int(input())
print(get_factors(n))

# Делители 2
# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей
# данного числа.
#
# Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.
#
# Примечание 2. Следующий программный код:
#
# print(number_of_factors(1))
# print(number_of_factors(5))
# print(number_of_factors(10))
# должен выводить:
#
# 1
# 2
# 4
# Тестовые данные 🟢

# объявление функции
def number_of_factors(num):
    return len([n for n in range(1, num + 1) if num % n == 0])

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
# Сумма цифр
# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 12345
# Sample Output 1:
#
# 15
# Sample Input 2:
#
# 12
# Sample Output 2:
#
# 3
# Sample Input 3:
#
# 7
# Sample Output 3:
#
# 7

# 1
# объявление функции
def print_digit_sum(num):
    ls = [int(i) for i in str(num)]
    print(sum(ls))

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)

# 2.
def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))

n = int(input())

print_digit_sum(n)
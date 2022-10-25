# Все вместе
# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке.

n = int(input())
counter_sum = 0
counter = 0
counter_mult = 1
copy_n = n

while n != 0:
    num = n % 10
    counter += 1
    counter_sum += num
    counter_mult *= num
    n //= 10

first_didgit = copy_n // 10 ** (counter - 1)
last_didgit = copy_n % 10

print(counter_sum)
print(counter)
print(counter_mult)
print(counter_sum / counter)
print(first_didgit)
print(first_didgit + last_didgit)




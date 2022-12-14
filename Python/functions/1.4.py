# Next Prime 🌶️🌶️
# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
#
#  Примечание 2. Следующий программный код:
#
# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))
# должен выводить:
#
# 7
# 11
# 17
# Тестовые данные 🟢

def is_prime(num):
    if len([i for i in range(1, num + 1) if num % i == 0]) == 2:
        return True
    else:
        return False


def get_next_prime(num):
    x = num + 1
    while is_prime(x) == False:
        x += 1
    else:
        return x

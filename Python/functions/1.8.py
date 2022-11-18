# BEEGEEK
# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
# фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
#
#  Примечание. Следующий программный код:
#
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))
#
# должен выводить:
#
# True
# False
# False
# False
#
#
# Тестовые данные 🟢
# Sample Input:
#
# 15551:7:290
# Sample Output:
#
# True

# объявление функции
def is_valid_password(password):
    password = password.split(':')
    a = password[0]
    b = int(password[1])
    c = int(password[2])
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    if len(password) == 3:
        flag1 = True
    if a[:] == a[::-1]:
        flag2 = True
    for i in range(2, b):
        if b % i == 0:
            break
    else:
        flag3 = True
    if c % 2 == 0:
        flag4 = True
    return flag1 and flag2 and flag3 and flag4
# считываем данные
psw = input()
# вызываем функцию
print(is_valid_password(psw))
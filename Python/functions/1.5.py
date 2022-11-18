# Good password 🌶️
# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 88 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
#  Примечание. Следующий программный код:
#
# print(is_password_good('aabbCC11OP'))
# print(is_password_good('abC1pu'))
# должен выводить:
#
# True
# False
# Тестовые данные 🟢

# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
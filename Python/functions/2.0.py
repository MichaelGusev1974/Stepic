# Змеиный регистр

# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
# и преобразует его в «змеиный регистр».
#
# Примечание 1. Почитать подробнее о стилях именования можно тут.
#
# Примечание 2. Следующий программный код:
#
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))
# должен выводить:
#
# this_is_camel_cased
# is_prime_number
# Тестовые данные 🟢
# Sample Input:
#
# ThisIsCamelCased
# Sample Output:
#
# this_is_camel_cased


# объявление функции
def convert_to_python_case(text):
    s = []
    for i in range(len(text)):
        if text[i].isupper():
            s.append('_')
            s.append(text[i].lower())
        else:
            s.append(text[i].lower())
    s = ''.join(s[1:])
    return s
# считываем данные
txt = input()
# вызываем функцию
print(convert_to_python_case(txt))
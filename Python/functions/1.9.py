# Правильная скобочная последовательность 🌶️
# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из
# символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной
# последовательностью и False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где
# каждой открывающей скобке найдется парная закрывающая скобка.
#
# Примечание 2. Следующий программный код:
#
# print(is_correct_bracket('()(()())'))
# print(is_correct_bracket(')(())('))
# должен выводить:
#
# True
# False
# Тестовые данные 🟢
# Sample Input:
#
# ((()))
# Sample Output:
#
# True
# 1 способ
# объявление функции
def is_correct_bracket(text):
    counter = 0
    for i in text:
        if i == '(':
            counter += 1
        if i == ')':
            counter -= 1
    if counter == 0:
        return True
    else:
        return False
# считываем данные
txt = input()
# вызываем функцию
print(is_correct_bracket(txt))


# 2 способ
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()','')
    if len(text) == 0:
        return True
    else:
        return False
# считываем данные
txt = input()
# вызываем функцию
print(is_correct_bracket(txt))
# Найти всех
# Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке.
# Проблема заключается в том, что данный метод не находит местоположение всех символов а.
#
# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и
# возвращает список, содержащий все местоположения этого символа в строке.
#
# Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.
#
# Примечание 2. Следующий программный код:
#
# print(find_all('abcdabcaaa', 'a'))
# print(find_all('abcadbcaaa', 'e'))
# print(find_all('abcadbcaaa', 'd'))
# должен выводить:
#
# [0, 4, 7, 8, 9]
# []
# [4]
# Тестовые данные 🟢
# 1 вариант
# объявление функции
def find_all(target, symbol):
    Ls = []
    for i in range(len(target)):
        if target[i] == symbol:
            Ls.append(i)
    return Ls
# считываем данные
s = input()
char = input()
# вызываем функцию
print(find_all(s, char))

# 2 вариант

# объявление функции
def find_all(target, symbol):
    return [x for x in range(len(target)) if target[x] == symbol]
# считываем данные
s = input()
char = input()
# вызываем функцию
print(find_all(s, char))
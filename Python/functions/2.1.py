# Звездный треугольник 🌶️
# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием и высотой равными
# 15 и 8 соответственно:
#
#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************
# Примечание 1 . Для вывода треугольника используйте цикл for.
#
# Примечание 2 . Справа от звездочек пробелов нет.
#
# Тестовые данные 🟢
# объявление функции
def draw_triangle():
    for i in range(1, 9):
        stroka = (" " * (8 - i)) + ("*" * (i + (i - 1)))
        print(stroka)


draw_triangle()  # вызов функции
# Is Valid Triangle?
# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных
# числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.
#
# Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.
#
# Примечание 2. Следующий программный код:
#
# print(is_valid_triangle(2, 2, 2))
# print(is_valid_triangle(2, 3, 10))
# print(is_valid_triangle(3, 4, 5))
# должен выводить:
#
# True
# False
# True
# Тестовые данные 🟢

def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else:
        return False
print(is_valid_triangle(2, 3, 10))
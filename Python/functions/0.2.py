# Звездный треугольник 1
# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10 в
# соответствии с образцом:
#
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# Примечание. Для вывода треугольника используйте цикл for.
#
# Тестовые данные 🟢

def draw_triangle():
    for i in range(1,11):
        print('*' * i)
draw_triangle()
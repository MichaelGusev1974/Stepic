# Цикл for VS цикл while

# Мы всегда можем заменить цикл for с помощью цикла while. Следующие две программы выводят числа от 0 до 100:
# используем for
for i in range(101):
    print(i)

# используем while
i = 0
while i < 101:
    print(i)
    i += 1

# В первом цикле переменная i последовательно принимает значения от 0 до 100. Для цикла while, нам пришлось завести
# самостоятельно переменную i и придать ей начальное значение. Тело цикла while содержит аналогичную инструкцию вывода
# print(i), однако помимо этого мы самостоятельно увеличиваем значение переменной i на 1, что делается автоматически
# в случае с циклом for.
#
# Напишем программу, выводящую все числа, кратные 3, используя цикл for и while:

# используем for
for i in range(0, 100, 3):
    print(i)

# используем while
i = 0
while i < 100:
    print(i)
    i += 3
# Не всегда, однако удается заменить цикл while с помощью цикла for. Если заранее не известно количество итераций,
# то необходимо использовать цикл while и только его.
# Операторы break и continue во вложенных циклах

# Оператор break выполняет прерывание ближайшего цикла в котором он расположен. Аналогично, оператор continue
# осуществляет переход на следующую итерацию ближайшего цикла.
#
# Рассмотрим программный код:

for i in range(3):
    for j in range(3):
        print(i, j)
# Результатом его выполнения будут 9 строк:
#
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# Изменим код, добавив во вложенный цикл условный оператор с оператором break:

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

# Результатом выполнения нового кода будут 3 строки:
#
# 1 0
# 2 0
# 2 1

# Изменим оператор прерывания break на оператор continue:

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)

# Результатом выполнения нового кода будут 6 строк:
#
# 0 1
# 0 2
# 1 0
# 1 2
# 2 0
# 2 1

# Если необходимо добиться прерывания внешнего цикла из-за выполнения условия во внутреннем,
# то стоит сделать это через сигнальную метку.
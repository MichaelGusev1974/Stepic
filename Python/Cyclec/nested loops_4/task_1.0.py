# Вложенные циклы

# Рассмотрим цикл, который частично моделирует электронные часы. Он показывает секунды от 0 до 59:

# for seconds in range(60):
#     print(seconds)

# Можно добавить переменную minutes и вложить цикл написанный выше внутрь еще одного цикла, который повторяется 60 раз:

# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds)

# Для того, чтобы сделать модель законченной, можно добавить еще одну переменную для подсчета часов:

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)


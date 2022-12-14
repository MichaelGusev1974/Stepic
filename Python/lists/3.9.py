# Сортировка простыми вставками
# Алгоритм сортировки простыми вставками делит список на 2 части — отсортированную и неотсортированную.
# Из неотсортированной части извлекается очередной элемент и вставляется на нужную позицию, в результате чего
# отсортированная часть списка увеличивается, а неотсортированная уменьшается. Так происходит, пока не исчерпан набор
# входных данных и не отсортированы все элементы.
#
# Сортировка простыми вставками наиболее эффективна когда список уже частично отсортирован и элементов массива немного.
# Если элементов в списке меньше 10, то этот алгоритм — один из самых быстрых.
#
# Рассмотрим его работу на примере сортировки списка a = [5, 1, 8, 2, 4] по возрастанию.

# Первый проход:
# Делим список на две части: отсортированную [5] и неотсортированную [1, 8, 2, 4].
# Извлекаем первый элемент 1 из неотсортированной части списка и находим ему место в отсортированной части:
# [1, 5, 4, 2, 8].
#
# Второй проход:
# Делим список на две части: отсортированную [1, 5] и неотсортированную [8, 2, 4].
# Извлекаем первый элемент 8 из неотсортированной части списка и находим ему место в отсортированной части:
# [1, 5, 8, 2, 4].
#
# Третий проход:
# Делим список на две части: отсортированную [1, 5, 8] и неотсортированную [2, 4].
# Извлекаем первый элемент 2 из неотсортированной части списка и находим ему место в отсортированной части:
# [1, 2, 5, 8, 4].
#
# Четвертый проход:
# Делим список на две части: отсортированную [1, 2, 5, 8] и неотсортированную [4].
# Извлекаем первый элемент 4 из неотсортированной части списка и находим ему место в отсортированной части:
# [1, 2, 4, 5, 8].
#
# Теперь список отсортирован и алгоритм может быть завершен.



# Реализация алгоритма

# Пусть требуется отсортировать по возрастанию список чисел: a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99].
#
# Следующий программный код реализует алгоритм сортировки простыми вставками:
#
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem
#
#
# print('Отсортированный список:', a)
# Результатом выполнения такого кода будет:
#
# Отсортированный список: [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]
# Оптимизация алгоритма
# Алгоритм сортировки простыми вставками можно значительно ускорить, если осуществлять поиск нужной позиции для
# вставки очередного элемента из неотсортированной части списка с помощью бинарного поиска.

a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
print('Начинаем цикл перебора всех элементов списка, начиная со второго (неотсортированный список)')
for i in range(1, n):
    print(a, i, 'итерация: a[i] =', a[i])
    elem = a[i]  # первый элемент из неотсортированной части списка
    print('Запоминаем проверяемый элемент списка в доп память - elem = a[i] =', a[i])
    j = i
    if a[j - 1] <= elem:
        print(f'В while не заходим, тк проверяемое число ({a[i]}) больше предыдущего ({a[i - 1]})')
    while j >= 1 and a[j - 1] > elem:
        print(f'while: сравниваем индекс = {j}: на место a[j] = {a[j]} записываем число {a[j - 1]}, и получаем', end=' ')
        a[j] = a[j - 1]
        print(a)
        j -= 1
    print(f'Извлекаем из доп памяти elem = {elem} в индекс {j}')
    a[j] = elem

print(a)
#_______________________________________________________________________________________________________________________
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
n = len(a)

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break
print(a)
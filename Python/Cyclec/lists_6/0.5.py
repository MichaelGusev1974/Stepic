# Алфавит
# Напишите программу, выводящую следующий список:
#
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
# Формат выходных данных
# Программа должна вывести указанный список.
#
# Примечание. Последний элемент списка состоит из 26 символов z
ls = []
mult = 0
for i in range(97, 123):
    mult += 1
    simb = chr(i) * mult
    ls.append(simb)
print(ls)



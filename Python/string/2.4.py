# Первое и последнее вхождение
# На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке, разделенных
# символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

s = input()
if s.count('f') == 1:
    print(s.find('f'))
if s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
if s.count('f') == 0:
    print('NO')

# пример ввода s: abcdefgfhfabc
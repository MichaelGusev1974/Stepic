# Построчный вывод
# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# ввод: У лукоморья дуб зеленый златая цепь на дубе том
s = input()
s = s.split()
print(*s, sep='\n')
# вывод:
# У
# лукоморья
# дуб
# зеленый
# златая
# цепь
# на
# дубе
# том
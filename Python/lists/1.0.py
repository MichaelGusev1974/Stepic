# k-ая буква слова 🌶️🌶️
# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая
# выводит k-ую букву из введенных строк на одной строке без пробелов.
#
# Формат входных данных
# На вход программе подается натуральное число n, далее n строк, каждая на отдельной строке.
# В конце вводится натуральное число k – номер буквы (нумерация начинается с единицы).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при
# выводе нужно игнорировать.

n = int(input())
ls = []
for i in range(n):
    s = input()
    ls.append(s)
k = int(input())
s1 = ''
s2 = ''
for i in range(n):
    if len(ls[i]) >= k:
        s1 = ls[i][k - 1]
        s2 += s1
print(s2)

# 5
# abcdef
# bcdefg
# cdefgh
# defghi
# efghij
# 2

# 1) Вводим переменную n через input
# 2) Создаем пустой список. Я назвал его list
# 3) Первый цикл for i в range(n):
# вводим переменные строк в цикле через input(я назвал её a')
# добавляем через append поочередно каждую переменную к списку list
# цикл закрыт
# 4) Вводим переменную k через input
# 5) Вводим поочередно две пустых строки x1 и x2(позже поймете, зачем они нужны)
# 6) Запускаем второй цикл for j в range(n):
# Теперь исключаем неподходящие нам по условию задачи строки. В цикле вводим условие: если длина элемента нашего
# списка list[j] больше или равна k.
# Чтобы вывести нужную нам букву и добавить ее в строку, пользуемся индексами, в моем случае это  x1 = list[j][k - 1].
# Теперь остается только в уже созданную переменную добавлять x1.
# x2 += x1
# 7)Выводим на экран x2

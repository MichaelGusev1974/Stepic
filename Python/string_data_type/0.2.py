# Три города
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
#
# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
#
# Примечание. Гарантируется, что длины названий всех трех городов различны.
a = input()
b = input()
c = input()
a1 = len(a)
b1 = len(b)
c1 = len(c)
min_city = min(a1, b1, c1)
max_city = max(a1, b1, c1)
if min_city == a1 and max_city == b1:
    print(a, b, sep='\n')
elif min_city == a1 and max_city == c1:
    print(a, c, sep='\n')
elif min_city == b1 and max_city == a1:
    print(b, a, sep='\n')
elif min_city == b1 and max_city == c1:
    print(b, c, sep='\n')
elif min_city == c1 and max_city == a1:
    print(c, a, sep='\n')
elif min_city == c1 and max_city == b1:
    print(c, b, sep='\n')
# В одну строку 2
# На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая выводит все
# цифровые символы данной строки.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Программу можно написать в одну строку кода.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# Число Pi примерно равно 3.1415
# Sample Output 1:
#
# 31415
# Sample Input 2:
#
# 123Python awesome!56
# Sample Output 2:
#
# 12356

print(*[s for s in input() if '0' <= s <= '9'], sep='')
print(*[i for i in input() if i in "0123456789"], sep = "")
print(*(i for i in input() if i.isdigit()), sep="")
print(''.join([i for i in input() if i.isdigit()]))
# Символы в диапазоне
# На вход программе подаются два числа a и b. Напишите программу, которая для каждого кодового значения в диапазоне от
# a до b (включительно), выводит соответствующий ему символ из таблицы символов Unicode.
#
# Формат входных данных
# На вход программе подается два натуральных числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

a = int(input())
b = int(input())
for i in range(a, b + 1):
    simb = chr(i)
    print(simb, end=' ')

# пример ввода: 65  70
# вывод:  A B C D E F 
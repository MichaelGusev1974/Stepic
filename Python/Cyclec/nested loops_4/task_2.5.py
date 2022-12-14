# Цифровой корень
# На вход программе подается натуральное число n. Напишите программу, которая находит цифровой корень данного числа.
# Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа,
# затем взять все цифры найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра),
# которое и называется цифровым корнем данного числа.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести цифровой корень введенного числа.
#
# Примечание. Используйте вложенные циклы while.

#n = int(input())
# sum_num1 = 0
# sum_num2 = 0
# num1 = 0
# num2 = 0
# while n > 9:
#     num1 = n % 10
#     sum_num1 += num1
#     n //= 10
# while sum_num1 > 0:
#     num2 = sum_num1 % 10
#     sum_num2 += num2
#     sum_num1 //= 10
# print(sum_num2)
n = int(input())
while n > 9:              # задаем условие while > 9:
    total = 0             # пропишем новую переменную, например total = 0
    while n > 0:          # задаем еще одно условие: while > 0:
        num = n % 10      # ищем последнюю цифру: num = n %10  ,
        total += num      # дальше прибавляем ее к новой переменной - total += num
        n //= 10          # добавим n //=10, что бы цикл не стал бесконечным
    n = total             # в конце под первым условием добавим еще одну важную строку:  n = total
print(n)




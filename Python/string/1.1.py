# Делаем срезы 1
# На вход программе подается одна строка. Напишите программу, которая выводит:
#
# общее количество символов в строке;
# исходную строку повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.

s = input()
counter = 0
for i in range(len(s)):
    counter += 1
print(counter)
print(s * 3)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:-1])
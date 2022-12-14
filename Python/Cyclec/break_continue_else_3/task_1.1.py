# Напишем программу, использующую цикл for, которая считывает 10 чисел и суммирует их до тех пор, пока не обнаружит
# отрицательное число. В этом случае выполнение цикла прерывается командой break:

num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    num //= 10

if flag == True:
    print('Число', number, 'содержит цифру 7')
else:
    print('Число', number, 'не содержит цифру 7')

# Как только мы встретили цифру 7, мы меняем значение сигнальной метки и прерываем цикл с помощью оператора break.
# Мы можем и не прерывать цикл преждевременно, а дождаться его естественного завершения (условие num != 0, то есть все
# цифры числа обработаны), однако в таком случае мы будем совершать лишнюю работу, и в случае если число очень большое,
# то программа будет работать медленнее.
# ФИО
# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.
#
# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# Александр
# Пушкин
# Сергеевич
# Sample Output 1:
#
# ПАС
# Sample Input 2:
#
# тимур
# Гуев
# ахсарбекович
# Sample Output 2:
#
# ГТА
# 1.
# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
# 2.
def print_fio(name, surname, patronymic):
    [print(m[0].upper(),end='') for m in [surname,name,patronymic]]
# считываем данные
name, surname, patronymic = input(), input(), input(),
# вызываем функцию
print_fio(name, surname, patronymic)

# 3.
# объявление функции
def print_fio(name, surname, patronymic):
    print(*[i[0].upper() for i in [surname, name, patronymic]], sep='')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
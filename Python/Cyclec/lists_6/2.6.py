# Все сразу 2 🌶️
# Дополните приведенный код, чтобы он:
#
# Заменил второй элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print()

numbers = [8, 9, 10, 11]
numbers[1] = 17
print(numbers)
numbers.append(4)
numbers.append(5)
numbers.append(6)
print(numbers)
numbers.remove(8)
print(numbers)
numbers.extend(numbers)
print(numbers)
numbers.insert(3, 25)
print(numbers)
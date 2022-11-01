# Дополните приведенный код, используя списочное выражение так, чтобы получить новый список, содержащий строки исходного
# списка с удаленным первым символом.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
            'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m[1:] for m in keywords]
print(new_keywords)

# Дополните приведенный код, используя списочное выражение так, чтобы получить новый список, содержащий длины строк
# исходного списка.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
            'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(m) for m in keywords]
print(lengths)

# Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной не менее
# пяти символов (включительно).

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
            'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m for m in keywords if len(m) >= 5]
print(new_keywords)

# Дополните приведенный код, используя списочное выражение так, чтобы получить список всех чисел палиндромов от 100 до 1000.

palindromes = [i for i in range(100, 1000) if i % 10 == i // 100]
print(palindromes)
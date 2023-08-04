# Напишите программу, которая получает на вход список чисел и выводит на экран сумму их квадратов.
def func1(l):
    return sum([i ** 2 for i in l])


# Напишите программу, которая получает на вход строку и выводит на экран все слова, начинающиеся на букву "a".
def func2(s):
    return [i for i in s.split() if i[0] == 'a']


# Напишите программу, которая получает на вход два списка чисел и выводит на экран их общие элементы.
def func3(a, b):
    return [i for i in a if i in b]


# Напишите программу, которая получает на вход словарь с именами и возрастами людей, и выводит на экран имена всех
# людей, возраст которых больше 18 лет.
def func4(d):
    return [names for names, age in d.items() if age > 18]


# Напишите программу, которая получает на вход список строк и выводит на экран самую длинную строку в списке.
def func5(s):
    return max(s.split(), key=len)


# Напишите программу, которая получает на вход список чисел и возвращает список из тех же чисел, но без повторений.
def func6(a):
    return list(set(a))


# Напишите программу, которая получает на вход два списка чисел и возвращает список из всех элементов,
# которые есть только в одном из списков.
def func7(a, b):
    return [i for i in a if i not in b]


# Напишите программу, которая получает на вход список слов и выводит на экран количество различных слов в списке.
def func8(a):
    return len(set(a))


# Напишите программу, которая получает на вход строку и выводит на экран все символы,
# которые встречаются в ней более одного раза.
def func9(s):
    s = sorted(s.replace(' ', ''))
    result = []
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            result.append(s[i])
    return result


def func9new(s):
    s = sorted(s.replace(' ', ''))
    return [s[i] for i in range(len(s) - 1) if s[i] != s[i + 1]]


# Напишите программу, которая получает на вход список чисел и возвращает новый список,
# в котором все числа умножены на 2.
def func10(a):
    return [i * 2 for i in a]


# Напишите программу, которая получает на вход два списка чисел и возвращает список из всех элементов,
# которые есть в обоих списках.
def func11(a, b):
    return a + b


# Напишите программу, которая получает на вход список чисел и возвращает новый список,
# в котором все отрицательные числа заменены на нули.
def func12(a):
    return [i if i > 0 else 0 for i in a]


# Напишите программу, которая получает на вход два списка строк и возвращает список из всех пар строк,
# одна из которых из первого списка, а другая - из второго списка.
def func13(a, b):
    return list(zip(a, b))


# Напишите программу, которая получает на вход словарь и возвращает новый словарь,
# в котором ключи и значения поменяны местами.
def func14(d):
    return {value: key for key, value in d.items()}


# Напишите программу, которая получает на вход список чисел и выводит на экран наибольшее из них.
def func15(a):
    return max(a)
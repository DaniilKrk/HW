__author__ = 'Крюков Даниил'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

a = 1234
i = len(str(a)) - 1
while i != -1:
    print(int(a/10 ** i))
    a = a - (int((a/10 ** i))*(10 ** i))
    i = i - 1


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input("Введите значение a ")
b = input("Введите значение b ")
c = a
a = b
b = c
print("a = ", a, "b = ", b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


while True:
    age = input("Вам уже есть 18? (Y/N)")
    if age == 'Y':
        print("Доступ разрешен")
        break
    elif age == 'N':
        print("Извините, пользование данным ресурсом только с 18 лет")
        break
    print("Неизвестный ответ")

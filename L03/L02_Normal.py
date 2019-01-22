# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def doing_magic(x, y):
        x = x + y
        y = x - y
        return x, y
    x = 1
    y = 0
    for z in str(n) * (n - 1):
        x, y = doing_magic(x, y)
    output = [x]
    for z in str(n) * (m - n):
        x, y = doing_magic(x, y)
        output.append(x)
    return output

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

import random

def sort_to_max(origin_list):
    if len(origin_list) <= 1:
       return origin_list
    else:
        q = random.choice(origin_list)
    lower = [i for i in origin_list if i < q]
    eq = [q] * origin_list.count(q)
    bigger = [i for i in origin_list if i > q]
    return sort_to_max(lower) + eq + sort_to_max(bigger)

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, a):
    result = ''
    for item in a:
        if func(item) == True:
            result += str(item)
    return iter(result)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def math_magic(x):

    # Делим исходное выражение на целые и дробные части. От выражения 1 5/6 + 4/7 мы получим ('1', '5/6', '4/7', 0)
    def decompos(x):
            # Меняем '' на нули, если целых частей изначально нет.
            def space_check(x):
                if x == '':
                    x = 0
                return x
            x = x.split()
            if len(x) == 5:
                i = iter((0, 3))
            elif len(x) == 4:
                i = iter((0, 2, 3))
            else:
                i = iter((0, 2))
            a = a2 = c = b = b2 = ''
            for item in i:
                try:
                    if x[item].find('/') == (-1) and int(x[item]) != 0:
                        if a == '' and item == 0:
                            a = x[item]
                        else:
                            b = x[item]
                except ValueError:
                    pass
            for item in x:
                if item.find('/') != -1 and a2 == '' and item != a:
                    a2 = item
                elif item.find('/') != -1 and a2 > '' and item != b:
                    b2 = item        
            return (a2, space_check(a), b2, space_check(b))

    # Получаем из дроби числитель и знаменатель в int
    def decompos_light(x):
        result = fract = '0'
        count = 0
        for item in x:
            if item.find('/') != -1:
                count = 1
            elif count == 0:
                result = result + item
            elif count == 1:
                fract = fract + item
        result = int(result)
        fract = int(fract)
        return result, fract
    
    # Приводим 2 дроби к одному знаменателю
    def generalization(a, x, b, y):
        if a == 0 or b == 0:
            return(a, b, x)
        a = a * y
        b = b * x
        x = x * y
        for i in range(len(str(x))):
            for i in range(x):
                i += 1
                if a / i == a // i and b / i == b // i and x / i == x // i:
                    a = a // i
                    b = b // i
                    x = x // i
        return a, b, x

    # Складываем         
    def addition(x):
        a2, a, b2, b = decompos(x)
        integ = int(a) + int(b)
        a2, x = decompos_light(a2)
        b2, y = decompos_light(b2)
        a2, b2, fraction = generalization(a2, x, b2, y)
        float_part = a2 + b2
        while True:
            if float_part > fraction:
                float_part -= fraction
                integ += 1
            else:
                break
        # Еще раз упрощаем
        for i in range(fraction):
            i += 1
            if float_part / i == float_part // i and fraction / i == fraction // i:
                    float_part = float_part // i
                    fraction = fraction // i
        if integ != 0 and float_part != 0:
            result = str(integ)+" "+str(float_part)+"/"+str(fraction)
        elif float_part != 0:
            result = str(float_part)+"/"+str(fraction)
        else:
            result = str(integ)
        return result

    # Вычитаем    
    def subtraction(x):
        a2, a, b2, b = decompos(x)
        integ = int(a) - int(b)
        a2, x = decompos_light(a2)
        b2, y = decompos_light(b2)
        a2, b2, fraction = generalization(a2, x, b2, y)
        float_part = a2 - b2
        while True:
            if float_part > fraction:
                float_part -= fraction
                integ += 1
            else:
                break
        # Еще раз упрощаем
        for i in range(fraction):
            i += 1
            if float_part / i == float_part // i and fraction / i == fraction // i:
                    float_part = float_part // i
                    fraction = fraction // i
        if integ != 0 and float_part != 0:
            result = str(integ)+" "+str(float_part)+"/"+str(fraction)
        elif float_part != 0:
            result = str(float_part)+"/"+str(fraction)
        else:
            result = str(integ)
        return result
    
    if x.find('+') == -1:
        result = subtraction(x)
    else:
        result = addition(x)
    print("\nИсходная задача: ", x)
    return result
        


print(math_magic('1 5/6 + 1 4/7'))
print(math_magic('5/6 + 1 4/7'))
print(math_magic('5/6 - 4/7'))
print(math_magic('1 5/6 + 1'))
print(math_magic('1 + 1'))
print(math_magic('1/3 + 1/3'))
print(math_magic('91/8322 + 155/34'))
        
    

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

def salary_counter(hours):
    addition = hours - hour_norm
    if addition > 0:
        addition *= 2
    result = (hour_norm + addition) * salary
    return result

# Tested
def line_to_tuple(x):
    iden = ''
    name = ''
    hours = ''
    counter = 0
    for item in x:
        if item != '/':
            if counter == 0:
                iden += item
            elif counter == 1:
                name += item
            else:
                hours += item
        else:
            counter += 1
    hours = int(hours)
    return iden, name, hours

def tuple_to_line(iden, name, salary):
    result = iden + " / " + name + " / " + str(salary)
    return result

def magic(x):
    iden, name, hours = line_to_tuple(x)
    salary = salary_counter(hours)
    result = tuple_to_line(iden, name, salary)
    return result

path_workers = os.path.join('data', 'workers.txt')
# В этом файле инфа хранится в формате id / ФИО /часы
# 001 / Виктор Иванов /160
# 002 / Сергей Агафонов /200
# 003 / Виктор Крищенко / 100
path_hours = os.path.join('data', 'hours_of.txt')
hour_norm = 160
salary = 100
line_out = []

with open(path_hours, "r") as input:
    for line_in in input:
        line_out.append(magic(line_in))
with open(path_workers, "w") as output:
    for line in line_out:
        output.write(line + "\n")



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

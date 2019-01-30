# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import L05_Easy as ez

actions = ['Перейти в папку',
           'Просмотреть содержимое текущей папки',
           'Удалить папку',
           'Создать папку']
for i in range(len(actions)):
    print(str(i + 1) + '. ' + actions[i])
while True:
    print("Для выхода наберите Q")
    user_answer = input("Выберите вариант [1/2/3...]")
    if user_answer == 'Q':
        break
    elif user_answer == '2':
        print("Файлы: " + str(ez.list_direct('files')))
        print("Папки: " + str(ez.list_direct('dirs')))
    else:
        try:
            
            user_answer_2 = input("Введите название папки\n")
            if user_answer == '3':
                ez.dir_removing(name = user_answer_2)
                print("Удалено")
            elif user_answer == '4':
                ez.dir_creation(name = user_answer_2)
                print("Создано")
            elif user_answer == '1':
                target_dir = ez.os.getcwd() + '\\' + user_answer_2
                ez.os.chdir(target_dir)
                if ez.os.getcwd() == target_dir:
                    print("Перешли")
        except FileNotFoundError:
            print("Не удается найти указанную папку")
        

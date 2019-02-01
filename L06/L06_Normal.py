# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, school, classes, persons):
        self.school = school
        self.classes = classes
        self.persons = persons
    # 1. Получить список всех классов
    def get_classes(self):
        return str(list(i.return_class_name() for i in classes))[1:-1]

class Classes:
    def __init__(self, class_num, objects, students, teachers):
        self.class_num = class_num
        self.objects = objects
        self.students = students
        self.teachers = teachers
    def get_class_objects(self):
        return str(self.objects)[2:-2]
    def return_class_name(self):
        return self.class_num
    def get_students_in_class(self):
        return str([i.get_shortname() for i in self.students])[1:-1]
    def get_teachers_in_class(self):
        return str([i.get_shortname() for i in self.teachers])[1:-1]
        
        
class Person:
    def __init__(self, name, shortname):
        self.name = name
        self.shortname = shortname
    def get_shortname(self):
        return self.shortname
    def get_name(self):
        return self.name

class Student(Person):
    def __init__(self, name, shortname, parents, class_room):
        super().__init__(name, shortname)
        self.parents = parents
        self.class_room = class_room
    def get_parents_name(self):
        return 'Родители ученика: ' + ((str(list(i.get_shortname() for i in self.parents)))[1:-1])
    def get_class_room(self):
        return self.class_room

class Teacher(Person):
    def __init__(self, name, shortname, objects):
        super().__init__(name, shortname)
        self.objects = objects
    def get_object(self):
        return objects

obj = [
    'Рисование',
    'Математика',
    'Русский',
    'Литература',
    'Физкультура',
    'Геометрия',
    ]
students = [
    [
    Student('Студентов1 Студент1 Студентович1', 'Студент1 С. С.',[Person('Полное_имя_матери_1', 'Мама1 М. М.')], '1 A'),
    Student('Студентов2 Студент2 Студентович2', 'Студент2 С. С.',[Person('Полное_имя_матери_2', 'Мама2 М. М.'), Person('Полное_имя_отца_2', 'Отец2 О. О.')], '1 A'),
    Student('Студентов3 Студент3 Студентович3', 'Студент3 С. С.',[Person('Полное_имя_матери_3', 'Мама3 М. М.'), Person('Полное_имя_отца_3', 'Отец3 О. О.')], '1 A'),
    ],
    [
    Student('Студентов4 Студент4 Студентович4', 'Студент4 С. С.',[Person('Полное_имя_матери_4', 'Мама4 М. М.'), Person('Полное_имя_отца_4', 'Отец4 О. О.')], '3 A'),
    Student('Студентов5 Студент5 Студентович5', 'Студент5 С. С.',[Person('Полное_имя_матери_5', 'Мама5 М. М.'), Person('Полное_имя_отца_5', 'Отец5 О. О.')], '3 A'),
    Student('Студентов6 Студент6 Студентович6', 'Студент6 С. С.',[Person('Полное_имя_матери_6', 'Мама6 М. М.'), Person('Полное_имя_отца_6', 'Отец6 О. О.')], '3 A'),
    ],
    [
    Student('Студентов7 Студент7 Студентович7', 'Студент7 С. С.',[Person('Полное_имя_матери_7', 'Мама7 М. М.'), Person('Полное_имя_отца_7', 'Отец7 О. О.')], '5 A'),
    Student('Студентов8 Студент8 Студентович8', 'Студент8 С. С.',[Person('Полное_имя_матери_8', 'Мама8 М. М.'), Person('Полное_имя_отца_8', 'Отец8 О. О.')], '5 A'),
    Student('Студентов9 Студент9 Студентович9', 'Студент9 С. С.',[Person('Полное_имя_матери_9', 'Мама9 М. М.'), Person('Полное_имя_отца_9', 'Отец9 О. О.')], '5 A')
    ]]
teachers = [
    Teacher('Teacher1_Draw', 'Teacher T. 1.', obj[0]),
    Teacher('Teacher2_Math', 'Teacher T. 2.', obj[1]),
    Teacher('Teacher3_Rus', 'Teacher T. 3.', obj[2]),
    Teacher('Teacher4_Lit', 'Teacher T. 4.', obj[3]),
    Teacher('Teacher5_Ph', 'Teacher T. 5.', obj[4]),
    Teacher('Teacher6_Geometry', 'Teacher T. 6.', obj[5])
    ]
classes_names = ['1 А', '3 А', '4 А']
classes = [
    Classes(classes_names[0], obj[0:3], students[0], teachers[0:3]),
    Classes(classes_names[1], obj[1:5], students[1], teachers[1:5]),
    Classes(classes_names[2], obj[1:], students[2], teachers[1:])
    ]
school_name = 'ГБУ СОШ 123'
hoomans = students
my_school = School(school_name, classes, hoomans)


print('1. Список всех классов: ', my_school.get_classes())
print('2. Все ученики в классе 1 А: ', my_school.classes[0].get_students_in_class())
print('3. Список предметов ученика'), my_school.persons[0][0].get_class_room()
print('4. ФИО родителей ученика', my_school.persons[0][0].get_parents_name())
print('5. Учителя класса', my_school.classes[0].get_teachers_in_class())

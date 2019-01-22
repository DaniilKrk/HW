# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    return "{:0.{}f}".format(number, ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# Короткое решение

def lucky_ticket(ticket_number):
    def summmaa(z):
        z = str(z)
        k = 0
        for numbers in z:
            k += int(numbers)
        return k
    x = int(ticket_number / 1000)
    y = ticket_number - x * 1000
    if summmaa(x) == summmaa(y):
        return "Win"
    else:
        return "Nope"

# Длинное решение, поддерживающее разное (включая нечетное)
# кол-во знаков в билете. Включая билеты, начинающиеся с '0'
# В случае нечетного кол-ва знаков в билете, значения в середине игнорируются.
# Т.е. в билете '12321' цифра '3' будет проигнорирована.

def lucky_ticket(ticket_number):
    def summmaa(z):
        z = str(z)
        k = 0
        for numbers in z:
            k += int(numbers)
        return k
    def adding_zero(z):
        while True:
            if len(z) < ticket_len:
                z = '0'+z
            else:
                return z
                break
    ticket_number = int(ticket_number)
    ticket_len = (int(len(str(ticket_number))/2))
    x = str(int(ticket_number / 10 ** ticket_len))
    y = str(ticket_number - int(x) * 10 ** ticket_len)
    x = adding_zero(x)
    y = adding_zero(y)
    len(str(ticket_number))
    if len(str(ticket_number)) % 2 > 0:
        while True:
            if len(str(x)) > len(str(y)):
                x = str(int(int(x) / 10))
                x = adding_zero(x)
            elif len(str(x)) < len(str(y)):
                y = str(int(int(y) / 10))
                y = adding_zero(y)
            else:
                break
    x = summmaa(x)
    y = summmaa(y)
    if x == y:
        return "Win"
    else:
        return "Nope"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

print(lucky_ticket(101))
print(lucky_ticket(100))
print(lucky_ticket('0101'))

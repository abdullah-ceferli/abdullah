#  1.  Проверка квадрата числа: напишите функцию, которая проверяет, является ли число полным квадратом. (Пример: 16 → True, 18 → False)


"""
import math

enter = int(input("Enter number for square or not >>> "))

def square(n):
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n


def bool_looker(a):
    if a <= 1:
        print(f"This number {enter} isn't square")

    elif a == True:
        print(f"This number {enter} is square")

    else:
        print(f"This number {enter} isn't square")


bool_looker(square(enter))
"""


#  2.  Чет или нечет: Напишите функцию, которая принимает число и выводит, является ли оно четным или нечетным.

"""
enter = int(input("Enter number of even or odd >>> "))

def odd_even(num):
    if num % 2 == 1 or num == 1:
        print(f"This number is odd: {num}")

    elif num % 2 == 0:
        print(f"This number is even: {num}")


odd_even(enter)
"""

#  3.  Вычисление факториала: напишите функцию, которая вычисляет факториал числа с помощью цикла.

"""
enter = int(input("Enter number for get number's factorial >>> "))

def factorial(o):
    a = 1
    for i in range(1, o+1):
        a *= i

    print(f"Finnal number is {a}")


factorial(enter)
"""

#  4.  Максимум три: напишите функцию, которая принимает 3 числа и возвращает наибольшее из них.

"""
num1 = int(input("Enter first number >>> "))
num2 = int(input("Enter second number >>> "))
num3 = int(input("Enter third number >>> "))

def max_number(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print("There no ones is big")

    else:
        finnal = max(a,b,c)
        print(f"This number is biggest: {finnal}")


max_number(num1, num2, num3)
"""

#  5.  Перевернуть строку: Напишите функцию, которая переворачивает заданную строку.

"""
enter = input("Enter text for reverse it >>> ")

def reversing(a):
    process = a.split()
    if len(process) == 0:
        print("Sorry i can't reverse it")

    else:
        finnal = a[::-1]
        print(f"This reversed form of your text: {finnal}")


reversing(enter)
"""

#  6.  Сумма от 1 до 100: Используйте цикл для вычисления суммы чисел от 1 до 100.

"""
num = 0

for i in range(1,101):
    num+=i

print(f"Here is your number {num}")
"""

#  7.  Простые числа: Выведите все простые числа от 1 до 50.

"""
def looker(n):
    if n < 2:
        return False
    
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            
    return True

for num in range(1, 51):
    
    if looker(num):
        print(num, end=" ")
"""

#  8.  Таблица умножения: Напишите функцию, которая принимает число и выводит его таблицу умножения до 10.

"""
num = int(input("Enter your number >>> "))

def multiplication_table(a):
    if a == 0:
        print("Sorry i can't give multiplication table for this number")

    else:
        for i in range(1, 11):
            print(f"{num} * {i} = {num * i}")


multiplication_table(num)
"""

#  9.  Чётные числа в списке: вывести только чётные числа из заданного списка.

"""
num = input("Enter your list of number >>> ")

list = num.split()

for i in list:
    if int(i) % 2 == 0:
        print(i, end=" ")
"""

#  10.    Алфавитный цикл: используйте цикл для печати букв от A до Z.

"""
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end=" ")
"""

#  11.  Налог на зарплату: напишите функцию, которая рассчитывает налог. Если зарплата > 1000, налог составит 10%, в противном случае — 5%.

"""
salary = int(input("Enter your salary amount >>> "))


def tax_looker(a):
    if a > 1000:
        result = round(a * 0.10, 2)
        print(f"Tax is 10% and your salary amount is {result}")
    else:
        result = round(a * 0.5, 2)
        print(f"Tax is 5% and your salary amount is {result}")


tax_looker(salary)
"""

#  12.  Оценка за экзамен: Введите оценку и распечатайте:

#     •    90+ → “Excellent”
#     •    70–89 → “Good”
#     •    50–69 → “Average”
#     •    < 50 → “Failed”

"""
enter = int(input("Enter your score in exam >>> "))

if enter >= 90:
    print("Excellent!!! Bro you einstein")
if 70 <= enter <= 89:
    print("Good")
if 50 <= enter <= 69:
    print("Average")
if enter < 50:
    print("Failed!! You need run because your dad not liked your exam score")
"""

#  13.  Сезон по месяцам: введите номер месяца (1–12) и выведите, к какому сезону он относится.

"""
enter = int(input("Enter month number >>> "))

match enter:
    case 1:
        print("This month number is January")
    case 2:
        print("This month number is February")
    case 3:
        print("This month number is March")
    case 4:
        print("This month number is April")
    case 5:
        print("This month number is May")
    case 6:
        print("This month number is June")
    case 7:
        print("This month number is July")
    case 8:
        print("This month number is August")
    case 9:
        print("This month number is September")
    case 10:
        print("This month number is October")
    case 11:
        print("This month number is November")
    case 12:
        print("This month number is December")
    case _:
        print("Sorry we can't find that number in month numbers")
"""

#  14.  День недели: введите число (1–7) и выведите день (1 → Понедельник, 7 → Воскресенье).

"""
enter = int(input("Enter week number >>> "))

match enter:
    case 1:
        print("This week number is Monday")
    case 2:
        print("This week number is Tuesday")
    case 3:
        print("This week number is Wednesday")
    case 4:
        print("This week number is Thursday")
    case 5:
        print("This week number is Friday")
    case 6:
        print("This week number is Saturday")
    case 7:
        print("This week number is Sunday")
    case _:
        print("Sorry we can't find that number in week numbers")
"""

#  15.  Минимум два: напишите функцию, которая возвращает меньшее из двух чисел.

"""
num1 = int(input("Enter first number >>> "))
num2 = int(input("Enter second number >>> "))

def max_number(a, b):
    if a == b and b == a:
        print("There here no ones is small")

    else:
        finnal = min(a,b)
        print(f"This number is smallest: {finnal}")


max_number(num1, num2)
"""

#  16.  Последовательность Фибоначчи: напишите функцию, которая выводит первые n чисел Фибоначчи.

"""
def fibonacci_numbers():
    a, b = 0, 1
    n = 10
    for i in range(n):
        a, b = b, a + b
        print(a, end=" ")


fibonacci_numbers()
"""

#  17.  Строка палиндрома: напишите функцию, которая проверяет, является ли строка палиндромом.

"""
enter = input("Enter text for palindrome looker >>> ")

def palindrome_looker(a):
    list = a.split()
    count = 0
    for i in range(len(list)):
        if list[i][::-1] == list[i]:
            count += 1
            if count > 1:
                print(f"Palindrome: {list[i]}", end=", ")

    if count == 0:
        print("Here no ones is palindrome")            
            


palindrome_looker(enter)
"""

#  18.  Сумма цифр: Напишите функцию, которая возвращает сумму цифр числа (Пример: 123 → 6).

"""
enter = int(input("Enter number like 123 -> 6 >>> "))

def process(a):
    finnal = 0
    for i in str(a):
        finnal += int(i)

    print(f"Finnal number is {finnal}")


process(enter)
"""

#  19.  Найти максимум: введите несколько чисел и верните наибольшее из них.

"""
enter = input("Enter numbers for biggest one >>> ")

def process(a):
    b = a.replace(" ", "")
    list = []

    for i in range(len(b)):
        list.append(b[i])
    
    if len(list) == 0:
        print("You even not writed any thing")
    else:
        print(f"This number is biggest one: {max(list)}")


process(enter)
"""

#  20.  Перевернуть список: Напишите функцию, которая переворачивает список.

"""
enter = input("Enter numbers >>> ")

def referse_list(a):
    b = a.replace(" ", "")
    print(list(b)[::-1])


referse_list(enter)
"""
# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
def m_power(a, b):
    if b == 1:
        return 1
    return a * m_power(a, b - 1)
print(f"A = 3, B = 5 -=> {m_power(3, 5)}")
print(f"A = 2, B = 3 -=> {m_power(2, 3)}")


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
def sum(a, b):
    if a == 0:
        return b
    return sum(a - 1, b + 1)
a = 3
b = 4
print(f"{a} {b} ==> {sum(a, b)}")
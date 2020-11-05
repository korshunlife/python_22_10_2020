""" Реализовать функцию my_func(), которая принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов.
"""

def my_func(x, y, z):
    i = [x, y, z]
    my_min = min(i)
    i.remove(my_min)
    return sum(i)


a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

print(my_func(a,  b, c))
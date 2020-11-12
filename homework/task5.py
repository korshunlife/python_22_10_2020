"""
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

with open('numbers.txt', 'w', encoding='utf-8') as f:
    count = 0
    list1 = 0
    while count != 10:
        a = random.randint(1, 200)
        list1 += a
        f.write(f"{a} ")
        count += 1
    print(list1)

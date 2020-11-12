"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
# подсчет количества строк
# количества слов в каждой строке

count = 0
with open("My_text.txt", "r") as file:
    for line in file:
        count += 1
        print(f"{count}  строке {len(line.split())} слов")


# Втторой вариант посчёт строк
with open("My_text.txt", "r") as file:
    print(len(file.readlines()))




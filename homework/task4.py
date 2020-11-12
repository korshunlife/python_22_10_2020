"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}
new_strings = ''

with open("list_task4_1.txt", 'r', encoding='utf-8') as text:
    for line in text:
        word = line.split()[0]
        new_strings += line.replace(word, rus_dict[word.lower()].title())

with open('rus_task4_1.txt', 'w', encoding='utf-8') as new_text:
    new_text.write(new_strings)
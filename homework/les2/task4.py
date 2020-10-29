list_4 = input("Введите слова: ").split()
i = 1

for word in list_4:
    print(f"{i} - {word[:10]}")
    i += 1
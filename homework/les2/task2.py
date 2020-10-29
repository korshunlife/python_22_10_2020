list1 = list(input("Введите элементы для списка: "))
index = 0

for i in range(int(len(list1)/2)):
    list1[index], list1[index + 1] = list1[index + 1], list1[index]
    index += 2

print(list1)

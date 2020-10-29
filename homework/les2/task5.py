my_list = [7, 5, 3, 3, 2]
print(my_list)
value = int(input("Введите новый элемент рейтинга: "))

for idx, i in enumerate(my_list):
    if i < value:
        my_list.insert(idx, value)
        break
    if idx == len(my_list) - 1:
        my_list.append(value)
        break
print(f"NEW Рейтинг: {my_list}")

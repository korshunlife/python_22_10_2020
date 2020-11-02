product_template =  {
    "Названия" : ('Имя товара', str),
    "Цена" : ("Стоимость товара", int),
    'Количество' : ("Количество товара", int),
    "Еда" : ("Единицы измерения  (шт, кг, и т.д.)", str)
}

next_true = True

auto_inc = 1
product_list = []

while next_true:
    product = {}
    for key, value in product_template.items():
        while True:
            user_value = input(f"{value[0]}\n")
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f"{e}\nНе верное значения данных")
                continue
            product[key] = user_value
            break
    product_list.append((auto_inc, product))
    auto_inc += 1

    while True:
        next_add = input("Добавить ещё продукт? да/нет\n")
        if next_add.lower() in ('да', 'нет'):
            next_true = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввоод, повторите')

print(product_list)

product_snalitics = {}

for key in  product_template:
    result  = []
    for itm in product_list:
        result.append(itm[1][key])
    product_snalitics[key] = result


#product_snalitics[key]  = [itm[1][key] for itm in product_list]

print(product_snalitics)
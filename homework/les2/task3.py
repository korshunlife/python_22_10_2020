month =  int(input("Введите число месяца: "))

list_month  = ("зима", "весна", "лето", "осень")

if month == 1 or month == 2 or month == 12:
    print(list_month[0])
elif month == 3 or month == 4 or month == 5:
    print(list_month[1])
elif month == 6 or month == 7 or month == 8:
    print(list_month[2])
elif month == 9 or month == 10 or month == 11:
    print(list_month[3])
else:
    print("Такого месяца не существует")


# Второй вариант решения задания через dict
seasons = {'зима': (1, 2, 12),
          'весна': (3, 4, 5),
          'лето': (6, 7, 8),
          'осень': (9, 10, 11)}

month = int(input('Choose a month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
    else:
        print("Такого месяца не существует")
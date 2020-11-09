from sys import argv

try:
    _, production, rate_hours, bonus = argv
    production = int(production)
    rate_hours = float(rate_hours)
    bonus = float(bonus)
    result = (production * rate_hours) + bonus
    print(f'Заработная плата сотрудника: {result}')

except ValueError:
    print('Неверные параметры! Нужно:\n'
          ' 1 - параметр int, выработка в часах\n'
          ' 2 - параметр (float and int), ставка в час\n'
          ' 3 - параметр (float and int) премия')
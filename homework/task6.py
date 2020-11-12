import os
# Сам не успевал в срок здать  домашнее задания, не хватило часкиа два .
# Поэтому  взял ваше  решения и разобрал его самостоятельно.
# Не  вилите казнить, прошу помиловать
db = os.path.join(os.path.dirname(__file__), 'task6')
db_dict = {}
with open(db, 'r') as file:
    for line in file:
        tmp = line.split(' ')
        name = tmp[0].split(':')[0]
        db_dict[name] = sum(int(itm.split('(')[0]) for itm in tmp[1:] if itm.split('(')[0].isdigit())


print(db_dict)
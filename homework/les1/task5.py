proceeds = int(input("Введите значения выручки: "))
costs = int(input("Введите издержки фирмы: "))

if proceeds > costs:
    print("прибыль — выручка больше издержек")
elif proceeds < costs:
    print("убыток — издержки больше выручки")
else:
    print("не хорошо не плохо")

print("Рентабельность: " + str(proceeds/costs))

collaborator = int(input("Введите численность сотруников: "))
print("Каждый сотруник получит: " + str((proceeds-costs)/collaborator))
a = int(input("Введите результат первого дня в км: "))
b = int(input("Введите результат для достижения в км: "))
i = 1  #начальный день


while a < b:
    print(f"{i}-й день: {round(a, 2)}")
    a += a * 0.1
    i += 1
    if a >= b:
        print(f"Ответ: на {i}-й день спортсмен достиг результата — не менее {b} км. результат: {round(a, 2)}")
        break

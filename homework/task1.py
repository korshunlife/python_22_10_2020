def MyFunc():
    try:
        a = float(input("Введите первое значения: "))
        b = float(input("Введите второе значения: "))
        c = a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No str'
    return c

print(MyFunc())
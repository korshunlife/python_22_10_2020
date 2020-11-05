"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def MyFunc(name, surname, year_birth, city, email, number_phone):
    print(f"name: {name}, surname: {surname}, year_birth: {year_birth}, city: {city}, email: {email}, number_phone: {number_phone}" )


MyFunc(name="Джэймс", surname='Бонд', year_birth="32",city="СПб", email="gmail", number_phone="007")

"""Эксперементировал внизу
user = {}

def MyFunc():
    for  key, value in template.items():
        user[key] = input(value)
    return user


def MyFunc2(name, surname, year_birth, city, email, number_phone):
    return ([name, surname, year_birth, city, email, number_phone])


template = {
    "name": "Ваше имя\n>>>",
    "surname": "Ваше фамилия\n>>>",
    "year_birth": "Ваш год рождения\n>>>",
    "city": "Ваш город\n>>>",
    "email": "ваш email\n>>>",
    "number_phone": "Ваш телефон\n>>>"
}

a = MyFunc()
print(a)
"""


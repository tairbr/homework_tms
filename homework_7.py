def inch(n):  # 1 дюйм = 2.54 сантиметр
    resault_cm = n * 2.54
    return resault_cm


def centimeter(n):  # 1 сантиметр = 0.3937007874016 дюйм
    resault_inch = n * 0.3937007874016
    return resault_inch


def mile(n):  # 1 миля = 1.609344 километр
    resault_km = n * 1.609344
    return resault_km


def km(n):  # 1 километр = 0.6213711922373 миля
    resault_mile = n * 0.6213711922373
    return resault_mile


def lb(n):  # 1 фунт = 0.45359237 килограмм
    resault_kg = n * 0.45359237
    return resault_kg


def kg(n):  # 1 килограмм = 2.44192843875 Фунт
    resault_lb = n * 2.44192843875
    return resault_lb


def ounce(n):  # 1 унция = 28.349523125 грамм
    resault_gram = n * 28.349523125
    return resault_gram


def gram(n):  # 1 грамм = 0.03527396194958 унция
    resault_ounce = n * 0.03527396194958
    return resault_ounce


def gallon(n):  # 1 галлон = 3.785411784 литр
    resault_liters = n * 3.785411784
    return resault_liters


def liters_gl(n):  # 1 литр = 0.2641720523581 галлон
    resault_gallon = n * 0.2641720523581
    return resault_gallon


def pint(n):  # 1 пинта США = 0.473176473 литр
    resault_liters = n * 0.473176473
    return resault_liters


def liters_pn(n):  # 1 литр = 2.113376418865 пинта
    resault_pint = n * 2.113376418865
    return resault_pint


print('''
1.Дюймы в сантиметры
2.Сантиметры в дюймы
3.Мили в километры
4.Километры в мили
5.Фунты в килограммы
6.Килограммы в фунты
7.Унции в граммы
8.Граммы в унции
9.Галлон в литры
10.Литры в галлоны
11.Пинты в литры
12.Литры в пинты\n''')

dict_1 = {1: ('дюйм', 'сантиметров'), 2: ('сантиметр', 'дюймов'), 3: ('миле', 'километров'),
          4: ('километр', 'мили'), 5: ('фунт', 'килограммов'), 6: ('килограмме', 'фунтов'),
          7: ('унции', 'грамм'), 8: ('грамм', 'унции'), 9: ('галлон', 'литров'), 10: ('литр', 'галлонов'),
          11: ('пинта', 'литров'), 12: ('литр', 'пинт')}
dict_2 = {1: 'Дюймы в сантиметры', 2: 'Сантиметры в дюймы', 3: 'Мили в километры', 4: 'Километры в мили',
          5: 'Фунты в килограммы', 6: 'Килограммы в фунты', 7: 'Унции в граммы', 8: 'Граммы в унции',
          9: 'Галлон в литры', 10: 'Литры в галлоны', 11: 'Пинты в литры', 12: 'Литры в пинты'}

while True:
    number_func = int(input('- Выбери нужный вариант из списка для перевода или 0 для выхода.\n:'))
    if number_func == 0:
        break
    elif number_func > 12:
        print('- Выбери от 1 до 12 либо 0 для выхода\n')
    else:
        while True:
            input_user = int(input(f'Переводим {dict_2[number_func]}.\nВвeди значение.\n:'))
            if input_user == 0:
                break
            else:
                dict_func = {1: inch(input_user), 2: centimeter(input_user), 3: mile(input_user), 4: km(input_user),
                             5: lb(input_user), 6: kg(input_user), 7: ounce(input_user), 8: gram(input_user),
                             9: gallon(input_user), 10: liters_gl(input_user), 11: pint(input_user),
                             12: liters_pn(input_user)}

                print(f'В {input_user} {dict_1[number_func][0]} - {dict_func[number_func]} {dict_1[number_func][1]}.')
                print('- Для выхода выбери 0 или введи новое значение.')
                print()


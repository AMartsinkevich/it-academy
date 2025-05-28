#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №2
# Задание 1.

# Есть цена товара и скидка в процентах.
# Посчитать, сколько будет стоить товар со скидкой,
# и вывести исходную цену, размер скидки и финальную цену.

# Решение:

print('-' * 80)
print('Task 1')

price = 250
discount = 20
discount_amount = round(price * discount / 100, 2)
total_price = round(price - discount_amount, 2)

print(f'''
Cost calculation:
PRICE: {price} $
DISCOUNT: {discount_amount} $
TOTAL: {total_price} $
''')


# Задание 2.

# Известно расстояние между двумя городами в километрах
# и средняя скорость движения автомобиля. Посчитать, за сколько часов
# можно доехать из одного города в другой.
# Вывести расстояние, скорость и время в пути.

# Решение:

print('-' * 80)
print('Task 2')

distance = 50
average_speed = 100

time = round(distance / average_speed, 2)
print(f'''
Distance between towns: {distance} km
Your average speed: {average_speed} km/h
You'll reach the city in: {time} h
''')


# Задание 3.

# Есть переменная с количеством байт.
# Перевести это число в килобайты,
# мегабайты и гигабайты. Всё вывести в консоль с пояснениями.

# Решение:

print('-' * 80)
print('Task 3')

byte_amount = 2561243423

print(f'''
Given size in BYTES: {byte_amount}
KB: {round(byte_amount / 1024, 2)}
MB: {round(byte_amount / 1024 / 1024, 2)}
GB: {round(byte_amount / 1024 / 1024 / 1024, 2)}
''')


# Задание 4.

# Даны три стороны треугольника.
# Найти его периметр и площадь (по формуле Герона).
# Вывести всё в консоль.

# Решение:

print('-' * 80)
print('Task 4')

side_a = 10
side_b = 20
side_c = 15

perimeter = side_a + side_b + side_c
half_perimeter = perimeter / 2
area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** (1 / 2)

print(f'''
Perimeter of trangle with sides {side_a}, {side_b}, {side_c}: {perimeter}
Area of triangle: {round(area, 2)}
''')


# Задание 5.

# В переменной лежит количество шагов,
# пройденных за день, и длина одного шага в метрах.
# Посчитать общее расстояние в километрах. Вывести всё в консоль.

# Решение:

print('-' * 80)
print('Task 5')

steps = 25300
step_length = 0.7

print(f'''
You walk a distance in a day:
Steps: {steps}
Total distance: {round(steps * step_length / 1000, 2)} km
''')


# Задание 6.

# Известны масса тела и рост человека,
# посчитать индекс массы тела (ИМТ = масса / рост², масса в кг, рост в метрах).
# Вывести всё красиво

# Решение:

print('-' * 80)
print('Task 6')

weight = 75
height = 1.8

print(f'''
You body mass index measurement:
Weight: {weight} kg
Height: {height} m
BMI: {round(weight / height ** 2, 2)}
''')

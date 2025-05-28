#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №8
# Задание 5.

# Используя map() и reduce() посчитать площадь 
# квартиры, имея на входе характеристики комнат квартиры. 
# Пример входных данных:
# rooms = [
# {"name": ”Kitchen", "length": 6, "width": 4},
# {"name": ”Room 1", "length": 5.5, "width": 4.5},
# {"name": ”Room 2", "length": 5, "width": 4},
# {"name": ”Room 3", "length": 7, "width": 6.3},
# ]


# WARNING:

# - Обязательно организовываем ДЗ в форме меню
# - Обязательно делаем проверки вводимых данных и даём юзеру перепопытки ввода
# - Обязательно каждая задача в виде отдельной функции
# - Обязательно соблюдаем структуру файла: сначала все импорты, потом все функции, потом основной код
# - Обязательно следим за пробелами и отступами, пользуемся Ctrl Alt L по необходимости
# - Желательно задаём аннотации типов аргументов и возвращаемых значений для функции
# - Желательно оставляем документацию к функции
# - Желательно сдаём домашку не за пару часов до следующего занятия

# Решение:

from functools import reduce
from operator import mul, add


def get_user_int_value(message: str = 'Enter integer grater than zero: ') -> int:
    '''Return integer value provided with user input'''

    value = None
    while not value:
        value = input(message)

        if value.isdecimal():
            return int(value) 
        else:
            print('Wrong input!')

def print_flat_dimensions(rooms: list[dict]) -> float:
    '''Print out flat dimensions and return list of romm's squares'''

    squares = []
    for room in rooms:
        length = room["length"]
        width = room["width"]
        square = reduce(mul, list(room.values())[1:])
        print(f'Room: {room["name"]} with dimensions {length} x {width} = {square}')
        squares.append(square)
    
    return squares

def calculate_sum(values: list[float]) -> float:
    '''Return total sum (rounded)'''

    total = round(reduce(add, values), 2)
    
    return total


print('-' * 80)
print('Task 5')


rooms = [
    {"name": 'Kitchen', 'length': 6, 'width': 4},
    {"name": 'Room 1', 'length': 5.5, 'width': 4.5},
    {"name": 'Room 2', 'length': 5, 'width': 4},
    {"name": 'Room 3', 'length': 7, 'width': 6.3},
]

print('Let me introduce our flat -)')
squares = print_flat_dimensions(rooms)
print(f'Calculating total flat square: {calculate_sum(squares)}')

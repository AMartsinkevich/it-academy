#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №8
# Задание 2.

# Дан список чисел. С помощью filter() получить список 
# тех элементов из исходного списка, значение которых 
# больше 0.


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

from random import randint


def generate_int_list(length: int = 20) -> list[int]:
    '''Return list of random integers'''

    return [randint(-50, 50) for _ in range(length)]

def filter_positive(values: list[int]) -> list[int]:
    '''Return list of strictly positive integers from input sequence'''

    return list(filter(lambda x: x > 0, values))

def get_user_int_value(message: str = 'Enter integer grater than zero: ') -> int:
    '''Return integer value provided with user input'''

    value = None
    while not value:
        value = input(message)

        if value.isdecimal():
            return int(value) 
        else:
            print('Wrong input!')


print('-' * 80)
print('Task 2')


length = get_user_int_value('Enter length of ineger list to be genetated: ')
values = generate_int_list(length)
print('Generated list of integers:')
print(values)

print('Filtered list of integers with strictly positive values:')
print(filter_positive(values))

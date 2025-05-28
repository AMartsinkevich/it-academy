#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №8
# Задание 1.

# Дан список чисел. С помощью map() получить список, 
# где каждое число из исходного списка переведено в строку. 
# Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]


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

    return [randint(0, 100) for _ in range(length)]

def generate_str_list_from_list(values: list) -> list[str]:
    '''Return list of strings from input sequence values'''

    return list(map(lambda x: str(x), values))

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
print('Task 1')


length = get_user_int_value('Enter length of ineger list to be genetated: ')
values = generate_int_list(length)
print('Generated list of integers:')
print(values)

print('Generated list of strings from list of integers:')
print(generate_str_list_from_list(values))

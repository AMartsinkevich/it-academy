#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 1.

# Дан список чисел, отсортированных по возрастанию. 
# На вход принимается значение, равное одному из элементов 
# списка. Реализовать функцию, выполняющую рекурсивный
# алгоритм бинарного поиска, на выходе программа должна 
# вывести позицию искомого элемента в исходном списке. 

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


def generate_sorted_list_of_numbers() -> list[int]:
    '''Generate sorted list of integers'''
    return sorted([randint(0, 100) for _ in range(20)])

def recursive_binary_search(value: int, values: list[int], left: int, right: int) -> int:
    '''Recursive binary search of existing integer elemet in list of integers'''
    center = (left + right) // 2
    if values[center] == value:
        return center + 1
    if values[center] < value:
        left = center + 1
    else:
        right = center - 1
    return recursive_binary_search(value, values, left, right)


print('-' * 80)
print('Task 1')

values = generate_sorted_list_of_numbers()
print(values)

value = None
while value not in values:
    value = input('Choose any existing value from the list above: ')
    if value.isdecimal():
        value = int(value) 
    else:
        print('Wrong input!')

print('Finding a value using recursive binary search...')
index = recursive_binary_search(value, values, 0, len(values) - 1)
print(f'Found at {index} position')

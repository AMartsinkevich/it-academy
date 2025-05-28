#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 7.

# Реализовать функцию, которая создаёт матрицу 
# размером M строк на N столбцов и заполняет её рандомными
# числами.

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


def create_matrix(rows: int, cols: int) -> None:
    '''Print matrix with M rows and N columns dimension'''

    matrix = []
    for row in range(rows):
        row = []
        for col in range(cols):
            row.append(randint(0, 10))
        matrix.append(row)

    print(matrix)

print('-' * 80)
print('Task 7')


value = None
while not value:
    value = input('Enter integer > 0 for matrix rows: ')
    if value.isdecimal():
        value = int(value)
    else:
        value = None
        print('Wrong input!')

rows = value

value = None
while not value:
    value = input('Enter integer > 0 for matrix columns: ')
    if value.isdecimal():
        value = int(value)
    else:
        value = None
        print('Wrong input!')

cols = value

print("Let's build a matrix MxN")
create_matrix(rows, cols)

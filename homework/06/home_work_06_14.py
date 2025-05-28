#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 14.

# Реализовать функцию, которая находит сумму 
# элементов на главной диагонали и сумму элементов на 
# побочной диагонали (матрица M x N). 

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


def create_matrix(rows: int, cols: int) -> list[list[int]]:
    '''Return matrix with M rows and N columns dimension filled with 0's and 1's'''

    matrix = []
    for row in range(rows):
        row = []
        for col in range(cols):
            row.append(randint(0, 1))
        matrix.append(row)

    return matrix

def add_column_matrix(matrix: list[list[int]]) -> list[list[int]]:
    '''Add column so row sums are even'''

    summ_row = [0 for _ in matrix]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            summ_row[i] += matrix[i][j]

    for i, row in enumerate(matrix):
        row.append(0 if summ_row[i] % 2 == 0 else 1)

    return matrix


print('-' * 80)
print('Task 14')


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

matrix = create_matrix(rows, cols)
print("Let's build a matrix MxN")
print(matrix)

matrix = add_column_matrix(matrix)

print('New matrix with added column so each row have even sum')
print(matrix)

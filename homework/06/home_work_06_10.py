#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 10.

# Реализовать функцию, которая находит сумму 
# элементов матрицы (матрица M x N). Определить, какую долю 
# в общей сумме (процент) составляет сумма элементов 
# каждого столбца.

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
    '''Return matrix with M rows and N columns dimension'''

    matrix = []
    for row in range(rows):
        row = []
        for col in range(cols):
            row.append(randint(0, 10))
        matrix.append(row)

    return matrix

def mul_matrix(matrix: list[list[int]], col_ref: int = 0) -> list[list[int]]:
    '''Multiply columns with values of first column'''

    mul_col = [0 for _ in matrix]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if j == col_ref:
                mul_col[i] += col

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            matrix[i][j] *= mul_col[i]

    return matrix


print('-' * 80)
print('Task 10')


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

matrix = mul_matrix(matrix)

print('New matrix with elements, multiplyed with first column elements')
print(matrix)

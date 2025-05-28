#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 9.

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

def sum_matrix(matrix: list[list[int]]) -> list[int]:
    '''Find summ of elements in matrix'''

    summ_cols = [0 for _ in matrix[0]]
    summ_total = 0
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            summ_total += col
            summ_cols[j] += col

    summ_cols = [round(item * 100 / summ_total, 2) for item in summ_cols]
    return summ_total, summ_cols


print('-' * 80)
print('Task 9')


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

summ_total, summ_cols = sum_matrix(matrix)
print(f'Total summ of elements is {summ_total}. Each colums makes up {"%, ".join(str(i) for i in summ_cols)}% of total summ respectively.')

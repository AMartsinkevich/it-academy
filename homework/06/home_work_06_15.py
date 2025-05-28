#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 15.

# Зал - 5рядов по8ĸресел. Переменная hall хранит нули (ĸресло свободно) и единицы
# (занято).
# hall = [
# [0,0,1,0,0,0,1,0],
# [1,1,1,1,0,0,0,0],
# ...
# ]
# Посчитать, сĸольĸо всего свободных ĸресел.
# Найти номер ряда смаĸсимальным числом свободных мест.
# Имея число k , вернуть ĸоординаты (ряд, место) первого подряд идущего блоĸа из k
# свободных ĸресел. Если его нет - None .

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

def summ_empty_matrix(matrix: list[list[int]]) -> int:
    '''Sum of empty elements'''

    summ = 0
    summ_row = [0 for _ in matrix]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] == 0:
                summ += 1
                summ_row[i] += 1
    
    empty_row_count = summ_row[0]
    empty_row_index = 0

    for i, row in enumerate(summ_row):
        if row > empty_row_count:
            empty_row_count = row
            empty_row_index = i

    return summ, empty_row_index + 1

def free_space_matrix(matrix: list[list[int]], space: int = 3) -> int:
    '''Find start of empty space of 3 seats'''

    free_space_index_sum = 0
    free_space_index_row = 0
    free_space_index_seat = -1

    for i, row in enumerate(matrix):
        free_space_index_row = i
        for j, col in enumerate(row):
            if matrix[i][j] == 0:
                if free_space_index_sum == 0:
                    free_space_index_sum += 1
                    free_space_index_seat = j
                else:
                    free_space_index_sum += 1
            else:
                free_space_index_sum = 0
                free_space_index_seat = -1
            if free_space_index_sum == space:
                return free_space_index_row + 1, free_space_index_seat + 1

    return -1, -1


print('-' * 80)
print('Task 15')


hall = create_matrix(rows=5, cols=8)
print('Hall of 5 rows and 8 seats in each')
print(hall)

summ, empty_row_index = summ_empty_matrix(hall)
print(f'Total {summ} empty seats in hall')
print(f'The most empty row is {empty_row_index}')
free_space_index_row, free_space_index_seat = free_space_matrix(hall)
if free_space_index_seat == -1:
    print('No empty space of 3 (by default) seats in row')
else:
    print(f'Found empty space of 3 (by default) seats in {free_space_index_row} row, starting from {free_space_index_seat} seat')

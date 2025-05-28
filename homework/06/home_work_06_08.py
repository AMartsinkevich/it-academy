#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 8.

# Реализовать функцию, которая находит минимальный и 
# максимальный элементы в матрице (матрица M x N). Вывести 
# в консоль индексы найденных элементов.

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

def min_max_matrix(matrix: list[list[int]]) -> int:
    '''Find minimum and maximum element in matrix'''

    min = max = matrix[0][0]
    i_min = j_min = i_max = j_max = 0
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] < min:
                min = matrix[i][j]
                i_min = i
                j_min = j
            if matrix[i][j] > max:
                max = matrix[i][j]
                i_max = i
                j_max = j
    
    return min, i_min, j_min, max, i_max, j_max


print('-' * 80)
print('Task 8')


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

min_element, min_row, min_col, max_element, max_row, max_col = min_max_matrix(matrix)
print(f'Min elemrnt is {min_element} at position [{min_row}][{min_col}], Max element is {max_element} at position [{max_row}][{max_col}]')

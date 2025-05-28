#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 17.

# «Магичесĸий ĸвадрат»
# Пользователь вводит ĸвадрат 3×3 целых чисел.
# Проверить, является ли он магичесĸим: суммы всех строĸ, столбцов идвух диагоналей
# равны.
# Если нет, вывести, ĸаĸие именно строĸи/столбцы не совпали смагичесĸой суммой.
# Сгенерировать первый известный магичесĸий ĸвадрат 3×3 (способ «1-5-9»)


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

def is_magic_matrix(matrix: list[list[int]]) -> bool:
    '''Check if square is magic'''

    magic_sum = 0
    current_sum = 0

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i == j:
                magic_sum += matrix[i][j]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if j == len(matrix) - 1 - i:
                current_sum += matrix[i][j]

    if magic_sum != current_sum:
        return False
    else:
        current_sum = 0

    for j, col in enumerate(matrix[0]):
        current_sum += col

    if magic_sum != current_sum:
        return False
    else:
        current_sum = 0

    for j, col in enumerate(matrix[1]):
        current_sum += col

    if magic_sum != current_sum:
        return False
    else:
        current_sum = 0

    for j, col in enumerate(matrix[2]):
        current_sum += col

    if magic_sum != current_sum:
        return False
    else:
        current_sum = 0

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if j == 0:
                current_sum += matrix[i][j]

    if magic_sum != current_sum:
        return False
    else:
        current_sum = 0

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if j == 1:
                current_sum += matrix[i][j]

    if magic_sum != current_sum:
        return False
    else:
        current_sum = 0

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if j == 2:
                current_sum += matrix[i][j]

    if magic_sum != current_sum:
        return False
    else:
        current_sum = 0

    return True

def magic_matrix(rows: int, cols: int) -> list[list[int]]:
    '''Generate magic matrix'''

    matrix = []
    row = [8,  1,  6]
    matrix.append(row)
    row = [3,  5,  7]
    matrix.append(row)
    row = [4,  9,  2]
    matrix.append(row)

    return matrix

print('-' * 80)
print('Task 17')


magic_square = create_matrix(rows=3, cols=3)
print('Generate matrix (insread of user input)')
print(magic_square)

print(f'Is it really magic?: {is_magic_matrix(magic_square)}')

print('Generate really magic one')
magic = magic_matrix(3, 3)
print(magic)
print(f'Is it really magic?: {is_magic_matrix(magic)}')

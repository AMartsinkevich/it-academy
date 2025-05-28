#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 16.

# Одноцветное изображение хранится в виде 0/1 , 1 - чёрный пиĸсель.
# star = [
# [0,0,1,0,0],
# [0,1,1,1,0],
# [1,1,1,1,1],
# [0,1,1,1,0],
# [0,0,1,0,0],
# ]
# Сделать «негатив» ĸартинĸи (0↔1).
# Повернуть изображение на90° почасовой стрелĸе.
# Отразить изображение погоризонтали (зерĸально).


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

def negative_matrix(matrix: list[list[int]]) -> list[list[int]]:
    '''Invert 0's and 1's'''

    rows = 5
    cols = 5
    negative_matrix = []
    for row in range(rows):
        row = []
        for col in range(cols):
            row.append(0)
        negative_matrix.append(row)

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            negative_matrix[i][j] = 0 if matrix[i][j] == 1 else 1
    
    return negative_matrix

def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    '''Rotete to 90 degrees clockwise'''

    rows = 5
    cols = 5
    rotated_matrix = []
    for row in range(rows):
        row = []
        for col in range(cols):
            row.append(0)
        rotated_matrix.append(row)
    
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            rotated_matrix[j][cols - 1 - i] = matrix[i][j]
        
    return rotated_matrix

def flip_matrix(matrix: list[list[int]]) -> list[list[int]]:
    '''Flip matrix horizontally'''

    rows = 5
    cols = 5
    flipped_matrix = []
    for row in range(rows):
        row = []
        for col in range(cols):
            row.append(0)
        flipped_matrix.append(row)
    
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            flipped_matrix[rows - 1 - i][j] = matrix[i][j]
    
    return flipped_matrix


print('-' * 80)
print('Task 16')


star = create_matrix(rows=5, cols=5)
print('Generate Picture: Black and white picture star')
print(star)

negative = negative_matrix(star)
print('Transform Star: Inverted picture with swapped 0 and 1')
print(negative)

rotate = rotate_matrix(star)
print('Transform Star: Rotated 90 degrees clockwise picture')
print(rotate)

flip = flip_matrix(star)
print('Transform Star: Flip picture horizontally')
print(flip)

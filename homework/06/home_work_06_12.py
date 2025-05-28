#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 12.

# Программа получает на вход число H. Реализовать 
# функцию, которая определяет, какие столбцы имеют хотя бы 
# одно такое же число, а какие не имеют (матрица M x N). 

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

def search_matrix(matrix: list[list[int]], search_number: int) -> list[int]:
    '''Search which columns has given number'''

    search_row = [0 for _ in matrix[0]]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] == search_number:
                search_row[j] += 1

    return search_row


print('-' * 80)
print('Task 12')


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
value = None

while not value:
    value = input('Enter integer > 0 for searching it withing matrix columns: ')
    if value.isdecimal():
        value = int(value)
    else:
        value = None
        print('Wrong input!')

search_value = value

search_row = search_matrix(matrix, search_value)

print(f'There are numbers of found {search_value} values in each column respectively: {", ".join(str(i) for i in search_row)}')

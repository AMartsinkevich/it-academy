#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 13.

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
    '''Return matrix with M rows and N columns dimension'''

    matrix = []
    for row in range(rows):
        row = []
        for col in range(cols):
            row.append(randint(0, 10))
        matrix.append(row)

    return matrix

def summ_matrix(matrix: list[list[int]]) -> int:
    '''Return summ of main and secondary diagonal'''

    summ_main = 0
    summ_secondary = 0

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i == j:
                summ_main += matrix[i][j]
            if i + j == len(row) - 1:
                summ_secondary += matrix[i][j]

    return summ_main, summ_secondary


print('-' * 80)
print('Task 13')


value = None
while not value:
    value = input('Enter integer > 0 for matrix rows/columns: ')
    if value.isdecimal():
        value = int(value)
    else:
        value = None
        print('Wrong input!')

rows = value


matrix = create_matrix(rows, rows)
print("Let's build a matrix MxN")
print(matrix)

summ_main, summ_secondary = summ_matrix(matrix)

print(f'Total sums of main and secondary diagonals respectively: {summ_main}, {summ_secondary}')

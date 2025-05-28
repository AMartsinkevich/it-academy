#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 12.

# Дан список чисел. Реализовать программу, которая 
# посчитает сумму всех чисел в списке, а также найдет 
# минимальный и максимальный элементы. 

# Решение:

from random import randint

print('-' * 80)
print('Task 12')

values = [randint(-1000, 1000) for _ in range(100)]
summ = 0
min_value = values[0]
max_value = values[0]
for value in values:
    summ += value
    if value < min_value:
        min_value = value 
    if value > max_value:
        max_value = value 
print(f'''Summ of values: {summ},
MIN value: {min_value},
MAX value: {max_value}''')

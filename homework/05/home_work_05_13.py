#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 13.

# Дан список чисел. Реализовать программу, которая 
# проверит, все ли числа в списке уникальны (встречаются 
# только один раз). Программа должна вывести результат 
# проверки, и, если не все элементы уникальны, вывести 
# дублирующиеся элементы и количество их повторений в 
# списке. 

# Решение:

from random import randint

print('-' * 80)
print('Task 13')

print('Searching for duplicated elements in list of values in range 0-99')
values = [randint(0, 99) for _ in range(100)]
statistics = [0 for _ in range(100)]

for value in values:
    statistics[value] += 1

print(f'{values = }')
print(f'{statistics = }')

statistics_set_empty = set(statistics) - {0}
statistics_set_unique = statistics_set_empty - {1}

if not statistics_set_empty:
    print('No values at all!')
elif not statistics_set_unique:
    print('All values are unique!!')
else:
    for index, value in enumerate(statistics):
        if value > 1:
            print(f'{index} meets {value} times')

# -------------------

statistics_set = {}
for value in values:
    if statistics_set.get(value):
        statistics_set[value] += 1
    else:
        statistics_set[value] = 1

print(statistics_set)

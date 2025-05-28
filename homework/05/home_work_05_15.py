#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 15.

# Реализовать алгоритм бинарного поиска по 
# сдвинутому списку отсортированных чисел (например, дан 
# список [5, 6, 7, 1, 2, 3, 4])

# Решение:

print('-' * 80)
print('Task 15')

search_values = [0, 5, 12, 20, 21, 27, 99, 7]
values = [21, 23, 24, 25, 26, 27, 0, 1, 2, 3, 4, 5, 6, 9, 11, 12, 14, 15, 19, 20]


print('Searching pivot')
left, right = 0, len(values) - 1
while left < right:
    center = (left + right) // 2
    if values[center] > values[right]:
        left = center + 1
    else:
        right = center
index = left
print(f'{index = }')

print('Searching value')
for search_value in search_values:
    if values[index] <= search_value <= values[-1]:
        left = index
        right = len(values) - 1
    else:
        left = 0
        right = index - 1

    while left <= right:
        center = (left + right) // 2
        print(left, center, right)
        if values[center] == search_value:
            print(f'Fount at position {center + 1}')
            break            
        elif values[center] < search_value:
            left = center + 1
        else:
            right = center - 1
    else:
        print('Not found!')

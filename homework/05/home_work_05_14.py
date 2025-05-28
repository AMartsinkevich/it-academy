#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 14.

# Дан список чисел, отсортированных по возрастанию. 
# На вход принимается значение, равное одному из элементов 
# списка. Реализовать алгоритм бинарного поиска, на выходе 
# программа должна вывести позицию искомого элемента в 
# исходном списке.

# Решение:

print('-' * 80)
print('Task 14')

search_values = [0, 5, 12, 21, 27, 99, 7]
values = [0, 1, 2, 3, 4, 5, 6, 9, 11, 12, 14, 15, 19, 20, 21, 23, 24, 25, 26, 27]

print('Searching value')
for search_value in search_values:
    left = 0
    right = len(values) - 1
    is_found = False
    while left <= right:
        center = (left + right) // 2
        print(left, center, right)
        if values[center] == search_value:
            is_found == True
            print(f'Fount at position {center + 1}')
            break
        elif values[center] < search_value:
            left = center + 1
        else:
            right = center - 1
    else:
        if not is_found:
            print('Not found!')
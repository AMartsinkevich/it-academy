#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №3
# Задание 4.

# Есть список чисел.
# - Отсортировать список и вывести его.
# - Посчитать, сколько раз в списке встречается число 1.
# - Добавить в список число 42, вывести получившийся список.
# - Развернуть список от конца к началу, вывести его.
# - Вставить в позицию №2 в списке значение 88, вывести получившийся список.
# - Удалить из списка элемент 42, вывести получившийся список.
# - Вывести элементы списка с 3-го до конца строки, выводя только каждый 3-й элемент.

# Решение:

print('-' * 80)
print('Task 4')

input_list = input('Enter your space-separated list of numbers: ')
nums = [int(_) for _ in input_list.split()]


nums.sort()
print(f'Sorted list: {nums}')
print(f'There are: {nums.count(1)} occurences of 1')
nums.append(42)
print(f'List with added 42: {nums}')
nums.reverse()
print(f'Reversed list: {nums}')
nums.insert(2, 88)
print(f'Inserting 88 at 2nd position: {nums}')
nums.remove(42)
print(f'List without 42: {nums}')
print(f'Every 3rd elements starting from 3rd {nums[3::3]}')

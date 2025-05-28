#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №3
# Задание 3.

# Дана строка. Замените в этой строке все появления буквы 'h' на букву 'H', кроме первого и последнего вхождения.
# Подсказка: использовать метод replace с параметрами.
# Например, дано: 'hhhabchghhh', должно быть 'hHHabcHgHHh'

# Решение:

print('-' * 80)
print('Task 3')

input_string = input('Enter your string: ')

left_index = input_string.find('h')
right_index = input_string.rfind('h')

prefix = input_string[:left_index + 1]
inner_string = input_string[left_index + 1 : right_index].replace('h', 'H')
suffix = input_string[right_index:]

print(f'Converted string: {prefix}{inner_string}{suffix}')

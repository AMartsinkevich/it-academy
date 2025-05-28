#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №3
# Задание 2.

# Дан список, узнать, сколько было в нём уникальных элементов,
# а сколько - неуникальных. Пользоваться простой арифметикой,
# встроенными функциями и конвертацией типов

# Решение:

print('-' * 80)
print('Task 2')

input_string = input('Enter your string: ')

char_list = list(input_string)
char_set = set(char_list)
char_count = len(char_set)

for item in char_set:
    char_list.remove(item)

non_unique_char_set = set(char_list)
non_unique_char_count = len(non_unique_char_set)
unique_char_count = char_count - non_unique_char_count

print(f'''In your string '{input_string}' there are:
{unique_char_count} unique symbols and
{non_unique_char_count} non unique symbols
''')

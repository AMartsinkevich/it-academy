#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №3
# Задание 1.

# На первой картинке условие задачи,
# на второй - что можно использовать для самопроверки.
# Если в вашу программу ввести строку "Hello",
# должен получиться соответствующий результат как в левом столбике на второй картинке

# Дана строка, в которой буква 'h' встречается как минимум два раза. Разверните
# последовательность символов, заключённую между первым и последним появлением
# буквы 'h', в противоположном порядке.

# Входные данные:
# In the hole in the ground there lived a hobbit
# qwertyhasdfghzxcvb
# asdfghhzxcvb
# ahbhchdheha
# habcdefgijklmh
# hh
# hah
# habh
# ahcvbhs


# Правильные ответы:
# In th a devil ereht dnuorg eht ni eloh ehobbit
# qwertyhgfdsahzxcvb
# asdfghhzxcvb
# ahehdhchbha
# hnmlkjigfedcbah
# hh
# hah
# hbah
# ahbvchs

# Решение:

print('-' * 80)
print('Task 1')

def revert_substring(input_string):

    first_h_index = input_string.find('h')
    last_h_index = input_string.rfind('h')

    output = list(input_string)
    output[first_h_index + 1 : last_h_index] = input_string[last_h_index - 1 : first_h_index: -1]

    return ''.join(output)

input_string = input('Input your string with at least 2 h in it: ')
print(f'''
Input string: {input_string}
Output string: {revert_substring(input_string)}
''')

input_list = [
    'In the hole in the ground there lived a hobbit',
    'qwertyhasdfghzxcvb',
    'asdfghhzxcvb',
    'ahbhchdheha',
    'habcdefgijklmnh',
    'hh',
    'hah',
    'habh',
    'ahcvbhs'
]

verify_list = [
    'In th a devil ereht dnuorg eht ni eloh ehobbit',
    'qwertyhgfdsahzxcvb',
    'asdfghhzxcvb',
    'ahehdhchbha',
    'hnmlkjigfedcbah',
    'hh',
    'hah',
    'hbah',
    'ahbvchs'
]

for index, item in enumerate(input_list):
    assert revert_substring(item) == verify_list[index], f'Input string "{item}" after conversion into "{revert_substring(item)}" is not equal to "{verify_list[index]}"'

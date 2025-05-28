#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №10
# Задание 7.

# Дан текстовый файл с несколькими строками. 
# Зашифровать шифром Цезаря, при этом шаг зависит от 
# номера строки: для первой строки шаг 1, для второй – 2 и т.д.
# Пример: 
# Входные данные:
# Hello
# Hello
# Hello
# Hello
# Выходные данные:
# Ifmmp
# Jgnnq
# Khoor
# Lipps


# Решение:


import os
import re


def cipher_text(value: str, operation: str, shift: int = 3) -> str:
    '''Encode/decode message using Cesarus algorithm'''

    cipher = ''
    en_lo = 'abcdefghijklmnopqrstuvwxyz'
    en_hi = en_lo.upper()
    ru_lo = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ru_hi = ru_lo.upper()
    en_ru_lo_hi = f'{en_hi}{en_lo}{ru_hi}{ru_lo}'
    shift = shift if operation == 'E' else (-1) * shift
    for char in value:
        if char not in en_ru_lo_hi:
            cipher += char
        else:
            index = en_ru_lo_hi.find(char)
            new_index = index + shift
            if 0 <= index <= 25:
                if new_index > 25:
                    new_index -= 26
                elif new_index < 0:
                    new_index += 26
                cipher += en_ru_lo_hi[new_index]                    
            if 26 <= index <= 51:
                if new_index > 51:
                    new_index -= 26
                elif new_index < 26:
                    new_index += 26
                cipher += en_ru_lo_hi[new_index]                    
            if 52 <= index <= 84:
                if new_index > 84:
                    new_index -= 33
                elif new_index < 52:
                    new_index += 33
                cipher += en_ru_lo_hi[new_index]                    
            if 85 <= index <= 117:
                if new_index > 117:
                    new_index -= 33
                elif new_index < 85:
                    new_index += 33
                cipher += en_ru_lo_hi[new_index]                    
    return cipher


print('-' * 80)
print('Task 7')


print('Changing directory to data')
os.chdir('data')
current_directoty = os.getcwd()
print(f'Current directory: {current_directoty}')
print('Reading file...')
with open('ceasar.txt', 'r') as file:
    data = file.readlines()
print('Encripting every line with line number key')
for index, line in enumerate(data):
    print(cipher_text(line, 'E', index + 1), end='')

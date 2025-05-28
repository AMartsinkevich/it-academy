#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №10
# Задание 6.

# В файл записано некоторое содержимое (буквы, 
# цифры, пробелы, специальные символы и т.д.). Числом 
# назовём последовательность цифр, идущих подряд. Вывести 
# сумму всех чисел, записанных в файле. 
# Пример: входные данные: 123 ааа456 1x2y3z 4 5 6
# Выходные данные: 600

# Решение:


import os
import re


print('-' * 80)
print('Task 6')


print('Changing directory to data')
os.chdir('data')
current_directoty = os.getcwd()
print(f'Current directory: {current_directoty}')
with open('calc.txt', 'r') as file:
    data = file.read()

pattern = re.compile(r'(\d+)')
print('Searching for numbers in text:')
find = pattern.findall(data)
print(find)
summ = 0
for num in find:
    summ += int(num)
print(f'Sum of numbers: {summ}')

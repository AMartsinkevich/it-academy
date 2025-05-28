#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №10
# Задание 5.

# В текстовый файл построчно записаны фамилия и имя 
# учащихся класса и оценка за контрольную. Вывести на экран 
# всех учащихся, чья оценка меньше трёх баллов.

# Решение:


import os
import re


print('-' * 80)
print('Task 5')


print('Changing directory to data')
os.chdir('data')
current_directoty = os.getcwd()
print(f'Current directory: {current_directoty}')
with open('class.txt', 'r') as file:
    students = file.readlines()

pattern = re.compile(r'([А-ЯA-Z]\S+ [А-ЯA-Z]\S+ [А-ЯA-Z]\S+) (\d)')
print('List of low reults students:')
for student in students:
    match = pattern.match(student)
    if int(match.group(2)) < 3:
        print(f'{match.group(1)}. Mark is: {match.group(2)}')

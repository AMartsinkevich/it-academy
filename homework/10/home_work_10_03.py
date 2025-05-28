#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №10
# Задание 3.

# Напишите программу, которая считывает текст из 
# файла (в файле может быть больше одной строки) и выводит 
# в новый файл самое часто встречаемое слово в каждой 
# строке и число – счётчик количества повторений этого слова 
# в строке.

# Решение:


import os


print('-' * 80)
print('Task 3')


print('Changing directory to data')
os.chdir('data')
current_directoty = os.getcwd()
print(f'Current directory: {current_directoty}')
with open('input.txt', 'r') as file:
    data = file.readlines()

word_count = {}
for line in data:
    words = line.split()
    for word in words:
        word = word.lower()
        if not word_count.get(word):
            word_count[word] = 1
        else:
            word_count[word] += 1
    word = ''
    times = 0
    for key, value in word_count.items():
        if value > times:
            times = value
            word = key
    text = f'Most common word in line: {word}, {times} occurences'
    print(text)
    with open('output.txt', 'a') as file:
        file.write(f'{text}\n')
    word_count = {}

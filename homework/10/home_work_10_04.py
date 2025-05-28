#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №10
# Задание 4.

# Напишите программу, которая получает на вход строку 
# с названием текстового файла и выводит на экран 
# содержимое этого файла, заменяя все запрещённые слова 
# звездочками. Запрещённые слова, разделённые символом 
# пробела, должны храниться в файле stop_words.txt. 
# Программа должна находить 
# запрещённые слова в любом месте файла, даже в середине 
# другого слова. Замена независима от регистра: если в списке 
# запрещённых есть слово exam, то замениться должны exam, 
# eXam, EXAm и другие вариации. 
# Пример: в stop_words.txt записаны слова: hello email 
# python the exam wor is
# Текст файла для цензуры выглядит так: Hello, World! Python 
# IS the programming language of thE future. My EMAIL is… 
# PYTHON as AwESOME!
# Тогда итоговый текст: *****, ***ld! ****** ** *** programming 
# language of *** future. My ***** **... ****** ** awesome!!!!

# Решение:


import os
import re


print('-' * 80)
print('Task 4')


print('Changing directory to data')
os.chdir('data')
current_directoty = os.getcwd()
print(f'Current directory: {current_directoty}')
with open('stop_words.txt', 'r') as file:
    data = file.readlines()

banned_words = []
for line in data:
    banned_words.extend(line.lower().split())
print(banned_words)

user_file = input('Enter file to print out: ')
if os.path.exists(user_file):
    with open(user_file, 'r') as file:
        censored_file = file.read()
else:
    print('Wrong path!')

for word in banned_words:
    censored_file = re.sub(word, '*'*len(word), censored_file, flags=re.IGNORECASE)
print('Censored version of file:')
print(censored_file)

#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №10
# Задание 9.

# ДЗ до след вторника:

# 1. Сделать из прошлой презентации 2 и 8 задачи
# 2. Залить их на гит. Мне скидываете ссылку на репозиторий. В гите поддерживать нормальную структуру ветвления: ветка master, от неё ветка develop, от неё, например, ветка feature/2-task и там вы делаете 2ю задачу, затем сливаете через merge в ветку develop. Также от develop ветка feature/8-task, там делаете 8 задачу и сливаете её в ветку develop так же. 
# 3. Бонусная задача: написать программу, которая с помощью регулярок находит в текстовом файле все емейлы и записывает их в отдельный файл emails.txt и также с номерами телефонов - находит и в файл phones.txt. 

# 4. Задать файл  .gitignore, обязательно игнорировать .venv и .idea


# Решение:


import os
import re
import json
import csv



print('-' * 80)
print('Task 9')


print('Changing directory to data')
os.chdir('data')
current_directoty = os.getcwd()
print(f'Current directory: {current_directoty}')
with open('extract_emails_and_phones.txt', 'r') as file:
    data = file.read()

pattern_email = re.compile(r'((\w+[._-])+\w+@(\w+\.)+\w+)')
pattern_phone = re.compile(r'\+\d{3}[-( ]?\d{2}[-) ]?\d{3}[- ]?\d{2}[- ]?\d{2}')

emails = pattern_email.findall(data)
phones = pattern_phone.findall(data)

print('Extracting emails in format (xxxxx@xxxx.xxx) from extract_emails_and_phones.txt file...')
with open('extracted_emales.txt', 'w') as file:
    for email in emails:
        file.write(f'{email[0]}\n')
print('Emails saved to extracted_emails.txt file')

print('Extracting phones in format (+375-XX-XXX-XX-XX) from extract_emails_and_phones.txt file...')
with open('extracted_phones.txt', 'w') as file:
    for phone in phones:
        file.write(f'{phone}\n')
print('Phones saved to extracted_phones.txt file')

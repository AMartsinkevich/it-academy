#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №10
# Задание 8.

# JSON и CSV. 
# Исходные данные: 
# https://drive.google.com/drive/folders/1KH3pJewo3QKl3mua2Xn
# JDv9xN2LxusbE?usp=sharing
# Пункты задания:
# 0. Есть данные в формате JSON – взять с диска с 
# исходными данными. 
# 1. Реализовать функцию, которая считает данные из 
# исходного JSON-файла и преобразует их в формат CSV
# 2. Реализовать функцию, которая сохранит данные в 
# CSV-файл (данные должны сохраняться независимо от их 
# количества – если добавить в исходный JSON-файл ещё 
# одного сотрудника, работа программы не должна 
# нарушаться).
# 3. Реализовать функцию, которая добавит информацию о 
# новом сотруднике в JSON-файл. Пошагово вводятся все 
# необходимые данные о сотруднике, формируются данные 
# для записи. 
# 4. Такая же функция для добавления информации о 
# новом сотруднике в CSV-файл. 
# 5. Реализовать функцию, которая выведет информацию 
# об одном сотруднике по имени. Имя для поиска вводится с 
# клавиатуры. 
# 6. Реализовать функцию фильтра по языку: с клавиатуры 
# вводится язык программирования, выводится список всех 
# сотрудников, кто владеет этим языком программирования. 
# 7. Реализовать функцию фильтра по году: ввести с 
# клавиатуры год рождения, вывести средний рост всех 
# сотрудников, у которых год рождения меньше заданного. 
# 8. Программа должна представлять собой интерактив –
# пользовательское меню с возможностью выбора 
# определённого действия (действия – функции из 
# предыдущих пунктов + выход из программы). Пока 
# пользователь не выберет выход из программы, должен 
# предлагаться выбор следующего действия.

# Решение:


import os
import re
import json
import csv



print('-' * 80)
print('Task 8')


print('Changing directory to data')
os.chdir('data')
current_directoty = os.getcwd()
print(f'Current directory: {current_directoty}')
with open('employees.json', 'r') as file:
    data = json.load(file)

field_names = list(data[0].keys())
print(field_names)

with open('csv.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

new_json_data =     {
        "name": "Aasd Dfdfd",
        "birthday": "11.09.2011",
        "height": 162,
        "weight": 62.4,
        "car": True,
        "languages": ["Python"]
    }

data.append(new_json_data)

with open('json_output.txt', 'w') as file:
    json.dump(data, file, indent=4)

with open('csv.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerow(new_json_data)

name = input('Enter name to search: ')
print('Info about persons with match in name:')
for man in data:
    if name.lower() in man['name'].lower():
        print(f'Found record: {man['name']}, {man['birthday']}')

language = input('Enter language to search: ')
print('Info about persons with match in language:')
for man in data:
    if [_ for _ in man['languages'] if language.lower() in _.lower()]:
        print(f'Found record: {man['name']}, {man['languages']}')

print('Find all persons with DOB < specified:')
year = input('Enter int year: ')
height_count = 0
height_sum = 0
if year.isdecimal():
    year = int(year)
    for man in data:
        if int(man['birthday'].split('.')[2]) < year:
            print(f'Found record: {man['name']}, {man['birthday']}')
            height_count += 1
            height_sum += man['height']
    print(f'Total {height_count} pesrons found with average height {round(height_sum / height_count, 2)}')

exit = None
while not exit:
    user_input = input('Enter 1, 2, 3, 4 for actions: search by name, search by year, search by language, exit: ')
    if user_input == '1':
        print('You are choosing searching by name')
    elif user_input == '2':
        print('You are choosing searching by year')
    elif user_input == '3':
        print('You are choosing searching by language')
    elif user_input == '4':
        print('You are choosing exit')
        exit = True

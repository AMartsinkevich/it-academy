#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №10
# Задание 1.

# Есть папка, в которой лежат файлы с разными расширениями. 
# Программа должна:
# 1. Вывести имя вашей ОС
# 2. Вывести путь до папки, в которой вы находитесь
# 3. Рассортировать файлы по расширениям, например, для 
# текстовых файлов создается папка, в неё перемещаются все 
# файлы с расширением .txt, то же самое для остальных 
# расширений
# 4. После рассортировки выводится сообщение типа «в папке с 
# текстовыми файлами перемещено 5 файлов, их суммарный 
# размер - 50 гигабайт» 
# 5. Как минимум один файл в любой из получившихся 
# поддиректорий переименовать. Сделать вывод сообщения 
# типа «Файл data.txt был переименован в some_data.txt»
# 6. Программа должна быть кроссплатформенной – никаких 
# хардкодов с именем диска и слэшами.

# Решение:


import os
import platform

print('-' * 80)
print('Task 1')


os_name = os.name
print(f'Working on {platform.platform()} OS')
print('Changing directory to data')
os.chdir('data')
current_directoty = os.getcwd()
print(f'Current directory: {current_directoty}')
print('List of files:')
files = os.listdir()
print(files)

file_groups = {}

for file in files:
    name, extension = os.path.splitext(file)
    key = '' if not extension else extension[1:]
    if file_groups.get(key):
        file_groups[key][0] += 1
        file_groups[key][1] += os.stat(file).st_size
    else:
        file_groups[key] = [1, os.stat(file).st_size]
print('Statistics:')
for name, stat in file_groups.items():
    print(f'Extension {'HIDDEN' if name == '' else name}: occured {stat[0]} times')

print('Creating folders and moving files...')
file_to_rename = ''
for name, stat in file_groups.items():
    count, size = stat
    if name == '':
        print('Skipping hidden files')
        print(f'Total {count} files, {size} bytes')
    else:
        for file in files:
            _, extension = os.path.splitext(file)
            if extension and extension[1:] == name:
                if not os.path.exists(name):
                    os.mkdir(name)
                os.rename(file, os.path.join(name, file))
                if file_to_rename == '':
                    file_to_rename = os.path.join(name, file)

        print(f'Moved {count} {name} files: {size} bytes')

if file_to_rename != '':
    print(f'Renaming file {file_to_rename} to {file_to_rename}_renamed')
    os.rename(file_to_rename, f'{file_to_rename}_renamed')

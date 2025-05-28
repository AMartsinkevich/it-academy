#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 2.

# Программа получает на вход число в десятичной 
# системе счисления. Реализовать функцию, которая 
# переводит входное число в двоичную систему счисления. 
# Допускается реализация функции как в рекурсивном 
# варианте, так и с итеративным подходом.

# WARNING:

# - Обязательно организовываем ДЗ в форме меню
# - Обязательно делаем проверки вводимых данных и даём юзеру перепопытки ввода
# - Обязательно каждая задача в виде отдельной функции
# - Обязательно соблюдаем структуру файла: сначала все импорты, потом все функции, потом основной код
# - Обязательно следим за пробелами и отступами, пользуемся Ctrl Alt L по необходимости
# - Желательно задаём аннотации типов аргументов и возвращаемых значений для функции
# - Желательно оставляем документацию к функции
# - Желательно сдаём домашку не за пару часов до следующего занятия

# Решение:

def print_decimal_to_binary(value: int) -> None:
    '''Convert decimal to binary string representation of given integer and printed it out'''
    if value // 2 != 0:
        print_decimal_to_binary(value // 2)
        print(value % 2, end='')
    else:
        print(value % 2, end='')


print('-' * 80)
print('Task 2')

value = None
while not value:
    value = input('Enter integer > 0 to convert into binary representation: ')
    if value.isdecimal():
        value = int(value) 
    else:
        value = None
        print('Wrong input!')
print(f'Converted representation of {value} in binary format is: ', end='')
print_decimal_to_binary(value)

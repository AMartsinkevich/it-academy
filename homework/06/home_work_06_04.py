#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 4.

# Программа получает на вход два числа и находит их 
# НОД (наибольший общий делитель). Пример: на вход 
# подаются числа 12 и 18, их НОД равен 6 

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

def find_greatest_common_divisor(value_one: int, value_two: int, divider: int = 2, gcd: int = 1) -> int:
    '''Find out a greatest common divisor of two given numbers'''

    if value_one < value_two:
        value_one, value_two = value_two, value_one
    
    if value_one == value_two:
        return value_one

    if value_one % value_two == 0:
        return value_two

    if divider < value_two:
        if value_one % divider == 0 and value_two % divider == 0:
            gcd = divider
        return find_greatest_common_divisor(value_one, value_two, divider+1, gcd)

    return gcd


print('-' * 80)
print('Task 4')


value = None
while not value:
    value = input('Enter integer > 0: ')
    if value.isdecimal():
        value = int(value)
    else:
        value = None
        print('Wrong input!')

value_one = value

value = None
while not value:
    value = input('Enter integer > 0: ')
    if value.isdecimal():
        value = int(value)
    else:
        value = None
        print('Wrong input!')

value_two = value

print(f"Let's find greatest common divisor of your two numbers: {find_greatest_common_divisor(value_one, value_two)}")

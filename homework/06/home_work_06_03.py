#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 3.

# Программа получает на вход число. Реализовать 
# функцию, которая определяет, является ли это число простым 
# (делится только на единицу и на само себя). 

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

def is_prime(value: int, divider: int = 2) -> bool:
    '''Check if given number is prime'''

    if value == 1:
        return False

    if value == 2:
        return True

    if divider ** 2 <= value:
        if value % divider == 0:
            return False
        return is_prime(value, divider+1)

    return True


print('-' * 80)
print('Task 3')


value = None
while not value:
    value = input('Enter integer > 0 to check if it is prime: ')
    if value.isdecimal():
        value = int(value)
    else:
        value = None
        print('Wrong input!')

print(f"Your number {'is' if is_prime(value) else 'is not'} prime")

#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №8
# Задание 3.

# Дан список строк. С помощью filter() получить список 
# тех строк из исходного списка, которые являются 
# палиндромами (читаются в обе стороны одинаково, например, 
# ’abcсba’)


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


def filter_palindrome(values: list[str]) -> list[str]:
    '''Return list of palindrome strings input sequence'''

    return list(filter(lambda x: is_palindrome(x), values))

def is_palindrome(values: str) -> bool:
    '''Return is input string a palindrome'''

    if len(values) == 1:
        return True
    
    if len(values) == 2:
        return values[0] == values[-1]
    
    return values[0] == values[-1] and is_palindrome(values[1:-1])    

def get_user_int_value(message: str = 'Enter integer grater than zero: ') -> int:
    '''Return integer value provided with user input'''

    value = None
    while not value:
        value = input(message)

        if value.isdecimal():
            return int(value) 
        else:
            print('Wrong input!')


print('-' * 80)
print('Task 3')


values = ['aa', 'a', 'abba', 'asdf1fdsa', 'sdsd', 'asddsc', 'sd ss']
print('List of input strings to filter out:')
print(values)

print('Filtered list with only palindrome strings:')
print(filter_palindrome(values))

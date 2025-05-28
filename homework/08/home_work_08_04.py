#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №8
# Задание 4.

# Сделать декоратор, который измеряет время, 
# затраченное на выполнение декорируемой функции. 


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

from time import sleep
from datetime import datetime



def time_duration(inner_function) -> float:
    '''Return time duration in seconds'''

    def wrapper(param):
        print('Emulating working process...')
        start = datetime.now()
        inner_function(param)
        end = datetime.now()
        duration = (end - start).total_seconds()
        print(f'Hard working duration: {duration}. Take a rest -)')
    return wrapper

@time_duration
def work_hard(time_to_sleep: int) -> None:
    sleep(time_to_sleep)

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
print('Task 4')


time_to_sleep = get_user_int_value('Enter time to sleep (emulating active function work): ')
work_hard(time_to_sleep)

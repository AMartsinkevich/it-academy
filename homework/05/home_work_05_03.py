#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 3.

# Проверка на простоту
# Определите, простое ли число n, перебирая возможные делители в цикле while.
# Усложнение: сделать оптимизацию к этому алгоритму через корень квадратный 

# Решение:

print('-' * 80)
print('Task 3')

input_string = input('Enter your number in range 1 - 999: ')

if input_string.isdigit() and (number := int(input_string)):
    is_prime = True
    divider = 2
    while divider ** 2 <= number and is_prime:
        if number % divider == 0:
            is_prime = False
        divider += 1
    else:
        if number == 1:
            is_prime = False
    print(f"Your number {'is' if is_prime else 'is not'} prime")
else:
    print('Wrong input!')

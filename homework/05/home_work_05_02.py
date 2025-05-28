#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 2.

# Длина цепочки Коллатца
# Для положительного числа n постройте последовательность Коллатца
# (если n чётное → n/2, иначе → 3n+1) до тех пор, пока не получите 1.
# Выведите длину цепочки.

# Решение:

print('-' * 80)
print('Task 2')

input_string = input('Enter your number in range 1 - 999: ')

if input_string.isdigit() and (number := int(input_string)):
    print(f'n: {number}')
    steps = 0
    while number != 1:
        number = int(number / 2) if number % 2 == 0 else 3 * number + 1
        steps += 1
        print(f'n: step {steps} : {number}')
    print(f'Length is {steps} step(s)')
else:
    print('Wrong input!')

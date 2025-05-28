#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №4
# Задание 1.

# Пользователь вводит число. Проверить, магическое ли оно.
# Магическими числами считаются те, у которых сумма цифр равна их произведению.
# Число может быть 1-, 2- и 3-х значным (0-9б 10-99, 100-999)

# Решение:

print('-' * 80)
print('Task 1')

input_string = input('Enter number from 0-999 range: ')
length = len(input_string)

if input_string.isdigit() and length <= 3:

    number = int(input_string)
    summ = 0
    product = 1

    for _ in range(length):
        last_digit = number % 10
        summ = summ + last_digit
        product = product * last_digit
        number = number // 10

    if summ == product:
        print('Magic number!')
    else:
        print('Ordinary number')

else:
    print('Wrong input!')

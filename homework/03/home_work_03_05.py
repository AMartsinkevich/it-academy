#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №3
# Задание 5.

# Дана строка.
# - Сначала выведите третий символ этой строки.
# - Во второй строке выведите предпоследний символ строки.
# - В третьей строке выведите первые пять символов строки.
# - В четвёртой выведите всё до последних двух символов.
# - В пятой строке выведите все символы с чётными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого)
# - В шестой строке выведите все символы с нечётными индексами, то есть начиная со второго символа строки.
# - В седьмой строке выведите все символы в обратном порядке.
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# - В девятой строке выведите длину данной строки.

# Решение:

print('-' * 80)
print('Task 5')

input_string = input('Enter your string of more than 5 symbols: ')

print(f'3rd symbol: {input_string[3]}')
print(f'Before last symbol: {input_string[-2]}')
print(f'First 5 symbols: {input_string[:5]}')
print(f'Up to 2 last symbols: {input_string[:-2]}')
print(f'Symbols with even indexes: {input_string[::2]}')
print(f'Symbols with odd indexes: {input_string[1::2]}')
print(f'String in reverse order: {input_string[::-1]}')
print(f'Every 2nd symbol in reverse order: {input_string[::-2]}')
print(f'String length: {len(input_string)}')

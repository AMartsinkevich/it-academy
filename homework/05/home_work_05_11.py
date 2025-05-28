#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 11.

# Реализовать вывод последовательности чисел 
# Фибоначчи (1 1 2 3 5 8 13 21 34 55 89 …), где каждое 
# следующее число является суммой двух предыдущих. 

# Решение:

print('-' * 80)
print('Task 11')

fibonacci_first = 1
fibonacci_second = 1
numbers_to_output = 100
print('Fibonacci Sequence. First 100 numbers')
print(f"{'#':<5}{'Sequence Number':<15}")
print(f"{'1':<5}{fibonacci_first:<15}")
print(f"{'2':<5}{fibonacci_second:<15}")
for index in range(3, numbers_to_output + 1):
    fibonacci_first, fibonacci_second = fibonacci_second, fibonacci_first + fibonacci_second
    print(f'{index:<5}{fibonacci_second:<15}')

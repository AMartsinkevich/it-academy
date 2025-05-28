#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 8.

# Продолжаем работать с формулами.
# Используя модуль math, вычислите значения по следующим 
# формулам:
# sin(x) = SUMM (-1)**n * x ** (2*n+1)/ (2*n + 1)!

# Решение:

from math import sin, sumprod, factorial, fsum

print('-' * 80)
print('Task 8')

print('Evaluating sin(x) through Maclaurin Series\n')
x = float(input('Enter numeric value x in radians: '))
reference = sin(x)
print(f'Reference: sin(x) = {reference}\n')
print(f"{'Iteration':^10} {'Maclaurin Series':^20} {'Error':^20}")

for i in range(21):
    approximation = fsum([((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1) for n in range(i+1)])
    print(f"{i:10}  {approximation:<20}{reference - approximation:20}")

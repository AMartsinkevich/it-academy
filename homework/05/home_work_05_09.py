#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 9.

# Продолжаем работать с формулами.
# Используя модуль math, вычислите значения по следующим 
# формулам:
# cos(x) = SUMM (-1)**n * x ** (2*n)/ (2*n)!

# Решение:

from math import cos, factorial, fsum

print('-' * 80)
print('Task 9')

print('Evaluating cos(x) through Maclaurin Series\n')
x = float(input('Enter numeric value x in radians: '))
reference = cos(x)
print(f'Reference: cos(x) = {reference}\n')
print(f"{'Iteration':^10} {'Maclaurin Series':^20} {'Error':^20}")

for i in range(21):
    approximation = fsum([((-1) ** n) * (x ** (2 * n)) / factorial(2 * n) for n in range(i+1)])
    print(f"{i:10}  {approximation:<20}{reference - approximation:20}")

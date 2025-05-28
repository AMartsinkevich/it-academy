#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №4
# Задание 2.

# Пользователь вводит три стороны треугольника.
# Если треугольник существует (a + b > c, a + c > b, b + c > a), проверяем:
#       Все три стороны равны? → "Равносторонний треугольник"
#       Две стороны равны? → "Равнобедренный треугольник"
#       Все стороны разные? → "Разносторонний треугольник"
# Если треугольник не существует, выводим "Такого треугольника не существует"
# (Напоминание: треугольник существует, если сумма любых двух сторон больше третьей.)

# Решение:

print('-' * 80)
print('Task 2')

input_a = input('Enter the side a of the triangle: ')
input_b = input('Enter the side b of the triangle: ')
input_c = input('Enter the side c of the triangle: ')


if input_a.isdigit() and input_b.isdigit() and input_c.isdigit():

    side_a = int(input_a)
    side_b = int(input_b)
    side_c = int(input_c)

    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:

        sides = {side_a, side_b, side_c}
        
        if len(sides) == 1:
            print('Равносторонний треугольник')
        elif len(sides) == 2:
            print('Равнобедренный треугольник')
        else:
            print('Разносторонний треугольник')

    else:
        print('Такого треугольника не существует')

else:
    print('Wrong input!')

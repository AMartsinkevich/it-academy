#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №4
# Задание 3.

# пользователь вводит рост и вес,
# мы ему должны посчитать индекс массы тела и указать,
# в какую категорию по ИМТ он попадает: недостаток, норма или ожирение.
# Границы диапазонов для ИМТ можно погуглить

# Решение:

print('-' * 80)
print('Task 3')

input_height = input('Enter your height, kg: ')
input_weight = input('Enter your weight, cm: ')

if input_height.isdigit() and input_weight.isdigit():

    height = float(input_height) / 100
    weight = float(input_weight)

    bmi = round(weight / height ** 2, 2)
    print(f'Your Body Mass Index is {bmi}')

    if bmi < 16:
        print('Острый дефицит массы')
    elif bmi <= 18.5:
        print('Недостаточная масса тела')
    elif bmi <= 25:
        print('Норма')
    elif bmi <= 30:
        print('Избыточная масса тела')
    elif bmi <= 35:
        print('Ожирение первой степени')
    elif bmi <= 40:
        print('Ожирение второй степени')
    else:
        print('Ожирение третьей степени	')

else:
    print('Wrong input!')

#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №9
# Задание 1.

# Реализовать программу для подсчёта индекса массы 
# тела человека. Пользователь вводит рост и вес с клавиатуры. 
# На выходе – ИМТ и пояснение к нему в зависимости от 
# попадания в тот или иной диапазон. Использовать обработку 
# исключений.

# Решение:


def get_user_int_value(message: str = 'Enter integer grater than zero: ') -> int:
    '''Return integer value provided with user input'''

    value = None
    while not value:
        value = input(message)

        if value.isdecimal():
            return int(value) 
        else:
            print('Wrong input!')
            raise ValueError('Enter integer value for parameter')

def get_bmi_categorie(bmi: float) -> str:
    '''Return description of given BMI value'''

    if bmi <= 18.5:
        return 'Underweight'
    if bmi <= 24.9:
        return 'Normal weight'
    if bmi <= 29.9:
        return 'Overweight'
    if bmi >= 30:
        return 'Obesity'


print('-' * 80)
print('Task 1')


print('BMI Calculator')
height = get_user_int_value('Enter your height in cm: ') / 100
weight = get_user_int_value('Enter your weight in kg: ')
bmi = round(weight / height ** 2, 1)

print(f'Your BMI value is {bmi}. You are in the {get_bmi_categorie(bmi)} categorie')

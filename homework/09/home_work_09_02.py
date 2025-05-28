#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №9
# Задание 2.

# Реализовать программу с функционалом калькулятора 
# для операций над двумя числами. Числа и операция вводятся 
# пользователем с клавиатуры. Использовать обработку 
# исключений. 

# Решение:


def get_user_float_value(message: str = 'Enter integer grater than zero: ') -> float:
    '''Return float value provided with user input'''

    value = None
    while not value:
        value = input(message)

        if value.isdigit():
            return int(value) 
        else:
            print('Wrong input!')
            raise ValueError('Enter digital value for parameter')

def calc(operand_left: float, operand_right: float, operation: str) -> float:
    '''Return calculated value'''

    if operation == '+':
        return operand_left + operand_right
    if operation == '-':
        return operand_left - operand_right
    if operation == '*':
        return operand_left * operand_right
    if operation == '/':
        if operand_right == 0:
            raise ZeroDivisionError('Please use non-zero right operand while dividing')
        return operand_left / operand_right
    raise ValueError('Enter +, -, * or / for type operation')


print('-' * 80)
print('Task 2')


print('Calculator')
left_operand = get_user_float_value('Enter your first operand: ')
right_operand = get_user_float_value('Enter your second operand: ')
operator = input('Enter oprator (one of +, -, *, /): ')
print(f'Calculated value of {left_operand}{operator}{right_operand} = {calc(left_operand, right_operand, operator)}')

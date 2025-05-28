#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 6.

# Сводка расходов по категориям Есть список словарей — операции банковской выписки:

# ops = [
#     {'category': 'еда', 'amount': 780},
#     {'category': 'транспорт', 'amount': 55},
#     …
# ]

# Сгруппируйте суммы по ключу category и выведите отчёт вида:

# еда: 4 350 ₽
# транспорт: 1 120 ₽

# Решение:

print('-' * 80)
print('Task 6')

operations = [
    {'category': 'Food', 'amount': 780},
    {'category': 'Transportation', 'amount': 55},
    {'category': 'Clothing', 'amount': 420},
    {'category': 'Food', 'amount': 120},
    {'category': 'Fun', 'amount': 160},
    {'category': 'Transportation', 'amount': 15},
    {'category': 'Clothing', 'amount': 110},
    {'category': 'Food', 'amount': 20},
    {'category': 'Transportation', 'amount': 15},
    {'category': 'Food', 'amount': 70},
    {'category': 'Transportation', 'amount': 25},
    {'category': 'Fun', 'amount': 30},
    {'category': 'Clothing', 'amount': 410},
    {'category': 'Fun', 'amount': 160}
]

total_spending = {}

for operation in operations:
    if total_spending.get(operation['category']):
        total_spending[operation['category']] += operation['amount']
    else:
        total_spending[operation['category']] = operation['amount']

print('You total spendings:')
print(f"{'Category':^30}{'Amount':^10}")
for category, amount in total_spending.items():
    print(f'{category:<30} ${amount:^10}')

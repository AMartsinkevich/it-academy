#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 10.

# Маша хочет накопить на телефон, который стоит N
# денег. Маша может откладывать k рублей каждый день, 
# кроме воскресенья (в воскресенье она тратит эти деньги на 
# поход в кино). Маша начинает копить в понедельник. За 
# сколько дней она накопит нужную сумму? Проверку на 
# воскресенье сделать через if. 

# Решение:

print('-' * 80)
print('Task 10')

phone_cost = float(input('Enter cost of the phone: '))
saving = float(input('Enter amount of savings per day: '))

weeks = int((phone_cost / saving) // 6)
last_week_without_sunday = 1 if weeks and ((phone_cost / saving) % 6 == 0) else 0
sundays = weeks - last_week_without_sunday
days = int(phone_cost / saving) if phone_cost % saving == 0 else int(phone_cost / saving + 1)
total_days = days + sundays

print(f'Starting from Monday and skipping Sundays you need: {total_days} days')

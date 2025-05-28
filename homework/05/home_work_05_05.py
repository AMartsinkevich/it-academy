#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 5.

# Трекинг шагов фитнес-браслета Список содержит количества шагов за каждый час суток (24 числа).
# Найдите суммарные шаги за день.
# Определите «самый активный» час (максимум шагов).

# Решение:

from random import randint

print('-' * 80)
print('Task 5')

steps_per_hour = [0 for _ in range(6)]
steps_per_hour.extend([randint(0, 1500) for _ in range(15)])
steps_per_hour.extend([0 for _ in range(3)])


print(steps_per_hour)
print(len(steps_per_hour))
total_steps = 0
max_steps_per_hour = 0
max_activity_hour = 0
for hour, steps in enumerate(steps_per_hour):
    total_steps += steps
    if steps > max_steps_per_hour:
        max_steps_per_hour = steps
        max_activity_hour = hour

print(f'''Your daily report.
Total steps per day: {total_steps},
maximum amount per hour: {max_steps_per_hour},
most active period: from {max_activity_hour} to {max_activity_hour + 1} hour.''')

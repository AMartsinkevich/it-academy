#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 1.

# Чат-модератор: счётчик запрещённых слов
# Юзер вводит сообщение Цикл продолжается,
# пока количество «плохих» слов не достигнет 5.
# Список запрещённых слов храните заранее.
# Как только пользователь понаписал 5 сообщений
# с запрещенными словами, он получает сообщение о бане. 

# Решение:

print('-' * 80)
print('Task 1')

ban_words = {'elka', 'ezh', 'eshche'}
is_not_ban = 5

while is_not_ban:
    input_string = input('Enter your message (will be premoderated): ')
    if len(ban_words - {word.strip(' .,!?') for word in input_string.lower().split()}) != len(ban_words):
        is_not_ban -= 1
        input_string = '***Censored***'
        print(f'Warning! We are using Jo in words! {is_not_ban} time(s) of 5 fails left to ban!')
    print(f'ChattieChat Message: {input_string}')
else:
    print('Gotcha! You are banned!')

#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №6
# Задание 5.

# Программа получает на вход строку – сообщение и 
# указание, что нужно сделать – шифровать или дешифровать. 
# Реализовать две функции: первая шифрует заданное 
# сообщение шифром Цезаря, вторая расшифровывает. В 
# зависимости от выбора пользователя (шифровать или 
# дешифровать) вызывается соответствующая функция, 
# результат выводится в консоль. 

# WARNING:

# - Обязательно организовываем ДЗ в форме меню
# - Обязательно делаем проверки вводимых данных и даём юзеру перепопытки ввода
# - Обязательно каждая задача в виде отдельной функции
# - Обязательно соблюдаем структуру файла: сначала все импорты, потом все функции, потом основной код
# - Обязательно следим за пробелами и отступами, пользуемся Ctrl Alt L по необходимости
# - Желательно задаём аннотации типов аргументов и возвращаемых значений для функции
# - Желательно оставляем документацию к функции
# - Желательно сдаём домашку не за пару часов до следующего занятия

# Решение:

def cipher_text(value: str, operation: str, shift: int = 3) -> str:
    '''Encode/decode message using Cesarus algorithm'''

    cipher = ''
    en_lo = 'abcdefghijklmnopqrstuvwxyz'
    en_hi = en_lo.upper()
    ru_lo = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ru_hi = ru_lo.upper()
    en_ru_lo_hi = f'{en_hi}{en_lo}{ru_hi}{ru_lo}'
    shift = shift if operation == 'E' else (-1) * shift
    for char in value:
        if char not in en_ru_lo_hi:
            cipher += char
        else:
            index = en_ru_lo_hi.find(char)
            new_index = index + shift
            if 0 <= index <= 25:
                if new_index > 25:
                    new_index -= 26
                elif new_index < 0:
                    new_index += 26
                cipher += en_ru_lo_hi[new_index]                    
            if 26 <= index <= 51:
                if new_index > 51:
                    new_index -= 26
                elif new_index < 26:
                    new_index += 26
                cipher += en_ru_lo_hi[new_index]                    
            if 52 <= index <= 84:
                if new_index > 84:
                    new_index -= 33
                elif new_index < 52:
                    new_index += 33
                cipher += en_ru_lo_hi[new_index]                    
            if 85 <= index <= 117:
                if new_index > 117:
                    new_index -= 33
                elif new_index < 85:
                    new_index += 33
                cipher += en_ru_lo_hi[new_index]                    
    return cipher


print('-' * 80)
print('Task 5')


value = None
while not value:
    value = input('Enter string to encode/decode: ')

operation = None
while not operation:
    operation = input('Enter operation to apply. "E"ncode or "D"ecode: ')
    if operation not in ('E', 'D'):
        operation = None
        print('Wrong input!')

print(f"Let's try to {'encript' if operation == 'E' else 'decrypt'} your message: {cipher_text(value, operation)}")

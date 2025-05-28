#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №5
# Задание 4.

# Контрольная из пяти вопросов
# В списке хранятся правильные ответы последовательно на каждый вопрос,
# например answers = ['c', 'a', 'b', 'd', 'b']. Вопросы заданы в отдельном списке. 
# Задавайте юзеру вопросы, спрашивайте у пользователя ответы один за другим, сравнивайте,
# подсчитывайте баллы и выведите результат. Например: «3/5 верно»
# Усложнение: организовать хранение вопросов-ответов не в виде двух списков,
# а в виде списка словарей, в каждом из словарей ключ - номер вопроса,
# значение - кортеж из самого вопроса и ответа на него. Индекс словаря в списке - это номер вопроса. 

# Решение:

from random import shuffle

print('-' * 80)
print('Task 4')

exam_qa = [
    {1: ('Who is Shark? A. Tralalero Tralala; B. Bombardiro Crocodilo', 'A')},
    {2: ('Who is BigFoot? A. Boneca Ambalabu; B. Brr Brr Patapim', 'B')},
    {3: ('What is the language of AI animals? A. German; B. Brazilian; C. Japaneese; D. Russian; E. Italian', 'E')},
    {4: ('What programming languages they related to? A. ADA; B. ALGOL; C. FORTRAN; D. Python', 'D')},
    {5: ('What is the number of the planet of this creatures? A. 2 - Venus; B. 3 - Earth; C. 9 - Pluto', 'B')}
]

print("Let's start our exam session. Answer for the next five questions")
mark = 0
shuffle(exam_qa)
for ticket in exam_qa:
    for number, content in ticket.items():
        question, answer = content
        print(f'Exam ticket: {number}. Question: {question}')
        user_input = input('Enter you answer (one lettter): ').capitalize()
        if user_input == answer:
            mark += 1

print(f'Your score is: {mark} of 5')

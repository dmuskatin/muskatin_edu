# В начале работы, программа спрашивает как зовут пользователя
# и приветствует его.

user_name = input('Введите Ваше имя ')
print(f'Привет, {user_name}, начинаем тренировку!')

# вводим переменные счетчики и списки вопросов и ответов
score = 0
score_percent = 0
score_question = 0

# варианты вопросов и ответов будем хранить в соответсвующих списках
questions = ["My name __ Vova", "I __ a coder", "I live __ Moscow"]
answers = ["is", "am", "in"]

# делаем цикл вопросов и ответов
for i in range(0, len(questions)):
    print(questions[i])
    user_answer = input()

    if user_answer == answers[i]:
        score += 10
        score_question += 1
        print("Ответ верный! \n"
       "Вы получаете 10 баллов!")
    else:
        print(f"Неправильно. \n"
        f"Правильный ответ: {answers[i]}")

score_percent = round(score * 100 / 30, 2)
score_question = round(score / 10)

# выводим на экран результаты теста в баллах и процентах
print()
print(f"Вот и все {user_name}!\n"
      f"Количество верных ответов: {score_question}. \n"
      f"Ваш счет: {score}. \n"
      f"Процент правильных ответов: {score_percent}. \n")

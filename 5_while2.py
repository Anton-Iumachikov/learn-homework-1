questions_and_answers = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",

}

def ask_user(answers_dict):
    while True:
        user_question = input("Задайте вопрос: ")
        if user_question in answers_dict: #не до конца понимаю
            print(answers_dict[user_question]) #не до конца понимаю

ask_user(questions_and_answers) #не до конца понимаю

if __name__ == "__main__":
    hello_user()

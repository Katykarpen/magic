import random

def fate():
    quest = input("Задавайте вопрос: ")
    answers = [
        "Да",
        "Нет",
        "Не сомневайся",
        "Перспективы есть",
        "Спроси позже",
        "Не очевидные перспективы",
        "Звезды не отвечают",
        "Мало шансов",
        "У тебя все получиться",
        "Возможно все",
        "Надо подождать",
        "Плохая идея",
        "Измени вопрос",
    ]

    if quest == "выход":
        print("Хорошего дня")
    else:
        print(random.choice(answers))
        fate()


fate()
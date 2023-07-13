import random


def randomStr():
    randomList = [
        "I don't understand, try rephrasing that?",
        "You've written something I don't understand yet",
        "What are you on about?",
        "...what?",
        "I'm sorry, you might want to ask someone else about that."
    ]

    listCount = len(randomList)
    randomItem = random.randrange(listCount)

    return randomList[randomItem]
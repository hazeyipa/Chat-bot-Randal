import random

def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "What are you on about?",
        "...what?",
        "I've got no idea what you're saying, man."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]


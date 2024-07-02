from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def launch_game():
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(question), correct_answer

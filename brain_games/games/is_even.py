from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANGE = 1
END_RANGE = 100


def launch_game():
    question = randint(START_RANGE, END_RANGE)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

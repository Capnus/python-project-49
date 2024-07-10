from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANGE = 1
END_RANGE = 100


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def launch_game():
    question = randint(START_RANGE, END_RANGE)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

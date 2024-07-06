from random import randint, choice

RULE = 'What is the result of the expression?'
START_RANGE = 1
END_RANGE = 100


def launch_game():
    num_1 = randint(START_RANGE, END_RANGE)
    num_2 = randint(START_RANGE, END_RANGE)
    question = 0
    correct_answer = 0
    operator = choice('+-*')
    if operator == '+':
        correct_answer = num_1 + num_2
        question = f'{num_1} + {num_2}'
    if operator == '-':
        correct_answer = num_1 - num_2
        question = f'{num_1} - {num_2}'
    if operator == '*':
        correct_answer = num_1 * num_2
        question = f'{num_1} * {num_2}'
    return question, str(correct_answer)

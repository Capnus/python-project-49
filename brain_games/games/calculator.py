from random import randint, choice

RULE = 'What is the result of the expression?'
RANDOM_NUM_1, RANDOM_NUM_2 = randint(1, 10), randint(1, 10)


def launch_game():
    global RANDOM_NUM_1, RANDOM_NUM_2
    question = 0
    correct_answer = 0
    sign = choice('+-*')
    if sign == '+':
        correct_answer = RANDOM_NUM_1 + RANDOM_NUM_2
        question = str(RANDOM_NUM_1) + " + " + str(RANDOM_NUM_2)
    if sign == '-':
        correct_answer = RANDOM_NUM_1 - RANDOM_NUM_2
        question = str(RANDOM_NUM_1) + " - " + str(RANDOM_NUM_2)
    if sign == '*':
        correct_answer = RANDOM_NUM_1 * RANDOM_NUM_2
        question = str(RANDOM_NUM_1) + " * " + str(RANDOM_NUM_2)
    return str(question), str(correct_answer)

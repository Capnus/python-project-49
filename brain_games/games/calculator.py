from random import randint, choice

RULE = 'What is the result of the expression?'
START_RANGE = 1
END_RANGE = 100


def launch_game():
    num_1, num_2 = randint(START_RANGE, END_RANGE), randint(START_RANGE, END_RANGE)
    question = 0
    correct_answer = 0
    sign = choice('+-*')
    if sign == '+':
        correct_answer = num_1 + num_2
        question = str(num_1) + " + " + str(num_2)
    if sign == '-':
        correct_answer = num_1 - num_2
        question = str(num_1) + " - " + str(num_2)
    if sign == '*':
        correct_answer = num_1 * num_2
        question = str(num_1) + " * " + str(num_2)
    return str(question), str(correct_answer)

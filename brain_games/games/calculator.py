from random import randint, choice

RULE = 'What is the result of the expression?'


def launch_game():
    question = 0
    correct_answer = 0
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
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

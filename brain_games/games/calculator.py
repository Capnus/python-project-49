from random import randint, choice


def rule():
    return 'What is the result of the expression?'


def launch_game():
    question = 0
    correct_answer = 0
    a = randint(1, 10)
    b = randint(1, 10)
    sign = choice('+-*')
    if sign == '+':
        correct_answer = a + b
        question = str(a) + " + " + str(b)
    if sign == '-':
        correct_answer = a - b
        question = str(a) + " - " + str(b)
    if sign == '*':
        correct_answer = a * b
        question = str(a) + " * " + str(b)
    return str(question), str(correct_answer)

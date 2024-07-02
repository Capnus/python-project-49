from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RANDOM_NUM_1 = randint(1, 100)

def launch_game():
    global RANDOM_NUM_1
    question = RANDOM_NUM_1
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(question), correct_answer

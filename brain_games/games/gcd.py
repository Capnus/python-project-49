from random import randint
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'
RANDOM_NUM_1, RANDOM_NUM_2 = randint(1, 100), randint(1, 100)


def launch_game():
    global RANDOM_NUM_1, RANDOM_NUM_2
    question = str(RANDOM_NUM_1) + ' ' + str(RANDOM_NUM_2)
    correct_answer = gcd(RANDOM_NUM_1, RANDOM_NUM_2)
    return str(question), str(correct_answer)

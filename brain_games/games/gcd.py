from random import randint
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
END_RANGE = 100


def launch_game():
    num_1 = randint(START_RANGE, END_RANGE)
    num_2 = randint(START_RANGE, END_RANGE)
    question = str(num_1) + ' ' + str(num_2)
    correct_answer = gcd(num_1, num_2)
    return str(question), str(correct_answer)

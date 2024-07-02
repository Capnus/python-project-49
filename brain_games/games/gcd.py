from random import randint
from math import gcd


RULE = 'Find the greatest common divisor of given numbers.'


def launch_game():
    num_1, num_2 = randint(1, 100), randint(1, 100)
    question = str(num_1) + ' ' + str(num_2)
    correct_answer = gcd(num_1, num_2)
    return str(question), str(correct_answer)

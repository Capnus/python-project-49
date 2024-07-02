from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANDOM_NUM_1 = randint(1, 100)


def launch_game():
    global RANDOM_NUM_1
    question = RANDOM_NUM_1
    count_divisors = 0
    for i in range(2, (question + 1) // 2):
        if question % i == 0:
            count_divisors += 1
    if count_divisors == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(question), correct_answer

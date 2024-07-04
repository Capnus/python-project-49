from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANGE = 1
END_RANGE = 100


def launch_game():
    question = randint(START_RANGE, END_RANGE)
    count_divisors = 0
    for i in range(2, (question + 1) // 2):
        if question % i == 0:
            count_divisors += 1
    if count_divisors == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(question), correct_answer

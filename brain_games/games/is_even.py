from random import randint

def rule():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def launch_game():
    question = randint(1, 99)
    count_divisors = 0
    for i in range(2, (question + 1) // 2):
        if question % i == 0:
            count_divisors += 1
    if count_divisors == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(question), correct_answer


from random import randint


def rule():
    return 'Find the greatest common divisor of given numbers.'


def launch_game():
    a, b = randint(1, 100), randint(1, 100)
    question = str(a) + ' ' + str(b)
    divisor_a = []
    divisor_b = []
    for i in range(1, ((a + 1) // 2) + 1):
        if a % i == 0:
            divisor_a.append(i)
    for i in range(1, ((b + 1) // 2) + 1):
        if b % i == 0:
            divisor_b.append(i)
    common_divisor = list(set(divisor_a) & set(divisor_b))
    correct_answer = max(common_divisor)
    return str(question), str(correct_answer)

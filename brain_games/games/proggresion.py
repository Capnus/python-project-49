from random import randint

RULE = 'What number is missing in the progression?'
RANDOM_NUM_1, RANDOM_NUM_2 = randint(1, 5), randint(1, 99)


def launch_game():
    global RANDOM_NUM_1, RANDOM_NUM_2
    step_list = RANDOM_NUM_1
    question = [RANDOM_NUM_2]
    for i in range(10):
        question.append(question[i] + step_list)

    random_index = randint(0, 9)
    correct_answer = question.pop(random_index)
    question.insert(random_index, '..')
    question = ' '.join(str(num) for num in question)
    return question, str(correct_answer)

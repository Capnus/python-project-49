from random import randint

RULE = 'What number is missing in the progression?'


def launch_game():
    step_list = randint(1, 5)
    question = [randint(1, 99)]
    for i in range(10):
        question.append(question[i] + step_list)

    random_index = randint(0, 9)
    correct_answer = question.pop(random_index)
    question.insert(random_index, '..')
    question = ' '.join(str(num) for num in question)
    return question, str(correct_answer)

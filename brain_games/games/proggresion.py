from random import randint

RULE = 'What number is missing in the progression?'
START_RANGE = 1
END_RANGE = 100
END_RANGE_STEP = 5
END_RANGE_INDEX = 9
END_RANGE_LENGTH = 10


def launch_game():
    length_progression = randint(END_RANGE_INDEX, END_RANGE_LENGTH)
    step_list = randint(START_RANGE, END_RANGE_STEP)
    question = [randint(START_RANGE, END_RANGE)]
    for i in range(length_progression):
        question.append(question[i] + step_list)
    random_index = randint(START_RANGE, END_RANGE_INDEX)
    correct_answer = question[random_index]
    question[random_index] = '..'
    question = ' '.join(str(num) for num in question)
    return question, str(correct_answer)

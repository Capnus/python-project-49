import prompt
count_correct_answers = 0
name = ''


def greet():
    print('Welcome to the Brain Games!')
    global name
    name = 'Nick'
    print(f'Hello, {name}!')


def core_games(launch_game):
    question, correct_answer = launch_game
    global count_correct_answers
    if count_correct_answers == 3:
        print(f'Congratulations, {name}!')
        return 'end'
    print('Question: ', question)
    answer = input()
    print('Your answer: ', answer)
    if answer == correct_answer:
        print('Correct!')
        count_correct_answers += 1
        return
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return 'end'

import prompt
COUNT_CORRECT_ANSWERS = 0
NAME = ''


def greet():
    print('Welcome to the Brain Games!')
    global NAME
    NAME = prompt.string('May I have your name? ')
    print(f'Hello, {NAME}!')


def core_games(launch_game):
    while launch_game != 'end':
        question, correct_answer = launch_game()
        global COUNT_CORRECT_ANSWERS
        if COUNT_CORRECT_ANSWERS == 3:
            print(f'Congratulations, {NAME}!')
            return 'end'
        print('Question:', question)
        answer = input()
        print('Your answer:', answer)
        if answer == correct_answer:
            print('Correct!')
            COUNT_CORRECT_ANSWERS += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {NAME}!")
            return 'end'

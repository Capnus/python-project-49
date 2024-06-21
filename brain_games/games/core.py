from brain_games.cli import welcome_user

name = welcome_user()


def core_games(launch_game):
    count_correct_answers = 0
    while True:
        question, correct_answer = launch_game
        if count_correct_answers == 3:
            print(f'Congratulations, {name}!')
            break
        print('Question: ', question)
        answer = input()
        print('Your answer: ', answer)
        if answer == correct_answer:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

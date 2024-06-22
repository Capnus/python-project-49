import prompt

for _ in range(3):
    def core_games(launch_game):
        print('Welcome to the Brain Games!')
        name = prompt.string('May I have your name? ')
        print(f'Hello, {name}!')
        count_correct_answers = 0
        question, correct_answer = launch_game
        while True:
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

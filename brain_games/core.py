import prompt


def start_core(launch_game, rule):
    count_correct_answers = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rule)
    while count_correct_answers < 4:
        if count_correct_answers == 3:
            print(f'Congratulations, {name}!')
            return
        question, correct_answer = launch_game()
        print(f'Question: {question}')
        answer = input()
        print(f'Your answer: {answer}')
        if answer == correct_answer:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

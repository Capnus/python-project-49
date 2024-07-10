import prompt
COUNT_ROUNDS = 3


def start_core(launch_game, rule):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rule)
    for _ in range(COUNT_ROUNDS):
        question, correct_answer = launch_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer:')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    return

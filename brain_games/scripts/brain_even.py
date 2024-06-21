#!/usr/bin/env python3
from random import randint
import prompt


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')


def brain_even():
    print('Answer "yes"  if the number is even, otherwise answer "no".')
    count_correct_answer = 0
    while count_correct_answer != 3:
        number = randint(1, 100)
        print('Question: ', number)
        answer = input()
        print('Your answer: ', answer)
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                count_correct_answer += 1
            if answer != 'yes':
                return print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
        elif number % 2 != 0:
            if answer == 'no':
                print('Correct!')
                count_correct_answer += 1
            if answer != 'no':
                return print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!" )
                
    print(f'Congratulations, {name}!')


def main():
    brain_even()


if __name__ == '__main__':
    main()

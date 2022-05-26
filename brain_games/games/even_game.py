from brain_games.check_answer import check_answer
from random import random


def play_even_game(name):
    """Brain-even

    Answer "yes" if the number is even, otherwise answer "no"

    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win = 0
    while win < 3 and win != -1:

        rand_int = int(random() * 100)
        correct_answer = 'yes' if rand_int % 2 == 0 else 'no'

        print(f'Question: {rand_int}')
        answer = input('Your answer: ')

        win = check_answer(name, answer, correct_answer, win, must_be_int=False)

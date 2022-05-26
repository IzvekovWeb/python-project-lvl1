from brain_games.check_answer import check_answer
import random


def play_prime_game(name):
    """Brain-prime

    Показываем игроку число, он должен угадать простое оно или нет=

    """

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    win = 0
    while win < 3 and win != -1:

        value = random.randint(0, 101)
        correct_answer = 'yes' if is_prime(value) else 'no'

        print(f'Question: {value}')
        answer = input('Your answer: ')

        win = check_answer(name, answer, correct_answer, win, must_be_int=False)


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

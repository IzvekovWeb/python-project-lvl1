from brain_games.check_answer import check_answer
import random


def play_gcd_game(name):
    """Game-gcd

    Суть игры в следующем: пользователю показывается два случайных числа,
    например, 25 50. Пользователь должен вычислить и ввести наибольший
    общий делитель этих чисел

    """
    print('Find the greatest common divisor of given numbers.')
    win = 0
    while win < 3 and win != -1:

        rand_values = [random.randint(0, 100), random.randint(0, 100)]
        correct_answer = find_nod(rand_values[0], rand_values[1])

        print(f'Question: {rand_values[0]} {rand_values[1]}')
        answer = input('Your answer: ')

        win = check_answer(name, answer, correct_answer, win, must_be_int=True)


def find_nod(x, y):
    while y > 0:
        z = y
        y = x % y
        x = z
    return x

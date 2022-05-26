from brain_games.check_answer import check_answer
import random


def play_calc_game(name):
    """Brain-calc

    Cуть игры в следующем: пользователю показывается случайное
    математическое выражение,например 35 + 16, которое нужно
    вычислить и записать правильный ответ

    """
    oper = ('+', '-', '*')

    win = 0
    while win < 3 and win != -1:
        rand_values = [random.randint(0, 100), random.randint(0, 100)]
        rand_index = random.randint(0, len(oper) - 1)

        question_fstr = f'{rand_values[0]} {oper[rand_index]} {rand_values[1]}'
        correct_answer = eval(question_fstr)

        print(f'Question: {question_fstr}')
        answer = input('Your answer: ')

        win = check_answer(name, answer, correct_answer, win, must_be_int=True)

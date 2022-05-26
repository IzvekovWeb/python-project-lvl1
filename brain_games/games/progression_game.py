from brain_games.check_answer import check_answer
import random


def play_progression_game(name):
    """Brain-progression

    Показываем игроку ряд чисел, образующий арифметическую прогрессию,
    заменив любое из чисел двумя точками. Игрок должен определить это число

    """

    win = 0
    while win < 3 and win != -1:

        p_length = random.randint(5, 11)
        p_start = random.randint(1, 10)
        p_step = random.randint(1, 5)

        progression = [i for i in range(p_start,
                                        p_length * p_step + p_start,
                                        p_step)]

        hidden_index = random.randint(0, p_length - 1)
        correct_answer = progression[hidden_index]

        progression[hidden_index] = '..'

        print(f'Question: {" ".join(str(x) for x in progression)}')
        answer = input('Your answer: ')

        win = check_answer(name, answer, correct_answer, win, must_be_int=True)

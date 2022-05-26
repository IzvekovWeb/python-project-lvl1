from brain_games.is_int import is_int


def check_answer(name, answer, correct_answer, wins, must_be_int):

    if must_be_int:
        if not is_int(answer) or int(answer) != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n \
            Let's try again, {name}!")
            wins = -1
        else:
            print('Correct!')
            wins += 1
    else:
        if answer == correct_answer:
            print('Correct!')
            wins += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n \
            Let's try again, {name}!")
            wins = -1

    if wins == 3:
        print(f'Congratulations, {name}!')

    return wins

import random


def play_prime_game(name):
    """Brain-prime

<<<<<<< HEAD
    According to the player's idea, the number that he must guess simply or not.
=======
    Показываем игроку число, он должен угадать простое оно или нет
>>>>>>> f0a82672f0ea7fc6f49491437551e2bc323d5352

    """

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    win = 0
    while win < 3:

        value = random.randint(0, 101)
        correct_answer = 'yes' if is_prime(value) else 'no'

        print(f'Question: {value}')
        answer = input('Your answer: ')

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n \
                Let's try again, {name}!")
            break
        else:
            print('Correct!')
            win += 1
        if win == 3:
            print(f'Congratulations, {name}!')


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

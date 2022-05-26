from brain_games.cli import welcome_user
from brain_games.games.prime_game import play_prime_game


def main():
    """Brain-prime main"""

    user_name = welcome_user()
    play_prime_game(user_name)


if __name__ == '__main__':
    main()

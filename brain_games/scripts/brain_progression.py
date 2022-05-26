from brain_games.cli import welcome_user
from brain_games.games.progression_game import play_progression_game


def main():
    """Brain-even main"""

    user_name = welcome_user()
    play_progression_game(user_name)


if __name__ == '__main__':
    main()

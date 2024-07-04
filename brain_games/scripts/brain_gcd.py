#!/usr/bin/env python3
from brain_games.games.gcd import launch_game, RULE
from brain_games.core import core_games, greet


def main():
    greet()
    print(RULE)
    core_games(launch_game)


if __name__ == '__main__':
    main()

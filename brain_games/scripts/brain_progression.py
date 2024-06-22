#!/usr/bin/env python3
from brain_games.games.proggresion import launch_game, rule
from brain_games.games.core import core_games, greet


def main():
    greet()
    print(rule())
    while core_games(launch_game()) != 'end':
        a = 'zaglushka'


if __name__ == '__main__':
    main()
    
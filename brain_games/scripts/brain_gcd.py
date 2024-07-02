#!/usr/bin/env python3
from brain_games.games.gcd import launch_game, RULE
from brain_games.games.core import core_games, greet


def main():
    greet()
    print(RULE)
    while core_games(launch_game()) != 'end':
        a = 'zaglushka'


if __name__ == '__main__':
    main()
 
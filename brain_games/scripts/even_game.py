#!/usr/bin/env python3
from brain_games.games.is_even import launch_game, RULE
from brain_games.core import core_games, greet


def main():
    greet()
    print(RULE)
    while core_games(launch_game()) != 'end':
        a = 'zaglushka'


if __name__ == '__main__':
    main()
  
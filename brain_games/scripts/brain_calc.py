#!/usr/bin/env python3
from brain_games.games.calculator import launch_game, RULE
from brain_games.core import start_core


def main():
    start_core(launch_game, RULE)


if __name__ == '__main__':
    main()

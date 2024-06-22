#!/usr/bin/env python3
from brain_games.games.calculator import launch_game, rule
from brain_games.games.core import core_games

rule = rule()


def main():
    launch_game()
    core_games()


if __name__ == '__main__':
    main()
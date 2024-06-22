#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.is_even import launch_game, rule
from brain_games.scripts.brain_games import greet
from brain_games.games.core import core_games

rule = rule()


def main():
    greet()
    launch_game()
    core_games()


if __name__ == '__main__':
    main()

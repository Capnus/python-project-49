#!/usr/bin/env python3
from brain_games.games import is_prime
from brain_games.core import start_core


def main():
    start_core(is_prime)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    return f'Hello, {name}!'


def main():
    welcome_user()


if __name__ == '__main__':
    main()

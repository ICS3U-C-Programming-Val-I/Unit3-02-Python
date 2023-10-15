#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: October 15, 2023
# This program asks the user to guess a number
# then lets them know if they're right or wrong.

CORRECT_GUESS = 7


def main():
    # Input - Get user guess
    user_guess = int(input("What is your guess?\n"))

    # process - Check if guess is correct
    if user_guess == CORRECT_GUESS:
        print("You are CORRECT!!!!!")
    elif user_guess != CORRECT_GUESS:
        print("You are INCORRECT!!!!!")


if __name__ == "__main__":
    main()

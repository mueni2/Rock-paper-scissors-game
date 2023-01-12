# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

CHOICES = 'rps'


def get_player_choice():
    """Get user input and validate it is one of the choices above"""
    player_choice = None
    while player_choice is None:
        player_choice = input('Choices: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()


def get_computer_choice():
    """Have the computer pick one of the valid choices at random"""
    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    return computer_choice


def is_draw(player_choice, computer_choice):
    """Check if game was a draw"""
    if player_choice == computer_choice:
        return True

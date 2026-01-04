import os
from typing import List
from deck import Deck
from hand import Hand
from card import CardEnum
from actions import ActionEnum

def clear_screen():
    # Check the operating system
    if os.name == 'nt':
        # For Windows
        _ = os.system('cls')
    else:
        # For macOS and Linux (os.name is 'posix')
        _ = os.system('clear')


def get_alive_str(players: List[Hand]) -> str:
    alive_str = "Alive Players: \n"
    for i, player in enumerate(players):
        if player.is_alive():
            alive_str += f"Player {i + 1}\n"

    return alive_str

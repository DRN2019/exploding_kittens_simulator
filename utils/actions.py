from enum import Enum
from .card import CardEnum, card_names
from hand import Hand
from typing import List
from deck import Deck
import random

class ActionEnum(Enum):
    DEFUSE = 1
    ATTACK = 2
    TWO_CAT = 3
    FAVOR = 4
    NOPE = 5
    SEE_THE_FUTURE = 6
    SHUFFLE = 7
    SKIP = 8

action_names = {
    ActionEnum.DEFUSE: "Defuse",
    ActionEnum.ATTACK: "Attack",
    ActionEnum.TWO_CAT: "Steal a Card (Cat card pair)",
    ActionEnum.FAVOR: "Favor",
    ActionEnum.NOPE: "Nope",
    ActionEnum.SEE_THE_FUTURE: "See the Future",
    ActionEnum.SHUFFLE: "Shuffle",
    ActionEnum.SKIP: "Skip",
}

card_action_mapping = {
    CardEnum.DEFUSE: ActionEnum.DEFUSE,
    CardEnum.NOPE: ActionEnum.NOPE,
    CardEnum.ATTACK: ActionEnum.ATTACK,
    CardEnum.FAVOR: ActionEnum.FAVOR,
    CardEnum.SHUFFLE: ActionEnum.SHUFFLE,
    CardEnum.SKIP: ActionEnum.SKIP,
    CardEnum.SEE_THE_FUTURE: ActionEnum.SEE_THE_FUTURE,
    CardEnum.BEARD: ActionEnum.TWO_CAT,
    CardEnum.CATERMELON: ActionEnum.TWO_CAT,
    CardEnum.POTATO: ActionEnum.TWO_CAT,
    CardEnum.RAINBOW: ActionEnum.TWO_CAT,
    CardEnum.TACO: ActionEnum.TWO_CAT,
}

def print_all_user_actions():
    """
    Prints all actions
    """
    actions_str = ""
    for key, value in action_names.items():
        # TODO: Filter out Defuse and Nope as available actions, and corresponding choice value

        actions_str += f"{key}: {value}\n"

    print(actions_str)

def perform_action(action_enum: ActionEnum, players: List[Hand], cur_player: int, skipTurn: bool, isAttacked: bool, deck: Deck):
    match action_enum:
        case ActionEnum.ATTACK:
            attack(skipTurn, isAttacked)

        case ActionEnum.TWO_CAT:
            steal_card(players, cur_player)
            pass

        case ActionEnum.FAVOR:
            favor(players, cur_player)
            pass

        case ActionEnum.SHUFFLE:
            shuffle(deck)
            pass

        case ActionEnum.SKIP:
            skip(skipTurn)

        case ActionEnum.SEE_THE_FUTURE:
            see_the_future(deck)
            pass

        case _:
            raise ValueError("Match statement")
    pass


def attack(skipTurn: bool, isAttacked: bool):
    """
    Uses an attack card
    
    Effectively ends turn and makes next player go twice

    Args:
        skipTurn (bool): _description_
        isAttacked (bool): _description_
    """
    skipTurn = True
    isAttacked = True

def steal_card(players: List[Hand], cur_player: int):
    """
    Pair cat card action

    Steals a random card from another player

    Args:
        players (List[Hand]): _description_
        cur_player (int): _description_

    Raises:
        ValueError: _description_
    """
    # Check if any players have cards
    has_cards = False
    for player in players:
        has_cards = has_cards and player.get_n_cards() > 0

    if not has_cards:
        return

    # Select user to steal from
    while True:
        print(get_alive_str(players, cur_player))
        target_player_input = input("What player would you like to steal from?")

        try: 
            target_player = int(target_player_input) - 1

            # Validate input
            if target_player < 0 or target_player >= len(players) or target_player == cur_player or not players[target_player].is_alive():
                raise ValueError()
            
            if players[target_player].get_n_cards() == 0:
                print("This player has no cards left! Please choose another player!")
                continue
            
            # Steal a card from designated player
            card = random.choices(
                population=list(players[target_player].get_cards().keys()),
                weights=list(players[target_player].get_cards().values()),
                k=1
            )[0]

            players[cur_player].add_card(card)
            players[target_player].remove_card(card)

            print(f"You stole a {card_names[card]} card from player {target_player + 1}!")

        except Exception:
            print("Please input a valid player!")


def favor(players: List[Hand], cur_player: int):
    """
    Performs a favor action

    Args:
        players (List[Hand]): 
        cur_player (int): 

    Raises:
        ValueError: 
    """
    # Check if any players have cards
    has_cards = False
    for player in players:
        has_cards = has_cards and player.get_n_cards() > 0

    if not has_cards:
        return
    
    # Select user to ask favor from
    while True:
        print(get_alive_str(players, cur_player))
        target_player_input = input("What player would you like to ask a favor from?")

        try: 
            target_player = int(target_player_input) - 1

            # Validate input
            if target_player < 0 or target_player >= len(players) or target_player == cur_player or not players[target_player].is_alive():
                raise ValueError()
            
            if players[target_player].get_n_cards() == 0:
                print("This player has no cards left! Please choose another player!")
                continue
            
            # Let target player select a card
            print(f"Player {target_player + 1}")
            print(f"Your current hand:")
            print(players[target_player].get_cards_str())
            card = None
            while True:
                card_choice = input(f"Player {target_player + 1}, which card would you like to give?")

                for card_type, card_name in card_names.items():
                    if card_choice.lower() == card_name.lower():
                        card = card_type

                if card != None:
                    break

                print("Please select a valid card!")

            players[cur_player].add_card(card)
            players[target_player].remove_card(card)

            print(f"You received a {card_names[card]} card from player {target_player + 1}!")

        except Exception:
            print("Please input a valid player!")

def nope():
    pass

def see_the_future(deck: Deck):
    """
    Prints out the top 3 cards of the deck

    Args:
        deck (Deck): Deck

    """
    top_3 = deck.see_top_3()
    top_3_names = [card_names[card] for card in top_3]
    print("Top 3 Cards: " + ", ".join(top_3_names))

def shuffle(deck: Deck):
    deck.shuffle()

def skip(skipTurn: bool):
    """
    Skips the player's turn

    Args:
        skipTurn (bool): skipTurn variable to be changed
    """
    skipTurn = True

def get_alive_str(players: List[Hand], cur_player: int, include_card_ct: bool = False) -> str:
    """
    Utility function that returns a string of alive players to choose from that is not the current player

    Args:
        players (List[Hand]): _description_
        cur_player (int): _description_
        include_card_ct (bool, optional): _description_. Defaults to False.

    Returns:
        str: _description_
    """
    alive_str = "Players: \n"
    for i, player in enumerate(players):
        if cur_player != i and player.is_alive():
            alive_str += f"Player {i + 1}"

            if include_card_ct:
                alive_str += f" ({player.get_n_cards()} cards)"

            alive_str += "\n"

    return alive_str
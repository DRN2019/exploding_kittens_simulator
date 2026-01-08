import random
from utils.deck import Deck
from utils.hand import Hand
from utils.card import CardEnum, card_names
from utils.actions import ActionEnum, print_all_user_actions, action_names
from utils.user_actions import perform_action
from utils.util import clear_screen
from typing import List
import utils.constants as const


def main():
    """
    Game state

    Initialization:
    - Intake number of players
    - Create Deck, shuffle, deal out inital cards
    - Insert exploding kitten cards + spare defuse cards

    Playing:
    - Current player draws a card
        1. Check if drew an exploding kitten. If exploding kitten is drawn
            a. If player has a defuse, use it and ask where to insert the exploding kitten. 
            b. If no defuse, the player is taken out. Check if the remaining player is a winner
        2. If exploding kitten is not drawn, add drawn card to player deck, update available actions
        3. Ask if the player would like to play any actions
            a. See hand
            b. Play an action (List out available actions + cancel)
                I. When an action is played, ask each other user if they'd like to nope it, even if they don't have a nope 
            c. End turn

    Finish:


    Reinforcment Model consideration:
    - Need a JSON import
        - # of players
        - Premade hands + Preshuffled deck (?)
    - Logs of steps and who won, etc
    """

    # Initialization step
    seed = int(input("Random seed: "))

    while True:
        n_players = int(input("How many players? "))

        if n_players < 2 or n_players > 5:
            print("Please enter a number between 2 and 5!")
        else:
            break
    

    
    # Initialize deck and deal initial hands
    random.seed(seed)
    deck: Deck = Deck()
    players: List[Hand] = [Hand(cards={}, alive=True) for i in range(n_players)]
    aliveCt = n_players

    for player in players:
        # Initial defuse + 7 cards
        player.add_card(CardEnum.DEFUSE)

        for j in range(7):
            player.add_card(deck.draw_card())
        
    # Add exploding kittens and spare defuses to finish initialization
    deck.add_defuse_and_kittens(n_players)

    # Turn based gameplay
    curPlayer = 0
    turnModifiers = { "isAttacking": False, "isAttacked": False, "skipTurn": False}
    while aliveCt > 1:
        # Check if current player is still in the game
        if not players[curPlayer].is_alive():
            curPlayer = (curPlayer + 1) % n_players
            continue

        print(f"Player {curPlayer + 1}'s turn:")

        turnModifiers["skipTurn"] = False
        if turnModifiers["isAttacking"]:
            print(f"Player {curPlayer + 1} -- You are being attacked!")
            turnModifiers["isAttacked"] = True
            turnModifiers["isAttacking"] = False

        while True:
            action = input(const.action_str).strip()
            
            match action:
                case "1":
                    print(f"Player {curPlayer + 1} -- Your hand:")
                    print(players[curPlayer].get_cards_str())

                case "2":
                    print(f"Player {curPlayer + 1} -- Here are your available actions:")
                    print(players[curPlayer].get_possible_actions_str())
                    print(f"Which action would you like to do?")
                    print("0. Exit")
                    print_all_user_actions()

                    # Loop through user selecting an action until action is completed
                    while True:
                        action_choice = input("Please enter the action number: ").strip()

                        if action_choice == "0":
                            break

                        try:
                            action_enum = ActionEnum(int(action_choice))

                            # Perform action if available
                            if players[curPlayer].get_possible_actions()[action_enum]:
                                print(f"Player {curPlayer + 1} is performing a {action_names[action_enum]}!")

                                # Ask each player if they would like to nope
                                nope_active = False
                                for i in range(len(players)):
                                    if players[i].is_alive() and players[i].can_nope():
                                        while True:
                                            nope = input(f"Player {i + 1} -- Would you like to nope? (Y/N)").strip().lower()
                                            match nope:
                                                case "y":
                                                    print(f"Player {i + 1} used a nope!")
                                                    nope_active = not nope_active

                                                    # Reset player asking to the start
                                                    i = 0
                                                    break
                                                case "n":
                                                    break
                                                case _:
                                                    print(f"Player {i + 1} -- Please input Y or N!")

                                if nope_active:
                                    print(f"Player {curPlayer + 1} -- Your card was noped!")
                                else:
                                    players[curPlayer].play_action(action_enum)
                                    perform_action(action_enum, players, curPlayer, turnModifiers, deck)
                                break
                                
                            else:
                                raise ValueError("If statement")

                        except Exception as e:
                            print("Please enter a valid action number!")
                            print(f"Error: {e}")
                            continue

                case "3":
                    break

                case _:
                    print("Please input a valid action")
                    continue

            if turnModifiers["skipTurn"]:
                break

        # Check if user played a card that skipped their turn
        if turnModifiers["skipTurn"]:
            if turnModifiers["isAttacked"]:
                turnModifiers["isAttacked"] = False
                continue
            curPlayer = (curPlayer + 1) % n_players
            continue
        
        # Draw a card
        print("Drawing top card...")
        top_card = deck.draw_card()

        # Check if exploding kitten
        if top_card == CardEnum.EXPLODING_KITTEN:
            print("Exploding Kitten drawn!")

            # Check if player can defuse
            if players[curPlayer].can_defuse():
                print("You used a defuse card to defuse the exploding kitten!")
                players[curPlayer].remove_card(CardEnum.DEFUSE)

                # Place defused exploding kitten
                pos = int(input(f"Place Exploding Kitten (1 = top, {deck.get_deck_size()+1} = bottom): "))
                while pos < 1 and pos > (deck.get_deck_size() + 1):
                    pos = int(input(f"Invalid input. Please try again (1 = top, {deck.get_deck_size() + 1} = bottom): "))
                    deck.insert_card(CardEnum.EXPLODING_KITTEN, pos)

                # Go to the next turn
                if turnModifiers["isAttacked"]:
                    turnModifiers["isAttacked"] = False
                    continue
                curPlayer = (curPlayer + 1) % n_players
                continue

            # If player can't defuse, take player out and go to the next player
            else:
                players[curPlayer].set_alive(False)
                aliveCt -= 1
                curPlayer = (curPlayer + 1) % n_players
                continue

        
        # If regular card drawn, add to player deck
        print(f"Player {curPlayer + 1} -- You drew a {card_names[top_card]}!")
        players[curPlayer].add_card(top_card)

        # Move to next player if not attacked
        if turnModifiers["isAttacked"]:
            turnModifiers["isAttacked"] = False
            continue
        curPlayer = (curPlayer + 1) % n_players


main()
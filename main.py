import random
from .utils.deck import Deck
from .utils.hand import Hand
from .utils.card import CardEnum
from .utils.actions import ActionEnum, print_all_user_actions, perform_action
from .utils.util import clear_screen
from typing import List


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
    n_players = int(input("How many players? "))
    seed = int(input("Random seed: "))

    
    # Initialize deck and deal initial hands
    random.seed(seed)
    deck: Deck = Deck()
    players: List[Hand] = [Hand()] * n_players
    aliveCt = n_players

    for i in range(n_players):
        # Initial defuse + 7 cards
        players[i].add_card(CardEnum.DEFUSE)

        for j in range(7):
            players[i].add_card(deck.draw_card())
        
    # Add exploding kittens and spare defuses to finish initialization
    deck.add_defuse_and_kittens(n_players)

    # Turn based gameplay
    curPlayer = 0
    isAttacked = False
    while aliveCt > 1:
        # Check if current player is still in the game
        if not players[curPlayer].is_alive():
            curPlayer = (curPlayer + 1) % n_players
            continue

        print(f"Player {curPlayer + 1}'s turn:")

        skipTurn = False
        while True:
            action = input("""What would you like to do?
                           1. See your hand
                           2. Play a card
                           3. End turn
                           """).strip()
            

            match action:
                case "1":
                    print(players[curPlayer].get_cards_str())

                case "2":
                    print("Here are your available actions:")
                    print(players[curPlayer].get_possible_actions_str())
                    print("Which action would you like to do?")
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
                                players[curPlayer].play_action(action_enum)
                                perform_action(action_enum, players, curPlayer, skipTurn, isAttacked, deck)

                                # Check if action ends turn
                                if skipTurn:
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

            break

        # Check if user played a card that skipped their turn
        if skipTurn:
            if isAttacked:
                isAttacked = False
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

                # Go to the next player
                if isAttacked:
                    isAttacked = False
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
        players[curPlayer].add_card(top_card)

        # Move to next player if not attacked
        if isAttacked:
            isAttacked = False
            continue
        curPlayer = (curPlayer + 1) % n_players


main()
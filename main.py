import random
from .utils.deck import Deck
from .utils.hand import Hand
from .utils.card import CardEnum
from .utils.actions import ActionEnum
from .utils.cli_util import clear_screen
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
    while aliveCt > 1:
        # Check if current player is still in the game
        if players[curPlayer] is None:
            curPlayer = (curPlayer + 1) % n_players
            continue

        print(f"Player {curPlayer + 1}'s turn:")

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
                    pos = int(input(f"Invalid input. Please try again (1 = top, {deck.get_deck_size()+1} = bottom): "))

                


                # Go to next player





        # Loop through available user actions

        # Move to next player
        curPlayer = (curPlayer + 1) % n_players

    

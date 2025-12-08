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
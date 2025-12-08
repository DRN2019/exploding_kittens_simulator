from .card import CardEnum
import random

class Deck:
    def __init__(self, n_players):
        defuse_ct = 1 if n_players == 5 else 2

        # Construct deck by count of cards
        self.n_players = n_players
        self.deck = {
            CardEnum.DEFUSE: defuse_ct,
            CardEnum.EXPLODING_KITTEN: n_players - 1,
            CardEnum.NOPE: 5,
            CardEnum.ATTACK: 4,
            CardEnum.FAVOR: 4,
            CardEnum.SHUFFLE: 4,
            CardEnum.SKIP: 4,
            CardEnum.SEE_THE_FUTURE: 5,
            CardEnum.BEARD: 4,
            CardEnum.CATERMELON: 4,
            CardEnum.POTATO: 4,
            CardEnum.RAINBOW: 4,
            CardEnum.TACO: 4,
        }

        self.draw_pile = self.build_deck()


    def build_deck(self):
        # Turn dictionary into a list of cards for ordering
        deck_list = []
        for card, count in self.deck.items():
            deck_list.extend([card] * count)

        random.shuffle(deck_list)
        return deck_list

    def shuffle(self):
        random.shuffle(self.draw_pile)

    def draw_card(self):
        if len(self.draw_pile) == 0:
            return None

        card = self.draw_pile.pop(0)
        self.deck[card] -= 1

    def see_top_3(self):
        return self.draw_pile[:3]

    def insert_card(self, card: CardEnum, index: int = 0):
        self.deck[card] += 1
        self.draw_pile.insert(index, card)

        

    
    
 


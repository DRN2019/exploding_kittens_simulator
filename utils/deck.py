from .card import CardEnum
import random
from typing import List

class Deck:
    def __init__(self, seed=123):
        # Construct deck by count of cards
        self.deck = {
            CardEnum.DEFUSE: 0,
            CardEnum.EXPLODING_KITTEN: 0,
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


    def build_deck(self) -> List[CardEnum]:
        # Turn dictionary into a list of cards for ordering
        deck_list = []
        for card, count in self.deck.items():
            deck_list.extend([card] * count)

        self.shuffle()

        return deck_list
    
    def add_defuse_and_kittens(self, n_players):
        defuseCt = 1 if n_players == 5 else 2
        expKittenCt = n_players - 1

        for i in range(defuseCt):
            self.insert_card(CardEnum.DEFUSE)
        
        for i in range(expKittenCt):
            self.insert_card(CardEnum.EXPLODING_KITTEN)

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.draw_pile)

    def draw_card(self) -> CardEnum:
        card = self.draw_pile.pop(0)
        self.deck[card] -= 1

        return card

    def see_top_3(self) -> List[CardEnum]:
        return self.draw_pile[:3]

    def insert_card(self, card: CardEnum, index: int = 0):
        self.deck[card] += 1
        self.draw_pile.insert(index, card)

    def get_deck_size(self):
        return len(self.draw_pile)
        

    
    
 


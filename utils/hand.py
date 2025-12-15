from .card import CardEnum
from .actions import ActionEnum
from .error import InsufficientCardsError

class Hand:

    def __init__(self, cards):
        """
        Args:
            cards (dict): Dictionary of initial cards
        """
        self.cards = cards

    def get_cards(self):
        """

        Returns:
            dict: Dictionary of cards in hand
        """
        return self.cards
    
    def get_cards_str(self):
        """
        Returns player's cards in a user-friendly string
        Returns:
            dict: Dictionary of cards in hand
        """
        cards = ""
        for cardType, quantity in self.cards:

            match cardType:
                case CardEnum.DEFUSE:
                    cards += f"Defuse: {quantity}"
               
                case CardEnum.NOPE:
                    cards += f"Nope: {quantity}"

                case CardEnum.ATTACK:
                    cards += f"Attack: {quantity}"

                case CardEnum.FAVOR:
                    cards += f"Favor: {quantity}"

                case CardEnum.SHUFFLE:
                    cards += f"Shuffle: {quantity}"

                case CardEnum.SKIP:
                    cards += f"Skip: {quantity}"

                case CardEnum.SEE_THE_FUTURE:
                    cards += f"See the Future: {quantity}"

                case CardEnum.BEARD:
                    cards += f"Beard Cat: {quantity}"

                case CardEnum.CATERMELON:
                    cards += f"Catermelon: {quantity}"

                case CardEnum.POTATO:                    
                    cards += f"Hairy Potato Cat: {quantity}"

                case CardEnum.RAINBOW:                    
                    cards += f"Rainbow Ralphing Cat: {quantity}"

                case CardEnum.TACO:                    
                    cards += f"Tacocat: {quantity}"

                case _:
                    pass

            string += "\n"



    def add_card(self, card: CardEnum, quantity: int = 1):
        """
        Adds a card to the player's hand

        Args:
            card (CardEnum): Enum of card type to be added
            quantity (int): Quantity of card to be added

        Returns:
            None
        """
        if not self.cards[card]:
            self.cards[card] = quantity
        else:
            self.cards[card] += quantity

    def remove_card(self, card: CardEnum, quantity: int = 1):
        """
        Removes a card from the player's hand

        Args:
            card (CardEnum): Enum of card type to be removed
            quantity (int): Quantity of card to be removed

        Returns:
            None
        """

        if not self.cards[card] or self.cards[card] < quantity:
            raise InsufficientCardsError(f"Not enough cards of type {card}")
        
        self.cards[card] -= quantity

        return None


    def get_possible_actions(self):
        possible_actions = {}

        for cardType in CardEnum:
            # Check for card specific actions
            count = self.cards[cardType]

            match cardType:
                case CardEnum.DEFUSE:
                    possible_actions[ActionEnum.DEFUSE] = count
               
                case CardEnum.NOPE:
                    possible_actions[ActionEnum.NOPE] = count

                case CardEnum.ATTACK:
                    possible_actions[ActionEnum.ATTACK] = count

                case CardEnum.FAVOR:
                    possible_actions[ActionEnum.FAVOR] = count

                case CardEnum.SHUFFLE:
                    possible_actions[ActionEnum.SHUFFLE] = count

                case CardEnum.SKIP:
                    possible_actions[ActionEnum.SKIP] = count

                case CardEnum.SEE_THE_FUTURE:
                    possible_actions[ActionEnum.SEE_THE_FUTURE] = count

                case CardEnum.BEARD:
                    if possible_actions[ActionEnum.TWO_CAT]:
                        possible_actions[ActionEnum.TWO_CAT] += count // 2
                    else:
                        possible_actions[ActionEnum.TWO_CAT] = count // 2

                case CardEnum.CATERMELON:
                    if possible_actions[ActionEnum.TWO_CAT]:
                        possible_actions[ActionEnum.TWO_CAT] += count // 2
                    else:
                        possible_actions[ActionEnum.TWO_CAT] = count // 2

                case CardEnum.POTATO:                    
                    if possible_actions[ActionEnum.TWO_CAT]:
                        possible_actions[ActionEnum.TWO_CAT] += count // 2
                    else:
                        possible_actions[ActionEnum.TWO_CAT] = count // 2

                case CardEnum.RAINBOW:                    
                    if possible_actions[ActionEnum.TWO_CAT]:
                        possible_actions[ActionEnum.TWO_CAT] += count // 2
                    else:
                        possible_actions[ActionEnum.TWO_CAT] = count // 2

                case CardEnum.TACO:                    
                    if possible_actions[ActionEnum.TWO_CAT]:
                        possible_actions[ActionEnum.TWO_CAT] += count // 2
                    else:
                        possible_actions[ActionEnum.TWO_CAT] = count // 2

                case _:
                    pass

    def can_nope(self):
        return self.cards[CardEnum.NOPE] > 0

    def can_defuse(self):
        return self.cards[CardEnum.DEFUSE] > 0
            


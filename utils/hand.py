from .card import CardEnum
from .actions import ActionEnum

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


    def add_card(self, card: CardEnum, quantity: int):
        """
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
                    if count >= 2:
                        if possible_actions[ActionEnum.TWO_CAT]:
                            possible_actions[ActionEnum.TWO_CAT] += count
                        else:
                            possible_actions[ActionEnum.TWO_CAT] = count

                case CardEnum.CATERMELON:
                    if count >= 2:
                        if possible_actions[ActionEnum.TWO_CAT]:
                            possible_actions[ActionEnum.TWO_CAT] += count
                        else:
                            possible_actions[ActionEnum.TWO_CAT] = count

                case CardEnum.POTATO:
                    if count >= 2:
                        if possible_actions[ActionEnum.TWO_CAT]:
                            possible_actions[ActionEnum.TWO_CAT] += count
                        else:
                            possible_actions[ActionEnum.TWO_CAT] = count

                case CardEnum.RAINBOW:
                    if count >= 2:
                        if possible_actions[ActionEnum.TWO_CAT]:
                            possible_actions[ActionEnum.TWO_CAT] += count
                        else:
                            possible_actions[ActionEnum.TWO_CAT] = count

                case CardEnum.TACO:
                    if count >= 2:
                        if possible_actions[ActionEnum.TWO_CAT]:
                            possible_actions[ActionEnum.TWO_CAT] += count
                        else:
                            possible_actions[ActionEnum.TWO_CAT] = count

                case _:
                    pass



            

    def can_nope(self):
        return self.cards[CardEnum.NOPE] > 0
            


from .card import CardEnum, card_names
from .actions import ActionEnum, action_names, card_action_mapping
from .error import InsufficientCardsError

class Hand:

    def __init__(self, cards = {}, alive = True):
        """
        Args:
            cards (dict): Dictionary of initial cards
        """
        self.cards: dict[CardEnum, int] = cards
        self.alive: bool = alive

    def get_cards(self) -> dict[CardEnum, int]:
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
        cards_str = ""
        for cardType, quantity in self.cards.items():
            cards_str += f"{card_names[cardType]}: {quantity}\n"

        return cards_str
    
    def get_n_cards(self) -> int:
        """
        Returns number of cards left in player's hand

        Returns:
            int: Number of cards in hand
        """

        return sum(self.cards.values())


    def add_card(self, card: CardEnum, quantity: int = 1):
        """
        Adds a card to the player's hand

        Args:
            card (CardEnum): Enum of card type to be added
            quantity (int): Quantity of card to be added

        Returns:
            None
        """
        if card in self.cards:
            self.cards[card] += quantity
        else:
            self.cards[card] = quantity

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
    
    def is_alive(self):
        """
        Checks if player is still alive

        Returns:
            bool: True if player is still alive, False otherwise
        """
        return self.alive
    
    def set_alive(self, alive: bool):
        """
        Sets the player's alive state

        Args:
            alive (bool): True if player is alive, False otherwise
        """
        self.alive = alive


    def get_possible_actions(self) -> dict[ActionEnum, int]:
        """
        Gets the list of possible actions the player can play and the number of times they can play that action

        Returns:
            dict[ActionEnum, int]: Dictionary with <Action, count> pairs
        """
        possible_actions: dict[ActionEnum, int] = {}

        for cardType in CardEnum:
            # Check for card specific actions
            count = 0
            if cardType in self.cards:   
                count = self.cards[cardType]

            match cardType:
                case CardEnum.ATTACK | CardEnum.FAVOR | CardEnum.SHUFFLE | CardEnum.SKIP | CardEnum.SEE_THE_FUTURE:
                    possible_actions[card_action_mapping[cardType]] = count

                case CardEnum.BEARD | CardEnum.CATERMELON | CardEnum.POTATO | CardEnum.RAINBOW | CardEnum.TACO:
                    if ActionEnum.TWO_CAT in possible_actions:
                        possible_actions[ActionEnum.TWO_CAT] += count // 2
                    else:
                        possible_actions[ActionEnum.TWO_CAT] = count // 2

                case _:
                    pass
        
        return possible_actions

    def get_possible_actions_str(self) -> str:
        """
        Returns the a stringified list of possible actions the player can perform

        Returns:
            str: String of all available actions player has
        """
        actions = self.get_possible_actions()
        
        action_str = ""

        for actionType, count in actions.items():
            action_str += f"{action_names[actionType]}: {count}\n"

        return action_str

    def play_action(self, action: ActionEnum) -> None:
        """
        Removes the corresponding cards from a player's hand after playing an action

        Args:
            action (ActionEnum): Action to be performed

        Raises:
            ValueError: Raised if insufficient cards to perform action
        """

        # Sanity check for valid action
        if not action in self.get_possible_actions():
            raise ValueError("Invalid action number!")
        
        # Check if player steals a card, only case where multiple cards are removed from hand from 1 action
        if action == ActionEnum.TWO_CAT:
            cat_cards = [CardEnum.BEARD, CardEnum.CATERMELON, CardEnum.POTATO, CardEnum.RAINBOW, CardEnum.TACO]

            # Simply use the first pair of cat cards found
            for card in cat_cards:
                if self.cards[card] >= 2:
                    self.cards[card] -= 2
                    return

        else:
            # Find the corresponding card type to the action
            for cardType, actionType in card_action_mapping.items():
                if action == actionType:
                    self.cards[cardType] -= 1
                    return


    def can_nope(self) -> bool:
        """
        Checks if the player can nope

        Returns:
            bool: True if player has at least one Nope card, False otherwise
        """
        return self.cards[CardEnum.NOPE] > 0

    def can_defuse(self) -> bool:
        """
        Checks if the player can defuse

        Returns:
            bool: True if player has at least one Defuse card, False otherwise
        """
        return self.cards[CardEnum.DEFUSE] > 0
            


class InsufficientCardsError(Exception):
    """Exception raised for insufficient cards in a hand"""
    pass

class InvalidPositionError(Exception):
    """Exception for invalid position in card deck"""
    pass
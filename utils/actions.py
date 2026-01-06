from enum import Enum
from .card import CardEnum, card_names

class ActionEnum(Enum):
    ATTACK = 1
    TWO_CAT = 2
    FAVOR = 3
    SEE_THE_FUTURE = 4
    SHUFFLE = 5
    SKIP = 6

action_names = {
    ActionEnum.ATTACK: "Attack",
    ActionEnum.TWO_CAT: "Steal a Card (Cat card pair)",
    ActionEnum.FAVOR: "Favor",
    ActionEnum.SEE_THE_FUTURE: "See the Future",
    ActionEnum.SHUFFLE: "Shuffle",
    ActionEnum.SKIP: "Skip",
}

card_action_mapping = {
    CardEnum.ATTACK: ActionEnum.ATTACK,
    CardEnum.FAVOR: ActionEnum.FAVOR,
    CardEnum.SHUFFLE: ActionEnum.SHUFFLE,
    CardEnum.SKIP: ActionEnum.SKIP,
    CardEnum.SEE_THE_FUTURE: ActionEnum.SEE_THE_FUTURE,
    CardEnum.BEARD: ActionEnum.TWO_CAT,
    CardEnum.CATERMELON: ActionEnum.TWO_CAT,
    CardEnum.POTATO: ActionEnum.TWO_CAT,
    CardEnum.RAINBOW: ActionEnum.TWO_CAT,
    CardEnum.TACO: ActionEnum.TWO_CAT,
}

def print_all_user_actions():
    """
    Prints all actions
    """
    actions_str = ""
    for key, value in action_names.items():
        # TODO: Filter out Defuse and Nope as available actions, and corresponding choice value

        actions_str += f"{key.value}. {value}\n"

    print(actions_str)

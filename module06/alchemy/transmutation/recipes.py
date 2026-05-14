from elements import create_fire

from alchemy.potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and '{strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )

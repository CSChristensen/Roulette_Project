from enum import Enum
from random import randint
from typing import Tuple


class Color(Enum):
    RED = "red"
    BLACK = "black"
    GREEN = "green"


WHEEL_POSITIONS = {
    0: Color.GREEN,
    1: Color.RED,
    2: Color.BLACK,
    3: Color.RED,
    4: Color.BLACK,
    5: Color.RED,
    6: Color.BLACK,
    7: Color.RED,
    8: Color.BLACK,
    9: Color.RED,
    10: Color.BLACK,
    11: Color.BLACK,
    12: Color.RED,
    13: Color.BLACK,
    14: Color.RED,
    15: Color.BLACK,
    16: Color.RED,
    17: Color.BLACK,
    18: Color.RED,
    19: Color.RED,
    20: Color.BLACK,
    21: Color.RED,
    22: Color.BLACK,
    23: Color.RED,
    24: Color.BLACK,
    25: Color.RED,
    26: Color.BLACK,
    27: Color.RED,
    28: Color.BLACK,
    29: Color.BLACK,
    30: Color.RED,
    31: Color.BLACK,
    32: Color.RED,
    33: Color.BLACK,
    34: Color.RED,
    35: Color.BLACK,
    36: Color.RED,
}


class Wheel:
    """A class to represent a wheel in a roulette game."""

    def __init__(self):
        self._ball_postion = None

    def spin(self):
        self._ball_postion = randint(0, 36)

    def get_ball_position(self) -> Tuple[int, Color]:
        return (self._ball_postion, WHEEL_POSITIONS[self._ball_postion])

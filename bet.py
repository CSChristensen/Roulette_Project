from wheel import Color
from player import Player


class Bet:

    def __init__(self, amount: int, color: Color, player: Player):
        self.amount = amount
        self.color = color
        self.player = player

    def payout(self, color: Color) -> None:
        if self.color == color:
            odds = 35 if color == Color.GREEN else 2
            self.player.add_to_balance(self.amount * odds)

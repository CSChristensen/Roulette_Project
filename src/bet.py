from .wheel import Color
from .player import Player


class Bet:

    def __init__(self, amount: int, color: Color, player: Player):
        self.amount = amount
        self.color = color
        self.player = player

    def payout(self, color: Color) -> None:
        if self.color == color:
            odds = 35 if color == Color.GREEN else 2
            winnings = self.amount * odds
            self.player.add_to_balance(winnings)
        # If bet loses, no payout is made (amount was already deducted when bet was placed)

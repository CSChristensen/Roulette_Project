from enum import Enum
from typing import Union
from .wheel import Color
from .player import Player


class BetType(Enum):
    COLOR = "color"
    NUMBER = "number"


class Bet:

    def __init__(self, amount: int, player: Player, bet_type: BetType = None, bet_value: Union[Color, int] = None, color: Color = None):
        self.amount = amount
        self.player = player
        
        # Handle backward compatibility - if color is provided, use color betting
        if color is not None:
            self.bet_type = BetType.COLOR
            self.bet_value = color
            self.color = color  # Keep for backward compatibility
        else:
            self.bet_type = bet_type
            self.bet_value = bet_value
            # Set color attribute for backward compatibility when it's a color bet
            if bet_type == BetType.COLOR:
                self.color = bet_value

    def payout(self, winning_color: Color, winning_position: int = None) -> None:
        # Handle backward compatibility - if only color is provided
        if winning_position is None:
            # Old method signature - assume color betting
            if hasattr(self, 'color') and self.color == winning_color:
                odds = 35 if winning_color == Color.GREEN else 2
                winnings = self.amount * odds
                self.player.add_to_balance(winnings)
            return
        
        # New method with both winning_color and winning_position
        won = False
        odds = 0
        
        if self.bet_type == BetType.COLOR:
            # Color bet logic
            if self.bet_value == winning_color:
                won = True
                odds = 35 if winning_color == Color.GREEN else 2
        elif self.bet_type == BetType.NUMBER:
            # Number bet logic - exact position match
            if self.bet_value == winning_position:
                won = True
                odds = 35  # 35:1 for number bets
        
        if won:
            winnings = self.amount * odds
            self.player.add_to_balance(winnings)
        # If bet loses, no payout is made (amount was already deducted when bet was placed)

#!/usr/bin/env python3
"""
Integration tests for mixed betting scenarios.
Tests multiple bets of different types, balance updates, and game flow.
"""

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False

from src.bet import Bet, BetType
from src.wheel import Color, Wheel
from src.player import Player
from src.table import Table
from src.game_controller import GameController


class TestMixedBettingIntegration:
    """Integration test class for mixed betting scenarios."""

    def setup_method(self):
        """Setup method to provide fresh instances for each test."""
        self.player = Player(1000)  # Player with $1000 balance
        self.table = Table()
        self.controller = GameController()
        self.controller.player = self.player
        self.controller.table = self.table

    def test_single_color_bet_integration(self):
        """Test single color bet placement and payout integration."""
        initial_balance = self.player.get_balance()
        bet_amount = 50
        
        # Deduct bet amount and place bet
        self.player.subtract_from_balance(bet_amount)
        bet = Bet(bet_amount, self.player, BetType.COLOR, Color.RED)
        self.table.place_bet(bet)
        
        # Verify bet is placed
        assert len(self.table.bets) == 1
        assert self.player.get_balance() == initial_balance - bet_amount
        
        # Mock a winning spin (red wins)
        self.table.wheel._ball_position = 1  # Position 1 is red
        self.table._payout_bets()
        
        # Verify payout (2:1 odds for red)
        expected_winnings = bet_amount * 2
        expected_balance = initial_balance - bet_amount + expected_winnings
        assert self.player.get_balance() == expected_balance
        assert len(self.table.bets) == 0  # Bets cleared after payout

    def test_single_number_bet_integration(self):
        """Test single number bet placement and payout integration."""
        initial_balance = self.player.get_balance()
        bet_amount = 25
        bet_number = 17
        
        # Deduct bet amount and place bet
        self.player.subtract_from_balance(bet_amount)
        bet = Bet(bet_amount, self.player, BetType.NUMBER, bet_number)
        self.table.place_bet(bet)
        
        # Verify bet is placed
        assert len(self.table.bets) == 1
        assert self.player.get_balance() == initial_balance - bet_amount
        
        # Mock a winning spin (number 17 wins)
        self.table.wheel._ball_position = bet_number
        self.table._payout_bets()
        
        # Verify payout (35:1 odds for numbers)
        expected_winnings = bet_amount * 35
        expected_balance = initial_balance - bet_amount + expected_winnings
        assert self.player.get_balance() == expected_balance
        assert len(self.table.bets) == 0

    def test_mixed_bets_both_win(self):
        """Test mixed color and number bets where both win."""
        initial_balance = self.player.get_balance()
        color_bet_amount = 30
        number_bet_amount = 10
        bet_number = 1  # Position 1 is red
        
        # Place color bet on red
        self.player.subtract_from_balance(color_bet_amount)
        color_bet = Bet(color_bet_amount, self.player, BetType.COLOR, Color.RED)
        self.table.place_bet(color_bet)
        
        # Place number bet on 1
        self.player.subtract_from_balance(number_bet_amount)
        number_bet = Bet(number_bet_amount, self.player, BetType.NUMBER, bet_number)
        self.table.place_bet(number_bet)
        
        # Verify both bets are placed
        assert len(self.table.bets) == 2
        total_bet = color_bet_amount + number_bet_amount
        assert self.player.get_balance() == initial_balance - total_bet
        
        # Mock winning spin (position 1, which is red)
        self.table.wheel._ball_position = 1
        self.table._payout_bets()
        
        # Calculate expected winnings
        color_winnings = color_bet_amount * 2  # 2:1 for red
        number_winnings = number_bet_amount * 35  # 35:1 for number
        total_winnings = color_winnings + number_winnings
        expected_balance = initial_balance - total_bet + total_winnings
        
        assert self.player.get_balance() == expected_balance
        assert len(self.table.bets) == 0

    def test_mixed_bets_color_wins_number_loses(self):
        """Test mixed bets where color bet wins but number bet loses."""
        initial_balance = self.player.get_balance()
        color_bet_amount = 40
        number_bet_amount = 15
        
        # Place color bet on red
        self.player.subtract_from_balance(color_bet_amount)
        color_bet = Bet(color_bet_amount, self.player, BetType.COLOR, Color.RED)
        self.table.place_bet(color_bet)
        
        # Place number bet on 17
        self.player.subtract_from_balance(number_bet_amount)
        number_bet = Bet(number_bet_amount, self.player, BetType.NUMBER, 17)
        self.table.place_bet(number_bet)
        
        # Mock winning spin (position 3, which is red, but not 17)
        self.table.wheel._ball_position = 3  # Red position, but not 17
        self.table._payout_bets()
        
        # Only color bet wins
        color_winnings = color_bet_amount * 2
        total_bet = color_bet_amount + number_bet_amount
        expected_balance = initial_balance - total_bet + color_winnings
        
        assert self.player.get_balance() == expected_balance

    def test_mixed_bets_number_wins_color_loses(self):
        """Test mixed bets where number bet wins but color bet loses."""
        initial_balance = self.player.get_balance()
        color_bet_amount = 20
        number_bet_amount = 5
        
        # Place color bet on red
        self.player.subtract_from_balance(color_bet_amount)
        color_bet = Bet(color_bet_amount, self.player, BetType.COLOR, Color.RED)
        self.table.place_bet(color_bet)
        
        # Place number bet on 2 (which is black)
        self.player.subtract_from_balance(number_bet_amount)
        number_bet = Bet(number_bet_amount, self.player, BetType.NUMBER, 2)
        self.table.place_bet(number_bet)
        
        # Mock winning spin (position 2, which is black)
        self.table.wheel._ball_position = 2
        self.table._payout_bets()
        
        # Only number bet wins
        number_winnings = number_bet_amount * 35
        total_bet = color_bet_amount + number_bet_amount
        expected_balance = initial_balance - total_bet + number_winnings
        
        assert self.player.get_balance() == expected_balance

    def test_mixed_bets_both_lose(self):
        """Test mixed bets where both bets lose."""
        initial_balance = self.player.get_balance()
        color_bet_amount = 35
        number_bet_amount = 12
        
        # Place color bet on red
        self.player.subtract_from_balance(color_bet_amount)
        color_bet = Bet(color_bet_amount, self.player, BetType.COLOR, Color.RED)
        self.table.place_bet(color_bet)
        
        # Place number bet on 17
        self.player.subtract_from_balance(number_bet_amount)
        number_bet = Bet(number_bet_amount, self.player, BetType.NUMBER, 17)
        self.table.place_bet(number_bet)
        
        # Mock losing spin (position 4, which is black, and not 17)
        self.table.wheel._ball_position = 4  # Black position, not 17
        self.table._payout_bets()
        
        # Both bets lose, no winnings
        total_bet = color_bet_amount + number_bet_amount
        expected_balance = initial_balance - total_bet
        
        assert self.player.get_balance() == expected_balance

    def test_multiple_same_type_bets(self):
        """Test multiple bets of the same type."""
        initial_balance = self.player.get_balance()
        
        # Place multiple number bets
        bet_amounts = [10, 15, 20]
        bet_numbers = [5, 17, 23]
        
        for amount, number in zip(bet_amounts, bet_numbers):
            self.player.subtract_from_balance(amount)
            bet = Bet(amount, self.player, BetType.NUMBER, number)
            self.table.place_bet(bet)
        
        assert len(self.table.bets) == 3
        total_bet = sum(bet_amounts)
        assert self.player.get_balance() == initial_balance - total_bet
        
        # Mock winning spin (position 17 wins)
        self.table.wheel._ball_position = 17
        self.table._payout_bets()
        
        # Only the bet on 17 wins (15 * 35 = 525)
        winning_amount = 15 * 35
        expected_balance = initial_balance - total_bet + winning_amount
        
        assert self.player.get_balance() == expected_balance

    def test_multiple_color_bets_different_colors(self):
        """Test multiple color bets on different colors."""
        initial_balance = self.player.get_balance()
        
        # Place bets on different colors
        red_amount = 25
        black_amount = 30
        green_amount = 10
        
        self.player.subtract_from_balance(red_amount)
        red_bet = Bet(red_amount, self.player, BetType.COLOR, Color.RED)
        self.table.place_bet(red_bet)
        
        self.player.subtract_from_balance(black_amount)
        black_bet = Bet(black_amount, self.player, BetType.COLOR, Color.BLACK)
        self.table.place_bet(black_bet)
        
        self.player.subtract_from_balance(green_amount)
        green_bet = Bet(green_amount, self.player, BetType.COLOR, Color.GREEN)
        self.table.place_bet(green_bet)
        
        assert len(self.table.bets) == 3
        total_bet = red_amount + black_amount + green_amount
        
        # Mock green winning (position 0)
        self.table.wheel._ball_position = 0
        self.table._payout_bets()
        
        # Only green bet wins (35:1 odds)
        green_winnings = green_amount * 35
        expected_balance = initial_balance - total_bet + green_winnings
        
        assert self.player.get_balance() == expected_balance

    def test_complex_mixed_betting_scenario(self):
        """Test complex scenario with multiple mixed bets."""
        initial_balance = self.player.get_balance()
        
        # Place various bets
        bets_data = [
            (BetType.COLOR, Color.RED, 50),
            (BetType.NUMBER, 17, 20),
            (BetType.COLOR, Color.BLACK, 30),
            (BetType.NUMBER, 0, 10),
            (BetType.COLOR, Color.GREEN, 15),
            (BetType.NUMBER, 23, 25),
        ]
        
        total_bet = 0
        for bet_type, bet_value, amount in bets_data:
            self.player.subtract_from_balance(amount)
            bet = Bet(amount, self.player, bet_type, bet_value)
            self.table.place_bet(bet)
            total_bet += amount
        
        assert len(self.table.bets) == 6
        assert self.player.get_balance() == initial_balance - total_bet
        
        # Mock winning spin (position 17, which is black)
        self.table.wheel._ball_position = 17
        self.table._payout_bets()
        
        # Calculate expected winnings:
        # - Color bet on BLACK wins: 30 * 2 = 60
        # - Number bet on 17 wins: 20 * 35 = 700
        # - All other bets lose
        expected_winnings = (30 * 2) + (20 * 35)  # 60 + 700 = 760
        expected_balance = initial_balance - total_bet + expected_winnings
        
        assert self.player.get_balance() == expected_balance

    def test_balance_insufficient_for_multiple_bets(self):
        """Test behavior when balance becomes insufficient during multiple bet placement."""
        # Start with limited balance
        limited_player = Player(100)
        
        # Place first bet
        limited_player.subtract_from_balance(60)
        bet1 = Bet(60, limited_player, BetType.COLOR, Color.RED)
        self.table.place_bet(bet1)
        
        # Place second bet
        limited_player.subtract_from_balance(40)
        bet2 = Bet(40, limited_player, BetType.NUMBER, 17)
        self.table.place_bet(bet2)
        
        # Player should now have $0
        assert limited_player.get_balance() == 0
        assert len(self.table.bets) == 2
        
        # Try to place another bet (should raise ValueError)
        with pytest.raises(ValueError, match="Insufficient balance") if PYTEST_AVAILABLE else self._expect_value_error():
            limited_player.subtract_from_balance(10)

    def _expect_value_error(self):
        """Helper method for non-pytest environments to test ValueError."""
        class ExpectValueError:
            def __enter__(self):
                return self
            def __exit__(self, exc_type, exc_val, exc_tb):
                return exc_type is ValueError
        return ExpectValueError()

    def test_zero_balance_after_losing_all_bets(self):
        """Test scenario where player loses all money."""
        # Start with small balance
        small_player = Player(50)
        
        # Bet everything
        small_player.subtract_from_balance(50)
        bet = Bet(50, small_player, BetType.NUMBER, 17)
        self.table.place_bet(bet)
        
        assert small_player.get_balance() == 0
        
        # Mock losing spin
        self.table.wheel._ball_position = 23  # Not 17
        self.table._payout_bets()
        
        # Player should still have $0
        assert small_player.get_balance() == 0

    def test_large_winnings_balance_update(self):
        """Test that large winnings are handled correctly."""
        initial_balance = self.player.get_balance()
        large_bet = 100
        
        # Place large number bet
        self.player.subtract_from_balance(large_bet)
        bet = Bet(large_bet, self.player, BetType.NUMBER, 7)
        self.table.place_bet(bet)
        
        # Mock winning spin
        self.table.wheel._ball_position = 7
        self.table._payout_bets()
        
        # Large winnings: 100 * 35 = 3500
        expected_winnings = large_bet * 35
        expected_balance = initial_balance - large_bet + expected_winnings
        
        assert self.player.get_balance() == expected_balance

    def test_bet_clearing_after_payout(self):
        """Test that bets are properly cleared after payout."""
        # Place multiple bets
        for i in range(5):
            self.player.subtract_from_balance(10)
            bet = Bet(10, self.player, BetType.NUMBER, i)
            self.table.place_bet(bet)
        
        assert len(self.table.bets) == 5
        
        # Process payout
        self.table.wheel._ball_position = 10  # None of the bets win
        self.table._payout_bets()
        
        # All bets should be cleared
        assert len(self.table.bets) == 0

    def test_mixed_betting_with_backward_compatibility(self):
        """Test that new betting works alongside old-style bets."""
        initial_balance = self.player.get_balance()
        
        # Place old-style color bet
        self.player.subtract_from_balance(30)
        old_bet = Bet(30, self.player, color=Color.RED)  # Old format
        self.table.place_bet(old_bet)
        
        # Place new-style number bet
        self.player.subtract_from_balance(20)
        new_bet = Bet(20, self.player, BetType.NUMBER, 1)  # New format
        self.table.place_bet(new_bet)
        
        assert len(self.table.bets) == 2
        
        # Mock winning spin (position 1, which is red)
        self.table.wheel._ball_position = 1
        self.table._payout_bets()
        
        # Both bets should win
        old_bet_winnings = 30 * 2  # Color bet
        new_bet_winnings = 20 * 35  # Number bet
        total_winnings = old_bet_winnings + new_bet_winnings
        expected_balance = initial_balance - 50 + total_winnings
        
        assert self.player.get_balance() == expected_balance


def run_standalone_tests():
    """Run tests without pytest for environments where it's not available."""
    print("Running mixed betting integration tests...")

    test_instance = TestMixedBettingIntegration()
    test_methods = [
        "test_single_color_bet_integration",
        "test_single_number_bet_integration",
        "test_mixed_bets_both_win",
        "test_mixed_bets_color_wins_number_loses",
        "test_mixed_bets_number_wins_color_loses",
        "test_mixed_bets_both_lose",
        "test_multiple_same_type_bets",
        "test_multiple_color_bets_different_colors",
        "test_complex_mixed_betting_scenario",
        "test_balance_insufficient_for_multiple_bets",
        "test_zero_balance_after_losing_all_bets",
        "test_large_winnings_balance_update",
        "test_bet_clearing_after_payout",
        "test_mixed_betting_with_backward_compatibility",
    ]

    passed = 0
    failed = 0

    for method_name in test_methods:
        try:
            test_instance.setup_method()
            method = getattr(test_instance, method_name)
            method()
            print(f"✓ {method_name}")
            passed += 1
        except Exception as e:
            print(f"✗ {method_name}: {e}")
            failed += 1

    print(f"\nTest Results: {passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    if PYTEST_AVAILABLE:
        pytest.main([__file__, "-v"])
    else:
        success = run_standalone_tests()
        exit(0 if success else 1)
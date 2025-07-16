#!/usr/bin/env python3
"""
Unit tests for the enhanced Bet class supporting both color and number betting.
Tests BetType enum and Bet class functionality including payout calculations.
"""

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False

from src.bet import Bet, BetType
from src.wheel import Color
from src.player import Player


class TestBetType:
    """Test class for BetType enumeration."""

    def test_bet_type_enum_values(self):
        """Test that BetType enum has correct values."""
        assert BetType.COLOR.value == "color"
        assert BetType.NUMBER.value == "number"

    def test_bet_type_enum_comparison(self):
        """Test BetType enum comparison operations."""
        assert BetType.COLOR == BetType.COLOR
        assert BetType.NUMBER == BetType.NUMBER
        assert BetType.COLOR != BetType.NUMBER


class TestBetClass:
    """Test class for enhanced Bet class functionality."""

    def setup_method(self):
        """Setup method to provide test fixtures."""
        self.player = Player(1000)  # Player with $1000 balance

    def test_bet_creation_color_new_format(self):
        """Test creating color bets with new format (bet_type and bet_value)."""
        bet = Bet(50, self.player, BetType.COLOR, Color.RED)
        
        assert bet.amount == 50
        assert bet.player == self.player
        assert bet.bet_type == BetType.COLOR
        assert bet.bet_value == Color.RED
        assert bet.color == Color.RED  # Backward compatibility

    def test_bet_creation_number_new_format(self):
        """Test creating number bets with new format."""
        bet = Bet(25, self.player, BetType.NUMBER, 17)
        
        assert bet.amount == 25
        assert bet.player == self.player
        assert bet.bet_type == BetType.NUMBER
        assert bet.bet_value == 17
        assert not hasattr(bet, 'color') or bet.color is None

    def test_bet_creation_backward_compatibility(self):
        """Test creating bets with old format (color parameter) for backward compatibility."""
        bet = Bet(100, self.player, color=Color.BLACK)
        
        assert bet.amount == 100
        assert bet.player == self.player
        assert bet.bet_type == BetType.COLOR
        assert bet.bet_value == Color.BLACK
        assert bet.color == Color.BLACK

    def test_bet_creation_edge_cases(self):
        """Test bet creation with edge case numbers."""
        # Test betting on 0
        bet_zero = Bet(10, self.player, BetType.NUMBER, 0)
        assert bet_zero.bet_value == 0
        assert bet_zero.bet_type == BetType.NUMBER

        # Test betting on 36 (maximum)
        bet_max = Bet(10, self.player, BetType.NUMBER, 36)
        assert bet_max.bet_value == 36
        assert bet_max.bet_type == BetType.NUMBER

    def test_color_bet_payout_winning_red(self):
        """Test payout for winning red color bet."""
        initial_balance = self.player.get_balance()
        bet = Bet(50, self.player, BetType.COLOR, Color.RED)
        
        # Red wins (2:1 odds)
        bet.payout(Color.RED, 1)  # Position 1 is red
        
        expected_winnings = 50 * 2  # 2:1 odds
        expected_balance = initial_balance + expected_winnings
        assert self.player.get_balance() == expected_balance

    def test_color_bet_payout_winning_black(self):
        """Test payout for winning black color bet."""
        initial_balance = self.player.get_balance()
        bet = Bet(30, self.player, BetType.COLOR, Color.BLACK)
        
        # Black wins (2:1 odds)
        bet.payout(Color.BLACK, 2)  # Position 2 is black
        
        expected_winnings = 30 * 2  # 2:1 odds
        expected_balance = initial_balance + expected_winnings
        assert self.player.get_balance() == expected_balance

    def test_color_bet_payout_winning_green(self):
        """Test payout for winning green color bet."""
        initial_balance = self.player.get_balance()
        bet = Bet(20, self.player, BetType.COLOR, Color.GREEN)
        
        # Green wins (35:1 odds)
        bet.payout(Color.GREEN, 0)  # Position 0 is green
        
        expected_winnings = 20 * 35  # 35:1 odds
        expected_balance = initial_balance + expected_winnings
        assert self.player.get_balance() == expected_balance

    def test_color_bet_payout_losing(self):
        """Test payout for losing color bet."""
        initial_balance = self.player.get_balance()
        bet = Bet(40, self.player, BetType.COLOR, Color.RED)
        
        # Red loses (black wins)
        bet.payout(Color.BLACK, 2)
        
        # No payout for losing bet
        assert self.player.get_balance() == initial_balance

    def test_number_bet_payout_winning(self):
        """Test payout for winning number bet."""
        initial_balance = self.player.get_balance()
        bet = Bet(10, self.player, BetType.NUMBER, 17)
        
        # Number 17 wins (35:1 odds)
        bet.payout(Color.RED, 17)  # Position 17 wins
        
        expected_winnings = 10 * 35  # 35:1 odds for number bets
        expected_balance = initial_balance + expected_winnings
        assert self.player.get_balance() == expected_balance

    def test_number_bet_payout_losing(self):
        """Test payout for losing number bet."""
        initial_balance = self.player.get_balance()
        bet = Bet(15, self.player, BetType.NUMBER, 17)
        
        # Number 17 loses (different number wins)
        bet.payout(Color.RED, 23)  # Position 23 wins, not 17
        
        # No payout for losing bet
        assert self.player.get_balance() == initial_balance

    def test_number_bet_payout_zero_winning(self):
        """Test payout for winning bet on zero."""
        initial_balance = self.player.get_balance()
        bet = Bet(5, self.player, BetType.NUMBER, 0)
        
        # Zero wins (35:1 odds)
        bet.payout(Color.GREEN, 0)
        
        expected_winnings = 5 * 35  # 35:1 odds
        expected_balance = initial_balance + expected_winnings
        assert self.player.get_balance() == expected_balance

    def test_number_bet_payout_thirty_six_winning(self):
        """Test payout for winning bet on thirty-six."""
        initial_balance = self.player.get_balance()
        bet = Bet(8, self.player, BetType.NUMBER, 36)
        
        # Thirty-six wins (35:1 odds)
        bet.payout(Color.RED, 36)
        
        expected_winnings = 8 * 35  # 35:1 odds
        expected_balance = initial_balance + expected_winnings
        assert self.player.get_balance() == expected_balance

    def test_backward_compatibility_payout_old_signature(self):
        """Test that old payout method signature still works for backward compatibility."""
        initial_balance = self.player.get_balance()
        bet = Bet(25, self.player, color=Color.RED)
        
        # Old method signature (only winning_color)
        bet.payout(Color.RED)
        
        expected_winnings = 25 * 2  # 2:1 odds for red
        expected_balance = initial_balance + expected_winnings
        assert self.player.get_balance() == expected_balance

    def test_backward_compatibility_payout_old_signature_green(self):
        """Test backward compatibility for green bet with old signature."""
        initial_balance = self.player.get_balance()
        bet = Bet(10, self.player, color=Color.GREEN)
        
        # Old method signature (only winning_color)
        bet.payout(Color.GREEN)
        
        expected_winnings = 10 * 35  # 35:1 odds for green
        expected_balance = initial_balance + expected_winnings
        assert self.player.get_balance() == expected_balance

    def test_multiple_payouts_same_bet(self):
        """Test that multiple payout calls on same bet work correctly."""
        initial_balance = self.player.get_balance()
        bet = Bet(20, self.player, BetType.COLOR, Color.RED)
        
        # First payout - win
        bet.payout(Color.RED, 1)
        balance_after_first = self.player.get_balance()
        expected_after_first = initial_balance + (20 * 2)
        assert balance_after_first == expected_after_first
        
        # Second payout - lose (should not change balance)
        bet.payout(Color.BLACK, 2)
        assert self.player.get_balance() == balance_after_first

    def test_bet_with_different_amounts(self):
        """Test bets with various amounts to ensure payout calculations are correct."""
        test_cases = [
            (1, BetType.NUMBER, 5, 5, 35),    # $1 on number 5, wins
            (100, BetType.COLOR, Color.RED, Color.RED, 2),  # $100 on red, wins
            (50, BetType.COLOR, Color.GREEN, Color.GREEN, 35),  # $50 on green, wins
            (25, BetType.NUMBER, 0, 0, 35),   # $25 on zero, wins
        ]
        
        for amount, bet_type, bet_value, winning_value, expected_odds in test_cases:
            player = Player(1000)  # Fresh player for each test
            initial_balance = player.get_balance()
            bet = Bet(amount, player, bet_type, bet_value)
            
            if bet_type == BetType.NUMBER:
                bet.payout(Color.RED, winning_value)  # Color doesn't matter for number bets
            else:
                bet.payout(winning_value, 1)  # Position doesn't matter for color bets
            
            expected_winnings = amount * expected_odds
            expected_balance = initial_balance + expected_winnings
            assert player.get_balance() == expected_balance, (
                f"Failed for amount={amount}, bet_type={bet_type}, "
                f"bet_value={bet_value}, expected_odds={expected_odds}"
            )


def run_standalone_tests():
    """Run tests without pytest for environments where it's not available."""
    print("Running Bet class tests...")

    # Test BetType enum
    bet_type_test = TestBetType()
    bet_type_methods = [
        "test_bet_type_enum_values",
        "test_bet_type_enum_comparison",
    ]

    # Test Bet class
    bet_class_test = TestBetClass()
    bet_class_methods = [
        "test_bet_creation_color_new_format",
        "test_bet_creation_number_new_format", 
        "test_bet_creation_backward_compatibility",
        "test_bet_creation_edge_cases",
        "test_color_bet_payout_winning_red",
        "test_color_bet_payout_winning_black",
        "test_color_bet_payout_winning_green",
        "test_color_bet_payout_losing",
        "test_number_bet_payout_winning",
        "test_number_bet_payout_losing",
        "test_number_bet_payout_zero_winning",
        "test_number_bet_payout_thirty_six_winning",
        "test_backward_compatibility_payout_old_signature",
        "test_backward_compatibility_payout_old_signature_green",
        "test_multiple_payouts_same_bet",
        "test_bet_with_different_amounts",
    ]

    passed = 0
    failed = 0

    # Run BetType tests
    for method_name in bet_type_methods:
        try:
            method = getattr(bet_type_test, method_name)
            method()
            print(f"✓ {method_name}")
            passed += 1
        except Exception as e:
            print(f"✗ {method_name}: {e}")
            failed += 1

    # Run Bet class tests
    for method_name in bet_class_methods:
        try:
            bet_class_test.setup_method()
            method = getattr(bet_class_test, method_name)
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
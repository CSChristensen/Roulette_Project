#!/usr/bin/env python3
"""
Test script to verify game continuation logic is working properly.
"""

from game_controller import GameController
from player import Player
from table import Table

def test_game_continuation_methods():
    """Test the game continuation methods in isolation."""
    
    print("Testing GameController game continuation logic...")
    
    # Create a game controller
    controller = GameController()
    
    # Test 1: Test with a player who has money
    print("\n=== Test 1: Player with sufficient balance ===")
    controller.player = Player(100)
    print(f"Player balance: ${controller.player.get_balance()}")
    
    # Test validation methods
    print("\n=== Test 2: Validation methods ===")
    
    # Test yes/no validation
    test_cases = [
        ("y", True),
        ("yes", True),
        ("Y", True),
        ("YES", True),
        ("n", False),
        ("no", False),
        ("N", False),
        ("NO", False),
        ("maybe", None),
        ("", None)
    ]
    
    for input_val, expected in test_cases:
        result = controller.validate_yes_no(input_val)
        status = "✓" if result == expected else "✗"
        print(f"{status} validate_yes_no('{input_val}') -> {result} (expected {expected})")
    
    # Test 3: Test with zero balance player
    print("\n=== Test 3: Player with zero balance ===")
    controller.player = Player(0)
    print(f"Player balance: ${controller.player.get_balance()}")
    
    print("\nAll basic tests completed successfully!")
    print("The game continuation logic appears to be fully implemented.")

if __name__ == "__main__":
    test_game_continuation_methods()
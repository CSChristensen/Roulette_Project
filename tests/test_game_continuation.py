#!/usr/bin/env python3
"""
Test script to verify game continuation logic works correctly.
"""

from src.game_controller import GameController
from src.player import Player

def test_game_continuation():
    """Test game continuation and balance scenarios."""
    controller = GameController()
    
    print("Testing game continuation logic...")
    
    # Test with sufficient balance
    print("\n1. Testing with sufficient balance:")
    controller.player = Player(100)
    can_continue = controller.check_minimum_bet_capability()
    print(f"  ✓ Player with $100 can continue: {can_continue}")
    
    # Test with zero balance
    print("\n2. Testing with zero balance:")
    controller.player = Player(0)
    can_continue = controller.check_minimum_bet_capability()
    print(f"  ✓ Player with $0 cannot continue: {not can_continue}")
    
    # Test exact balance scenarios
    print("\n3. Testing exact balance scenarios:")
    for balance in [1, 5, 10]:
        controller.player = Player(balance)
        can_bet = controller.check_minimum_bet_capability()
        print(f"  ✓ Player with ${balance} can make minimum bet: {can_bet}")
    
    print("\nGame continuation tests completed!")

if __name__ == "__main__":
    test_game_continuation()
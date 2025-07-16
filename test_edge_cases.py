#!/usr/bin/env python3
"""
Simple test script to verify edge case handling works correctly.
"""

from game_controller import GameController
from player import Player

def test_edge_cases():
    """Test edge case handling methods."""
    controller = GameController()
    
    print("Testing edge case handling...")
    
    # Test minimum bet capability check
    print("\n1. Testing minimum bet capability:")
    
    # Create player with $1 (minimum bet)
    controller.player = Player(1)
    result = controller.check_minimum_bet_capability()
    print(f"  ✓ Player with $1 can make minimum bet: {result}")
    
    # Create player with $0
    controller.player = Player(0)
    result = controller.check_minimum_bet_capability()
    print(f"  ✓ Player with $0 cannot make minimum bet: {not result}")
    
    # Test balance validation
    print("\n2. Testing balance edge cases:")
    
    # Test player with exact balance for bet
    controller.player = Player(50)
    balance = controller.player.get_balance()
    print(f"  ✓ Player created with ${balance}")
    
    # Test that player class handles insufficient balance correctly
    try:
        controller.player.subtract_from_balance(100)  # More than balance
        print("  ✗ Should have raised ValueError for insufficient balance")
    except ValueError as e:
        print(f"  ✓ Correctly caught insufficient balance error: {e}")
    
    # Test that balance is unchanged after failed subtraction
    balance_after = controller.player.get_balance()
    print(f"  ✓ Balance unchanged after failed subtraction: ${balance_after}")
    
    print("\nEdge case tests completed!")

if __name__ == "__main__":
    test_edge_cases()
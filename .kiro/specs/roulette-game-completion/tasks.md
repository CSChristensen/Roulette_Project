# Implementation Plan

- [x] 1. Fix critical bugs in existing classes
  - Fix typos and method signature issues that prevent the game from running
  - Ensure all existing functionality works correctly
  - _Requirements: 5.1, 5.4_

- [x] 1.1 Fix Player class method typo and add balance getter
  - Rename `subract_from_balance` to `subtract_from_balance`
  - Add `get_balance()` method to return current balance
  - Add validation to prevent negative balances in subtract method
  - _Requirements: 5.4_

- [x] 1.2 Fix Wheel class attribute typo and method call
  - Rename `_ball_postion` to `_ball_position` 
  - Fix `get_ball_position` method call in main (missing parentheses)
  - Ensure method returns correct tuple format
  - _Requirements: 5.1, 5.4_

- [x] 1.3 Fix Table class payout logic
  - Update `spin_wheel_and_payout` method to call `spin_wheel` instead of `spin`
  - Fix `_payout_bets` method to get winning color and pass it to bet payout
  - Ensure bets are cleared after processing
  - _Requirements: 5.2, 5.3_

- [x] 1.4 Fix Bet class payout method
  - Update payout method to only add winnings when bet wins
  - Ensure correct odds are applied (2:1 for Red/Black, 35:1 for Green)
  - Add logic to handle losing bets (no payout)
  - _Requirements: 5.2_

- [x] 2. Create GameController class for user interface
  - Implement main game loop with user interaction
  - Handle all user input validation and error messages
  - _Requirements: 1.1, 1.2, 1.3, 1.4_

- [x] 2.1 Implement basic GameController structure
  - Create GameController class with initialization
  - Add methods for displaying messages and getting user input
  - Implement input validation helper methods
  - _Requirements: 1.1, 1.4_

- [x] 2.2 Implement player setup and deposit handling
  - Add method to prompt for and validate initial deposit
  - Create player with validated deposit amount
  - Handle invalid input with error messages and re-prompting
  - _Requirements: 1.2, 1.3, 1.4_

- [x] 2.3 Implement betting interface
  - Add method to display current balance and prompt for bet
  - Validate bet amount against player balance
  - Validate color choice input (red/black/green)
  - Handle invalid inputs with appropriate error messages
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_

- [x] 2.4 Implement game round execution
  - Add method to process wheel spin and display results
  - Show winning number and color to player
  - Display payout results and updated balance
  - _Requirements: 3.1, 3.2, 3.3, 3.4_

- [x] 2.5 Implement game continuation logic
  - Add method to prompt for continue/quit decision
  - Handle insufficient balance scenarios
  - Provide option to make additional deposits
  - Implement graceful game exit with final balance display
  - _Requirements: 4.1, 4.2, 4.3, 4.4_

- [x] 3. Update main game entry point
  - Replace current main() function with GameController usage
  - Remove test code and implement proper game initialization
  - _Requirements: 1.1_

- [x] 3.1 Refactor main() function
  - Remove existing test code from main()
  - Initialize and start GameController
  - Add proper error handling for game startup
  - _Requirements: 1.1_

- [x] 4. Add comprehensive error handling and edge cases
  - Ensure all user inputs are properly validated
  - Handle edge cases like exact balance bets
  - _Requirements: 5.5_

- [x] 4.1 Implement robust input validation
  - Add validation for all numeric inputs (deposits, bets)
  - Add validation for color choices with case-insensitive matching
  - Add validation for yes/no prompts
  - Ensure all validation includes error messages and re-prompting
  - _Requirements: 5.5_

- [x] 4.2 Add edge case handling
  - Handle case where player has exactly enough for minimum bet
  - Handle case where player balance becomes zero
  - Add proper error handling for all game operations
  - _Requirements: 5.5_

- [x] 5. Create comprehensive test suite
  - Implement unit tests for all validation methods
  - Test edge cases and error handling scenarios
  - Verify game continuation logic works correctly
  - _Requirements: 5.5_

- [x] 5.1 Implement validation tests
  - Create test_validation.py with comprehensive validation tests
  - Test positive integer validation with edge cases
  - Test color choice validation with case-insensitive matching
  - Test yes/no validation with multiple input variations
  - _Requirements: 5.5_

- [x] 5.2 Implement edge case tests
  - Create test_edge_cases.py for boundary condition testing
  - Test minimum bet capability checking
  - Test balance validation and error handling
  - Verify insufficient balance scenarios work correctly
  - _Requirements: 5.5_

- [x] 5.3 Implement game continuation tests
  - Create test_game_continuation.py for flow testing
  - Test game continuation with various balance scenarios
  - Verify zero balance handling works correctly
  - Test exact balance betting scenarios
  - _Requirements: 4.1, 4.2, 4.3, 4.4_
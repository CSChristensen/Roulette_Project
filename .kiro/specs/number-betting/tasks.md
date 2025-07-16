# Implementation Plan

- [x] 1. Create BetType enumeration and enhance Bet class





  - Add BetType enum to support "color" and "number" betting types
  - Modify Bet class constructor to accept bet type and value (Color or int)
  - Update payout method to handle both color and number bets with correct odds
  - _Requirements: 1.1, 2.1, 2.2, 5.1, 5.2_

- [x] 1.1 Add BetType enumeration


  - Create BetType enum with COLOR and NUMBER values
  - Import and use in bet-related modules
  - _Requirements: 5.1, 5.2_

- [x] 1.2 Enhance Bet class for dual bet types


  - Modify __init__ method to accept bet_type and bet_value parameters
  - Update class attributes to store bet type and value (Union[Color, int])
  - Maintain backward compatibility with existing color-only bet creation
  - _Requirements: 1.1, 5.1, 5.3_

- [x] 1.3 Update Bet payout method for number betting


  - Modify payout method to accept both winning_position and winning_color
  - Implement logic to check number bet wins (exact position match)
  - Apply correct odds: 35:1 for number bets, existing odds for color bets
  - Ensure losing bets don't receive payouts
  - _Requirements: 2.1, 2.2, 2.4_
-

- [x] 2. Add number validation to GameController




  - Implement validate_number_choice method for number input validation
  - Add bet type selection functionality
  - Update display methods to show number betting options and odds
  - _Requirements: 1.2, 1.4, 1.5, 4.1, 4.2_

- [x] 2.1 Implement number input validation


  - Create validate_number_choice method that accepts string input
  - Validate input is integer between 0-36 inclusive
  - Handle non-numeric input with appropriate error messages
  - Return validated integer or None for invalid input
  - _Requirements: 1.4, 1.5_

- [x] 2.2 Add bet type selection interface


  - Create get_bet_type method to prompt user for bet type choice
  - Validate bet type input (color/number, case-insensitive)
  - Display available options with odds information
  - Return BetType enum value or None for invalid input
  - _Requirements: 1.1, 4.1, 4.2_

- [x] 2.3 Update welcome message and help display


  - Modify display_welcome method to include number betting information
  - Add odds display for both color betting (2:1 Red/Black, 35:1 Green) and number betting (35:1)
  - Update game instructions to explain both betting types
  - _Requirements: 4.1, 4.2_

- [x] 3. Enhance betting flow for multiple bet types





  - Update handle_betting method to support bet type selection
  - Implement number betting flow alongside existing color betting
  - Add bet confirmation display showing type, amount, and selection
  - _Requirements: 1.1, 1.2, 1.3, 4.3, 4.4_

- [x] 3.1 Modify betting flow for type selection


  - Update handle_betting method to first prompt for bet type
  - Branch to appropriate input collection based on bet type
  - Maintain existing color betting flow for backward compatibility
  - _Requirements: 1.1, 5.3_

- [x] 3.2 Implement number betting flow

  - Add number betting branch in handle_betting method
  - Prompt for number choice using validate_number_choice
  - Create number-based Bet object with correct parameters
  - Display bet confirmation with number and odds information
  - _Requirements: 1.2, 1.3, 4.3_

- [x] 3.3 Add bet confirmation display


  - Create display_bet_confirmation method to show bet details
  - Display bet type, amount, selection, and potential payout
  - Use consistent formatting for both color and number bets
  - _Requirements: 4.3_

- [x] 4. Update Table class to pass winning position to bets



  - Modify _payout_bets method to pass both winning position and color
  - Ensure all bet payout calls receive complete winning information
  - Maintain compatibility with existing color-only bet processing
  - _Requirements: 2.4, 5.1, 5.3_

- [x] 4.1 Update Table payout method signature


  - Modify _payout_bets method to get winning position from wheel
  - Pass both winning_position and winning_color to each bet's payout method
  - Update method calls to provide complete winning information
  - _Requirements: 2.4, 5.2_

- [x] 5. Add support for multiple bets per round





  - Implement multiple bet placement functionality
  - Update game flow to handle multiple bets of different types
  - Enhance result display to show outcomes for each bet
  - _Requirements: 3.1, 3.2, 3.3, 3.4_

- [x] 5.1 Implement multiple bet placement


  - Add handle_multiple_bets method to GameController
  - Allow players to place additional bets after first bet
  - Validate total bet amounts don't exceed player balance
  - Track all bets placed in current round
  - _Requirements: 3.1, 3.2_

- [x] 5.2 Update round execution for multiple bets


  - Modify execute_round method to handle multiple bets
  - Calculate and display individual payout results for each bet
  - Show total winnings/losses for the round
  - Display detailed results showing each bet outcome
  - _Requirements: 3.3, 3.4, 4.4_
-

- [x] 6. Create comprehensive test suite for number betting




  - Implement unit tests for BetType enum and enhanced Bet class
  - Test number input validation with edge cases
  - Test payout calculations for number bets
  - Test multiple bet scenarios and mixed bet types
  - _Requirements: 5.4, 5.5_

- [x] 6.1 Create unit tests for enhanced Bet class


  - Test Bet creation with both color and number bet types
  - Test payout method with winning and losing number bets
  - Verify correct odds application (35:1 for numbers)
  - Test edge cases like betting on 0 and 36
  - _Requirements: 5.4, 5.5_

- [x] 6.2 Create validation tests for number input


  - Test validate_number_choice with valid inputs (0-36)
  - Test invalid inputs (negative, >36, non-numeric, empty)
  - Test edge cases and boundary conditions
  - Verify error message accuracy and helpfulness
  - _Requirements: 5.5_

- [x] 6.3 Create integration tests for mixed betting


  - Test rounds with both color and number bets
  - Test multiple bets of same type and mixed types
  - Verify balance updates with complex bet combinations
  - Test game flow with various betting scenarios
  - _Requirements: 5.5_
-

- [x] 7. Update main game entry point and documentation









  - Ensure main.py works with enhanced GameController
  - Update any documentation or help text
  - Verify backward compatibility with existing functionality
  - _Requirements: 5.3_

- [x] 7.1 Verify main entry point compatibility


  - Test main.py with enhanced GameController
  - Ensure existing game flow continues to work
  - Verify new features are accessible through main interface
  - _Requirements: 5.3_
# Design Document

## Overview

The roulette game completion will focus on fixing existing bugs, implementing missing functionality, and creating a proper command-line interface. The current codebase has good object-oriented structure but needs several critical fixes and the addition of a game loop with user interaction.

## Architecture

The existing architecture will be maintained with these components:
- **Player**: Manages balance and transactions
- **Bet**: Represents individual wagers with payout logic
- **Table**: Coordinates bets and wheel interactions
- **Wheel**: Handles random number generation and color mapping
- **Game Controller**: New component to manage user interface and game flow

## Components and Interfaces

### Fixed Components

#### Player Class
- Fix typo in `subract_from_balance` method name
- Add balance getter method for display purposes
- Add validation to prevent negative balances

#### Table Class
- Fix `spin_wheel_and_payout` method to properly call payout with winning color
- Fix `_payout_bets` method to pass the winning color to bet payout
- Add method to clear bets after payout

#### Wheel Class
- Fix typo in `_ball_postion` attribute name
- Ensure `get_ball_position` method works correctly as a method call

#### Bet Class
- Fix payout logic to handle the case where bet loses (no payout)
- Ensure proper odds calculation

### New Components

#### GameController Class
- Manages the main game loop
- Handles user input and validation
- Coordinates between all game components
- Provides user interface through console I/O

## Data Models

### User Input Validation
- Deposit amounts: Must be positive integers
- Bet amounts: Must be positive integers not exceeding player balance
- Color choices: Must be one of "red", "black", or "green" (case-insensitive)
- Continue/quit choices: Must be "y/n" or "yes/no" (case-insensitive)

### Game State
- Current player balance
- Active bets for current round
- Wheel position and winning color
- Game continuation status

## Error Handling

### Input Validation Errors
- Invalid numeric input: Display error message and re-prompt
- Insufficient funds: Display balance and re-prompt for valid bet
- Invalid color choice: Display valid options and re-prompt

### Game Logic Errors
- Prevent negative balances through validation
- Handle edge case where player has exactly enough for one bet
- Graceful exit when player chooses to quit

## Testing Strategy

### Unit Testing Approach
- Test each class method individually
- Test edge cases for balance operations
- Test payout calculations for all color combinations
- Test input validation functions

### Integration Testing
- Test complete game rounds from bet to payout
- Test multiple consecutive rounds
- Test game termination scenarios

### Manual Testing
- Play through complete game sessions
- Test all user input scenarios
- Verify correct balance updates and payouts
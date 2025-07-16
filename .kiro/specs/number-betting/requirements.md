# Requirements Document

## Introduction

This document outlines the requirements for adding number betting functionality to the existing roulette game. Players will be able to bet on specific numbers (0-36) in addition to the existing color betting, with higher payouts for successful number bets following standard roulette odds.

## Requirements

### Requirement 1

**User Story:** As a player, I want to bet on specific numbers, so that I can have more betting options with higher potential payouts.

#### Acceptance Criteria

1. WHEN the system prompts for bet type THEN the player SHALL be able to choose between "color" and "number" betting
2. WHEN a player chooses number betting THEN the system SHALL prompt for a specific number between 0 and 36
3. WHEN a player enters a valid number (0-36) THEN the system SHALL accept the bet and deduct the amount from their balance
4. WHEN a player enters an invalid number (outside 0-36 range) THEN the system SHALL display an error and prompt again
5. WHEN a player enters non-numeric input for number betting THEN the system SHALL display an error and prompt again

### Requirement 2

**User Story:** As a player, I want number bets to pay higher odds than color bets, so that the risk/reward matches standard roulette rules.

#### Acceptance Criteria

1. WHEN a number bet wins THEN the system SHALL pay 35:1 odds (35 times the bet amount plus the original bet)
2. WHEN a number bet loses THEN the system SHALL not return any money (bet amount already deducted)
3. WHEN displaying payout information THEN the system SHALL clearly show the different odds for number vs color bets
4. WHEN calculating payouts THEN the system SHALL use the correct odds based on bet type

### Requirement 3

**User Story:** As a player, I want to place multiple bets of different types in the same round, so that I can use various betting strategies.

#### Acceptance Criteria

1. WHEN placing bets THEN the player SHALL be able to place multiple bets (both color and number) in the same round
2. WHEN the system prompts for additional bets THEN the player SHALL be able to choose to place another bet or proceed to spin
3. WHEN multiple bets are placed THEN the system SHALL track and process all bets correctly
4. WHEN displaying results THEN the system SHALL show the outcome for each individual bet placed

### Requirement 4

**User Story:** As a player, I want clear information about betting options and odds, so that I can make informed betting decisions.

#### Acceptance Criteria

1. WHEN the game starts THEN the system SHALL display information about available bet types and their odds
2. WHEN prompting for bet type THEN the system SHALL show the current options (color: 2:1 for Red/Black, 35:1 for Green; number: 35:1)
3. WHEN a bet is placed THEN the system SHALL confirm the bet type, amount, and selection
4. WHEN displaying results THEN the system SHALL show the winning number, its color, and payout details for each bet

### Requirement 5

**User Story:** As a developer, I want the number betting functionality to integrate seamlessly with existing code, so that the game remains maintainable and bug-free.

#### Acceptance Criteria

1. WHEN implementing number betting THEN the system SHALL extend existing classes without breaking current functionality
2. WHEN processing bets THEN the system SHALL handle both color and number bets using a unified approach
3. WHEN the game runs THEN the system SHALL maintain all existing functionality while adding new features
4. WHEN errors occur THEN the system SHALL handle them gracefully without crashing the game
5. WHEN testing THEN the system SHALL pass all existing tests and new tests for number betting functionality
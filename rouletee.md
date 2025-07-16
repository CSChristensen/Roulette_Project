# Enhanced Roulette Game Documentation

## Overview

This is a comprehensive Python-based roulette game simulation that implements both traditional color betting and modern number betting functionality. The game follows European roulette rules with a single zero (0-36 positions) and provides an interactive command-line interface for players.

## Game Features

### Dual Betting System
The game supports two distinct betting types:

1. **Color Betting** (Traditional)
   - Red/Black bets with 2:1 odds
   - Green (0) bets with 35:1 odds
   - Classic roulette experience

2. **Number Betting** (Enhanced)
   - Bet on specific numbers 0-36
   - All number bets pay 35:1 odds
   - High-risk, high-reward gameplay

### Advanced Features
- **Multiple Bets Per Round**: Place multiple bets of different types in a single spin
- **Interactive Interface**: Clear prompts, confirmations, and detailed results
- **Balance Management**: Real-time balance tracking with transaction history
- **Input Validation**: Comprehensive validation for all user inputs
- **Backward Compatibility**: All original functionality preserved

## Technical Architecture

### Core Components

#### Player Class (`src/player.py`)
- Manages player balance and transactions
- Handles deposits, withdrawals, and bet deductions
- Provides balance validation and history tracking

#### Bet Class (`src/bet.py`)
- Unified betting system supporting both color and number bets
- BetType enumeration for type safety (COLOR, NUMBER)
- Intelligent payout calculation based on bet type and winning conditions

#### Table Class (`src/table.py`)
- Central coordinator for bet management
- Interfaces with wheel for spin results
- Processes multiple bets and calculates payouts

#### Wheel Class (`src/wheel.py`)
- Simulates European roulette wheel (0-36)
- Maps positions to colors using standard roulette layout
- Provides random number generation for fair gameplay

#### GameController Class (`src/game_controller.py`)
- Manages game flow and user interface
- Handles bet type selection and input validation
- Provides enhanced user experience with confirmations and detailed results

### Data Flow

1. **Game Initialization**: Player creates account with initial deposit
2. **Bet Placement**: Player selects bet type, amount, and choice
3. **Bet Validation**: System validates inputs and deducts bet amount
4. **Multiple Bets**: Optional additional bets in same round
5. **Wheel Spin**: Random number generation determines outcome
6. **Payout Processing**: Calculate and apply winnings based on bet types
7. **Result Display**: Show detailed outcomes for each bet
8. **Balance Update**: Update player balance with winnings/losses

## Game Rules and Odds

### Wheel Layout
- **37 Positions**: Numbers 0-36 (European style, single zero)
- **Color Distribution**:
  - **Red**: 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
  - **Black**: 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35
  - **Green**: 0 (zero)

### Betting Options and Payouts

#### Color Betting
- **Red/Black Bets**: 2:1 odds (double your money)
  - Win if ball lands on any number of chosen color
  - 18 winning numbers out of 37 total
- **Green Bet**: 35:1 odds (35 times your money)
  - Win only if ball lands on 0
  - 1 winning number out of 37 total

#### Number Betting
- **Specific Number Bets**: 35:1 odds (35 times your money)
  - Win only if ball lands on exact chosen number
  - 1 winning number out of 37 total
  - Available for all numbers 0-36

### Betting Rules
- **Minimum Bet**: $1 per bet
- **Maximum Bet**: Limited by available balance
- **Multiple Bets**: No limit on number of bets per round
- **Mixed Types**: Can combine color and number bets in same round
- **Balance Requirement**: Must have sufficient balance for all bets

## Usage Examples

### Basic Color Betting
```
Enter bet type (color/number): color
Choose your color (red/black/green): red
Enter your bet amount: $100

BET CONFIRMATION
Bet Type: Color
Selection: Red
Bet Amount: $100
Odds: 2:1
Potential Payout: $200
```

### Number Betting
```
Enter bet type (color/number): number
Enter your number choice (0-36): 17
Enter your bet amount: $50

BET CONFIRMATION
Bet Type: Number
Selection: 17
Bet Amount: $50
Odds: 35:1
Potential Payout: $1750
```

### Multiple Bets Example
```
# First bet
Bet Type: Color, Selection: Red, Amount: $100

# Second bet
Bet Type: Number, Selection: 7, Amount: $25

# Results
The ball landed on: 7 (RED)
Bet #1: $100 on Red - ✅ WON! Payout: $200
Bet #2: $25 on number 7 - ✅ WON! Payout: $875
Total winnings: $1075
```

## Installation and Setup

### Prerequisites
- Python 3.x (no external dependencies required)
- Command-line interface (Terminal, Command Prompt, PowerShell)

### Installation
1. Download or clone the project files
2. Navigate to the project directory
3. Ensure Python 3.x is installed and accessible

### Running the Game

#### Primary Method
```bash
python main.py
```

#### Alternative Method
```bash
python -m src.Rouletee
```

#### Module Testing
```bash
# Test individual components
python -m src.player
python -m src.wheel
python -m src.table
```

## Testing

### Test Suite
The project includes comprehensive tests covering:

- **Unit Tests**: Individual class functionality
- **Integration Tests**: Multi-component interactions
- **Validation Tests**: Input validation and edge cases
- **Compatibility Tests**: Backward compatibility verification

### Running Tests
```bash
# Run individual test files
python -m tests.test_validation
python -m tests.test_edge_cases
python -m tests.test_game_continuation
python -m tests.test_bet_class
python -m tests.test_number_validation
python -m tests.test_mixed_betting_integration

# Run with pytest (if available)
python -m pytest tests/
```

## Development Notes

### Code Quality
- **Type Hints**: Full type annotation throughout codebase
- **Enumerations**: Type-safe enums for colors and bet types
- **Error Handling**: Comprehensive input validation and error recovery
- **Documentation**: Detailed docstrings and comments

### Architecture Principles
- **Single Responsibility**: Each class has a clear, focused purpose
- **Open/Closed**: Easy to extend with new bet types or features
- **Dependency Inversion**: Clean interfaces between components
- **Backward Compatibility**: New features don't break existing functionality

### Extensibility
The architecture supports easy addition of:
- New bet types (e.g., odd/even, high/low)
- Different wheel layouts (American double-zero)
- Advanced betting strategies
- Multiplayer functionality
- Persistent game state

## Troubleshooting

### Common Issues

#### Game Won't Start
- Ensure Python 3.x is installed
- Check that all files are in correct directory structure
- Verify main.py has execute permissions

#### Input Validation Errors
- Number bets: Must be integers 0-36
- Color bets: Must be "red", "black", or "green" (case-insensitive)
- Bet amounts: Must be positive integers within available balance

#### Balance Issues
- Ensure sufficient balance before placing bets
- Check that initial deposit is positive
- Verify bet amounts don't exceed available balance

### Getting Help
- Check error messages for specific guidance
- Review game rules and betting options
- Ensure inputs match expected formats
- Restart game if persistent issues occur

## Version History

### Current Version (Enhanced)
- ✅ Number betting system (0-36) with 35:1 odds
- ✅ Multiple bet support per round
- ✅ Enhanced user interface with confirmations
- ✅ Comprehensive input validation
- ✅ Detailed result reporting
- ✅ Backward compatibility maintained

### Previous Version (Basic)
- ✅ Color betting (Red/Black/Green)
- ✅ Player balance management
- ✅ Basic roulette wheel simulation
- ✅ Simple game flow

## Future Enhancements

### Potential Features
- **American Roulette**: Double-zero wheel option
- **Advanced Bets**: Odd/even, high/low, dozens, columns
- **Betting Strategies**: Martingale, Fibonacci, D'Alembert systems
- **Statistics**: Win/loss tracking, betting history
- **Multiplayer**: Multiple players per table
- **GUI Interface**: Graphical user interface option
- **Save/Load**: Persistent game state

### Technical Improvements
- **Configuration**: External config files for game settings
- **Logging**: Detailed game logging for debugging
- **Performance**: Optimization for large numbers of bets
- **Internationalization**: Multi-language support
- **API**: REST API for external integrations

## License and Usage

This project is designed for educational and entertainment purposes. It demonstrates object-oriented programming principles, game logic implementation, and user interface design in Python.

### Educational Value
- **OOP Concepts**: Classes, inheritance, encapsulation
- **Design Patterns**: Strategy, Factory, Observer patterns
- **Input Validation**: Robust user input handling
- **Error Handling**: Graceful error recovery
- **Testing**: Comprehensive test suite development
- **Documentation**: Professional documentation practices

Feel free to use, modify, and extend this code for learning purposes or as a foundation for more complex gaming applications.
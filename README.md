# Enhanced Roulette Game

A comprehensive Python-based roulette game simulation featuring both traditional color betting and modern number betting with an interactive command-line interface. Experience the thrill of European roulette with multiple betting options, realistic odds, and professional game flow.

## Features

### Core Gameplay
- **Player Balance Management**: Deposit, withdraw, and track your balance
- **Dual Betting System**: Choose between color betting and number betting
- **Multiple Bets**: Place multiple bets of different types in a single round
- **Realistic Wheel**: European roulette wheel with 37 positions (0-36)
- **Automatic Payouts**: Correct odds calculation and balance updates

### Betting Options

#### Color Betting
- **Red/Black**: Pay 2:1 odds
- **Green (0)**: Pays 35:1 odds
- Traditional roulette color betting experience

#### Number Betting
- **Specific Numbers**: Bet on any number from 0-36
- **High Payouts**: All number bets pay 35:1 odds
- **Exact Match**: Win only if the ball lands on your exact number

### Game Features
- **Interactive Interface**: Clear prompts and confirmations
- **Bet Confirmation**: Review your bets before spinning
- **Detailed Results**: See outcomes for each individual bet
- **Round Summary**: Track your winnings and losses
- **Multiple Rounds**: Play as many rounds as you want

## Installation

### Prerequisites
- Python 3.x
- No external dependencies required (uses Python standard library only)

### Setup
1. Clone or download the project
2. Navigate to the project directory
3. Run the game using one of the methods below

## Usage

### Running the Game

#### Primary Method
```bash
python main.py
```

#### Alternative Method
```bash
python -m src.Rouletee
```

### Game Flow
1. **Initial Deposit**: Enter your starting balance
2. **Place Bets**: 
   - Choose bet type (color or number)
   - Enter bet amount
   - Select your choice (color or specific number)
   - Optionally place additional bets
3. **Spin**: Watch the wheel spin and see results
4. **Results**: View detailed outcomes and updated balance
5. **Continue**: Choose to play another round or exit

### Example Gameplay
```
Enter your initial deposit amount: $1000
Enter your bet amount: $50
Enter bet type (color/number): number
Enter your number choice (0-36): 17

BET CONFIRMATION
Bet Type: Number
Selection: 17
Bet Amount: $50
Odds: 35:1
Potential Payout: $1750

The ball landed on: 17 (RED)
✅ Won $1750!
Your new balance: $2700
```

## Testing

### Run Tests
```bash
# Run individual test files
python -m tests.test_validation
python -m tests.test_edge_cases
python -m tests.test_game_continuation

# Run with pytest (if available)
python -m pytest tests/
```

### Test Coverage
- **Input Validation**: Number and color input validation
- **Bet Processing**: Color and number bet creation and payouts
- **Edge Cases**: Boundary conditions and error handling
- **Integration**: Mixed betting scenarios and game flow

## Project Structure

```
Roulette_Project/
├── main.py                    # Main entry point
├── src/                       # Source code package
│   ├── __init__.py           # Package initialization
│   ├── Rouletee.py           # Main game orchestration
│   ├── game_controller.py    # Game flow and user interface
│   ├── player.py             # Player balance management
│   ├── bet.py                # Betting system with dual types
│   ├── table.py              # Bet management and wheel interaction
│   └── wheel.py              # Wheel simulation and position mapping
├── tests/                     # Comprehensive test suite
└── .kiro/                     # Development specifications
```

## Technical Details

### Architecture
- **Object-Oriented Design**: Clean separation of concerns
- **Type Hints**: Full type annotation for better code quality
- **Enum-Based**: Color and bet type enumerations for type safety
- **Backward Compatible**: Existing functionality preserved

### Key Classes
- **Player**: Manages balance and transactions
- **Bet**: Handles both color and number bets with unified payout logic
- **Table**: Coordinates bets and wheel interactions
- **Wheel**: Simulates roulette wheel with position-to-color mapping
- **GameController**: Manages game flow and user interface

### Betting System
- **BetType Enum**: COLOR and NUMBER bet types
- **Unified Payout**: Single method handles both bet types
- **Multiple Bets**: Support for multiple bets per round
- **Validation**: Comprehensive input validation for all bet types

## Game Rules

### Roulette Wheel
- **37 Positions**: Numbers 0-36 (European style)
- **Color Distribution**:
  - Red: 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
  - Black: 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35
  - Green: 0

### Payout Odds
- **Red/Black Color Bets**: 2:1 (double your money)
- **Green Color Bet**: 35:1 (35 times your money)
- **Any Number Bet**: 35:1 (35 times your money)

### Betting Rules
- **Minimum Bet**: $1
- **Maximum Bet**: Limited by your balance
- **Multiple Bets**: Place as many bets as you want per round
- **Mixed Types**: Combine color and number bets in the same round

## Development

### Code Style
- **Python 3.x**: Modern Python features
- **Type Hints**: Full type annotation
- **Snake Case**: Method and variable naming
- **PascalCase**: Class naming
- **Docstrings**: Comprehensive documentation

### Contributing
1. Follow existing code style and patterns
2. Add tests for new features
3. Update documentation as needed
4. Ensure backward compatibility

## License

This project is for educational and entertainment purposes.

## Changelog

### Latest Version
- ✅ Added number betting (0-36) with 35:1 odds
- ✅ Multiple bet support per round
- ✅ Enhanced user interface with bet confirmations
- ✅ Comprehensive test suite
- ✅ Backward compatibility maintained
- ✅ Detailed result reporting

### Previous Versions
- ✅ Basic color betting (Red/Black/Green)
- ✅ Player balance management
- ✅ Roulette wheel simulation
- ✅ Basic game flow
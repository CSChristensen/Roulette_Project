# Project Structure

## File Organization
The project follows a structured package layout with source code and tests organized in separate directories:

```
├── main.py                    # Main entry point
├── src/                       # Source code package
│   ├── __init__.py           # Package initialization
│   ├── Rouletee.py           # Main game orchestration
│   ├── player.py             # Player class with balance management
│   ├── bet.py                # Bet class linking players, amounts, and colors
│   ├── table.py              # Table class managing bets and wheel interactions
│   ├── wheel.py              # Wheel class with spinning logic and position mapping
│   └── game_controller.py    # Game flow controller
├── tests/                     # Test suite
│   ├── test_validation.py    # Input validation tests
│   ├── test_edge_cases.py    # Edge case testing
│   └── test_game_continuation.py # Game flow tests
├── .kiro/                     # Kiro configuration and specs
│   └── steering/              # Project steering documentation
├── rouletee.md               # Project documentation
├── pyproject.toml            # Project configuration
└── .gitignore                # Git ignore rules
```

## Architecture Patterns

### Core Components
- **Player**: Manages individual player state and balance operations
- **Bet**: Represents a single wager with amount, color choice, and player reference
- **Table**: Central coordinator that manages active bets and wheel interactions
- **Wheel**: Handles random number generation and position-to-color mapping

### Data Flow
1. Players are created with initial balance
2. Bets are created linking player, amount, and color choice
3. Bets are placed on the table
4. Table spins wheel and processes payouts
5. Player balances are updated based on outcomes

## Naming Conventions
- **Files**: snake_case for modules, PascalCase for main entry point
- **Classes**: PascalCase (Player, Bet, Table, Wheel)
- **Methods**: snake_case (place_bet, spin_wheel, add_to_balance)
- **Private attributes**: Leading underscore (_balance, _ball_position)
- **Constants**: UPPER_SNAKE_CASE (WHEEL_POSITIONS)

## Import Structure
- Each module imports only what it needs
- Circular imports avoided through careful dependency design
- Main game logic in src/Rouletee.py imports all other modules
- Tests import from src package using relative imports
- Package structure allows for clean module organization
# Project Structure Overview

This document outlines the reorganized structure of the Roulette Game project.

## Directory Layout

```
Roulette_Project/
├── main.py                    # Main entry point for the game
├── src/                       # Source code package
│   ├── __init__.py           # Package initialization
│   ├── Rouletee.py           # Main game orchestration
│   ├── game_controller.py    # Game flow controller and UI
│   ├── player.py             # Player class with balance management
│   ├── bet.py                # Bet class linking players, amounts, and colors
│   ├── table.py              # Table class managing bets and wheel interactions
│   └── wheel.py              # Wheel class with spinning logic and position mapping
├── tests/                     # Test suite
│   ├── test_validation.py    # Input validation tests
│   ├── test_edge_cases.py    # Edge case testing
│   └── test_game_continuation.py # Game flow tests
├── .kiro/                     # Kiro configuration and specs
│   └── steering/              # Project steering documentation
│       ├── product.md        # Product overview and features
│       ├── structure.md      # Project structure documentation
│       └── tech.md           # Technology stack information
├── rouletee.md               # Project documentation
├── pyproject.toml            # Project configuration
├── README.md                 # Project README
└── .gitignore                # Git ignore rules
```

## Key Changes Made

### 1. Source Code Organization
- Moved all source files to `src/` directory
- Created `src/__init__.py` to make it a proper Python package
- Updated all imports to use relative imports within the package

### 2. Test Organization
- Moved all test files to `tests/` directory
- Updated test imports to reference the `src` package
- Tests can be run using `python -m tests.test_name`

### 3. Entry Point
- Created `main.py` as the primary entry point
- Imports and calls the main function from `src.Rouletee`

### 4. Documentation Updates
- Updated Kiro steering files to reflect new structure
- Added comprehensive project structure documentation

## Running the Project

### Run the Game
```bash
# Primary method
python main.py

# Alternative method
python -m src.Rouletee
```

### Run Tests
```bash
# Run individual test files
python -m tests.test_validation
python -m tests.test_edge_cases
python -m tests.test_game_continuation

# Run all tests with pytest (if available)
python -m pytest tests/
```

### Run Individual Modules
```bash
python -m src.player
python -m src.wheel
python -m src.table
```

## Benefits of New Structure

1. **Better Organization**: Clear separation between source code and tests
2. **Package Structure**: Proper Python package with `__init__.py`
3. **Scalability**: Easy to add new modules and tests
4. **Professional Layout**: Follows Python project best practices
5. **Import Clarity**: Relative imports within package, absolute imports from tests
6. **Maintainability**: Easier to navigate and maintain codebase

## Import Pattern

- **Within src package**: Use relative imports (e.g., `from .wheel import Color`)
- **From tests**: Use absolute imports (e.g., `from src.wheel import Color`)
- **Main entry point**: Import from src package (e.g., `from src.Rouletee import main`)
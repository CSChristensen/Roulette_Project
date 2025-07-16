# Technology Stack

## Language & Runtime
- **Python 3.x** - Core programming language
- Standard library only (no external dependencies)

## Key Libraries Used
- `enum` - For Color enumeration (RED, BLACK, GREEN)
- `random` - For wheel spinning simulation via `randint()`
- `typing` - For type hints (Tuple, etc.)

## Code Style & Conventions
- Class-based object-oriented design
- Type hints used for method parameters and return types
- Private attributes prefixed with underscore (`_balance`, `_ball_position`)
- Enum values use string literals for colors
- Method names use snake_case convention

## Common Commands
Since this is a structured Python project:

```bash
# Run the main game
python main.py

# Run the game directly from source
python -m src.Rouletee

# Run individual modules for testing
python -m src.player
python -m src.wheel
python -m src.table

# Run tests (when test framework is added)
python -m pytest tests/
python -m unittest discover tests/
```

## Development Notes
- Project uses pyproject.toml for configuration
- Source code organized in src/ package structure
- Test suite organized in tests/ directory
- Kiro specs and steering documentation in .kiro/
- Standard Python .gitignore in use
- Ready for test framework integration (pytest recommended)
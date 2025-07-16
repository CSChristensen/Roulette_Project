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
Since this is a pure Python project with no external dependencies:

```bash
# Run the main game
python Rouletee.py

# Run individual modules for testing
python -m player
python -m wheel
python -m table
```

## Development Notes
- No build system or package manager currently configured
- No testing framework set up
- No requirements.txt or setup.py present
- Standard Python .gitignore in use
# Design Document

## Overview

The number betting feature will extend the existing roulette game to support betting on specific numbers (0-36) in addition to the current color betting system. The design maintains the existing object-oriented architecture while adding new bet types and enhanced user interface options. Players will be able to place multiple bets of different types in a single round, with number bets paying 35:1 odds.

## Architecture

The existing architecture will be extended with minimal changes to maintain backward compatibility:
- **Player**: No changes needed - balance management remains the same
- **Bet**: Enhanced to support both color and number betting with unified payout logic
- **Table**: No changes needed - existing bet management works for both bet types
- **Wheel**: No changes needed - already provides both position and color information
- **GameController**: Enhanced to support bet type selection and number input validation

## Components and Interfaces

### Enhanced Components

#### Bet Class Enhancements
The current Bet class will be extended to support both color and number betting:

```python
class Bet:
    def __init__(self, amount: int, bet_type: str, bet_value: Union[Color, int], player: Player):
        self.amount = amount
        self.bet_type = bet_type  # "color" or "number"
        self.bet_value = bet_value  # Color enum or int (0-36)
        self.player = player
    
    def payout(self, winning_position: int, winning_color: Color) -> None:
        # Unified payout logic for both bet types
```

**Design Rationale**: Extending the existing Bet class maintains compatibility while adding new functionality. Using a union type for bet_value allows the same class to handle both color and number bets efficiently.

#### GameController Class Enhancements
The GameController will be enhanced with new methods for bet type selection and number validation:

```python
def get_bet_type(self) -> str:
    # Prompt user to choose between "color" and "number" betting
    
def validate_number_choice(self, choice: str) -> Optional[int]:
    # Validate number input (0-36)
    
def handle_betting_enhanced(self) -> bool:
    # Enhanced betting flow supporting multiple bet types
    
def handle_multiple_bets(self) -> bool:
    # Allow players to place multiple bets per round
```

**Design Rationale**: Adding new methods rather than modifying existing ones ensures backward compatibility and follows the single responsibility principle.

### New Enumerations

#### BetType Enumeration
```python
class BetType(Enum):
    COLOR = "color"
    NUMBER = "number"
```

**Design Rationale**: Using an enumeration provides type safety and makes the code more maintainable than using string literals.

## Data Models

### Enhanced Bet Data Model
```python
@dataclass
class BetInfo:
    amount: int
    bet_type: BetType
    bet_value: Union[Color, int]  # Color for color bets, int for number bets
    player: Player
```

### User Input Validation Extensions
- **Bet type validation**: Must be "color" or "number" (case-insensitive)
- **Number validation**: Must be integer between 0-36 inclusive
- **Multiple bet handling**: Support for placing additional bets in same round

### Game State Extensions
- **Active bet tracking**: List of all bets placed in current round
- **Bet type display**: Show different bet types and their odds
- **Enhanced result display**: Show outcomes for each individual bet

## Error Handling

### New Input Validation Errors
- **Invalid bet type**: Display available options and re-prompt
- **Invalid number choice**: Display valid range (0-36) and re-prompt
- **Mixed validation**: Handle edge cases where user switches between bet types

### Enhanced Game Logic
- **Bet processing**: Ensure both color and number bets are processed correctly
- **Payout calculation**: Verify correct odds are applied based on bet type
- **Multiple bet validation**: Ensure total bet amounts don't exceed balance

## Testing Strategy

### Unit Testing Extensions
- **Bet class testing**: Test both color and number bet creation and payout logic
- **Validation testing**: Test number input validation with edge cases (0, 36, invalid inputs)
- **Payout testing**: Verify correct odds calculation for number bets (35:1)

### Integration Testing
- **Mixed betting**: Test rounds with both color and number bets
- **Multiple bet processing**: Test multiple bets of same and different types
- **Balance management**: Test balance updates with various bet combinations

### User Experience Testing
- **Bet type selection**: Test user flow for choosing bet types
- **Number input**: Test various number input scenarios
- **Result display**: Verify clear display of multiple bet outcomes

## Implementation Approach

### Phase 1: Core Bet Enhancement
1. Extend Bet class to support both bet types
2. Add BetType enumeration
3. Update payout logic for unified processing

### Phase 2: User Interface Enhancement
1. Add bet type selection to GameController
2. Implement number validation
3. Update betting flow to support type selection

### Phase 3: Multiple Bet Support
1. Add support for placing multiple bets per round
2. Enhance result display for multiple bets
3. Update game flow to handle multiple bet scenarios

### Phase 4: Enhanced User Experience
1. Add comprehensive help and odds display
2. Improve error messages and user guidance
3. Add bet confirmation and summary features

## Backward Compatibility

The design ensures full backward compatibility:
- Existing color betting functionality remains unchanged
- Current game flow continues to work as before
- New features are additive, not replacing existing ones
- All existing tests should continue to pass

## Performance Considerations

- **Memory usage**: Minimal increase due to additional bet information
- **Processing time**: Negligible impact on game performance
- **User experience**: Enhanced options without complexity for basic users
from typing import Optional
from player import Player
from table import Table
from bet import Bet
from wheel import Color


class GameController:
    """Main game controller that manages the user interface and game flow."""
    
    def __init__(self):
        self.player: Optional[Player] = None
        self.table = Table()
    
    def display_welcome(self) -> None:
        """Display welcome message and game instructions."""
        print("=" * 50)
        print("Welcome to Roulette!")
        print("=" * 50)
        print("Game Rules:")
        print("- Red/Black bets pay 2:1 odds")
        print("- Green (0) bets pay 35:1 odds")
        print("- You can bet on Red, Black, or Green")
        print("- Good luck!")
        print("=" * 50)
    
    def display_message(self, message: str) -> None:
        """Display a message to the user."""
        print(message)
    
    def get_user_input(self, prompt: str) -> str:
        """Get input from the user with a prompt."""
        return input(prompt).strip()
    
    def validate_positive_integer(self, value: str) -> Optional[int]:
        """Validate that a string represents a positive integer.
        
        Returns:
            The integer value if valid, None otherwise.
        """
        try:
            num = int(value)
            if num > 0:
                return num
            return None
        except ValueError:
            return None
    
    def validate_color_choice(self, choice: str) -> Optional[Color]:
        """Validate color choice input.
        
        Returns:
            Color enum if valid, None otherwise.
        """
        choice_lower = choice.lower()
        if choice_lower == "red":
            return Color.RED
        elif choice_lower == "black":
            return Color.BLACK
        elif choice_lower == "green":
            return Color.GREEN
        return None
    
    def validate_yes_no(self, choice: str) -> Optional[bool]:
        """Validate yes/no input.
        
        Returns:
            True for yes, False for no, None for invalid input.
        """
        choice_lower = choice.lower()
        if choice_lower in ["y", "yes"]:
            return True
        elif choice_lower in ["n", "no"]:
            return False
        return None
    
    def setup_player(self) -> None:
        """Set up a new player with initial deposit."""
        while True:
            deposit_input = self.get_user_input("Enter your initial deposit amount: $")
            deposit_amount = self.validate_positive_integer(deposit_input)
            
            if deposit_amount is not None:
                self.player = Player(deposit_amount)
                self.display_message(f"Player created with balance: ${deposit_amount}")
                break
            else:
                self.display_message("Error: Please enter a valid positive number for your deposit.")
    
    def handle_additional_deposit(self) -> bool:
        """Handle additional deposit for existing player.
        
        Returns:
            True if deposit was made, False if player chose not to deposit.
        """
        while True:
            choice_input = self.get_user_input("Would you like to make an additional deposit? (y/n): ")
            choice = self.validate_yes_no(choice_input)
            
            if choice is True:
                while True:
                    deposit_input = self.get_user_input("Enter deposit amount: $")
                    deposit_amount = self.validate_positive_integer(deposit_input)
                    
                    if deposit_amount is not None:
                        self.player.add_to_balance(deposit_amount)
                        self.display_message(f"Deposit successful! New balance: ${self.player.get_balance()}")
                        return True
                    else:
                        self.display_message("Error: Please enter a valid positive number for your deposit.")
            elif choice is False:
                return False
            else:
                self.display_message("Error: Please enter 'y' for yes or 'n' for no.")
    
    def handle_betting(self) -> bool:
        """Handle the betting process for a round.
        
        Returns:
            True if bet was placed successfully, False if player has insufficient funds.
        """
        current_balance = self.player.get_balance()
        self.display_message(f"\nCurrent balance: ${current_balance}")
        
        if current_balance <= 0:
            self.display_message("You have no money left to bet!")
            return False
        
        # Get bet amount
        while True:
            bet_input = self.get_user_input("Enter your bet amount: $")
            bet_amount = self.validate_positive_integer(bet_input)
            
            if bet_amount is None:
                self.display_message("Error: Please enter a valid positive number for your bet.")
                continue
            
            if bet_amount > current_balance:
                self.display_message(f"Error: Bet amount (${bet_amount}) exceeds your balance (${current_balance}).")
                continue
            
            break
        
        # Get color choice
        while True:
            self.display_message("Choose a color to bet on:")
            self.display_message("- Red (pays 2:1)")
            self.display_message("- Black (pays 2:1)")
            self.display_message("- Green (pays 35:1)")
            
            color_input = self.get_user_input("Enter your color choice (red/black/green): ")
            color_choice = self.validate_color_choice(color_input)
            
            if color_choice is not None:
                break
            else:
                self.display_message("Error: Please enter 'red', 'black', or 'green'.")
        
        # Deduct bet amount from player balance and place bet
        try:
            self.player.subtract_from_balance(bet_amount)
            bet = Bet(bet_amount, color_choice, self.player)
            self.table.place_bet(bet)
            
            self.display_message(f"Bet placed: ${bet_amount} on {color_choice.value}")
            self.display_message(f"Remaining balance: ${self.player.get_balance()}")
            return True
            
        except ValueError as e:
            self.display_message(f"Error placing bet: {e}")
            return False
    
    def execute_round(self) -> None:
        """Execute a game round - spin wheel and process payouts."""
        self.display_message("\n" + "=" * 30)
        self.display_message("Spinning the wheel...")
        self.display_message("=" * 30)
        
        # Store balance before spin for payout calculation
        balance_before = self.player.get_balance()
        
        # Spin wheel and process payouts
        self.table.spin_wheel_and_payout()
        
        # Get winning position and color
        winning_position, winning_color = self.table.wheel.get_ball_position()
        
        # Display results
        self.display_message(f"The ball landed on: {winning_position} ({winning_color.value.upper()})")
        
        # Calculate and display payout results
        balance_after = self.player.get_balance()
        payout_amount = balance_after - balance_before
        
        if payout_amount > 0:
            self.display_message(f"🎉 Congratulations! You won ${payout_amount}!")
        else:
            self.display_message("😞 Sorry, you lost this round.")
        
        self.display_message(f"Your new balance: ${balance_after}")
        self.display_message("=" * 30)
    
    def should_continue_playing(self) -> bool:
        """Ask player if they want to continue playing.
        
        Returns:
            True if player wants to continue, False otherwise.
        """
        current_balance = self.player.get_balance()
        
        # Check if player has zero balance
        if current_balance <= 0:
            self.display_message("\nYou have no money left!")
            if self.handle_additional_deposit():
                return True
            else:
                self.display_message("Thanks for playing!")
                return False
        
        # Ask if player wants to continue
        while True:
            choice_input = self.get_user_input("\nWould you like to play another round? (y/n): ")
            choice = self.validate_yes_no(choice_input)
            
            if choice is True:
                return True
            elif choice is False:
                self.display_final_balance()
                return False
            else:
                self.display_message("Error: Please enter 'y' for yes or 'n' for no.")
    
    def display_final_balance(self) -> None:
        """Display final balance and goodbye message."""
        final_balance = self.player.get_balance()
        self.display_message("\n" + "=" * 40)
        self.display_message("Thanks for playing Roulette!")
        self.display_message(f"Your final balance: ${final_balance}")
        self.display_message("=" * 40)
    
    def run_game(self) -> None:
        """Main game loop that orchestrates the entire game."""
        # Display welcome and set up player
        self.display_welcome()
        self.setup_player()
        
        # Main game loop
        while True:
            # Handle betting
            if not self.handle_betting():
                # If betting failed due to insufficient funds, offer deposit or quit
                if not self.handle_additional_deposit():
                    self.display_final_balance()
                    break
                continue
            
            # Execute the round
            self.execute_round()
            
            # Check if player wants to continue
            if not self.should_continue_playing():
                break
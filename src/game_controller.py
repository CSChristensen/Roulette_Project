from typing import Optional
from .player import Player
from .table import Table
from .bet import Bet, BetType
from .wheel import Color


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
        print()
        print("COLOR BETTING:")
        print("- Red/Black bets pay 2:1 odds")
        print("- Green (0) bets pay 35:1 odds")
        print()
        print("NUMBER BETTING:")
        print("- Bet on specific numbers (0-36)")
        print("- All number bets pay 35:1 odds")
        print()
        print("You can choose between color or number betting each round.")
        print("Good luck!")
        print("=" * 50)

    def display_message(self, message: str) -> None:
        """Display a message to the user."""
        print(message)

    def get_user_input(self, prompt: str) -> str:
        """Get input from the user with a prompt."""
        return input(prompt).strip()

    def validate_positive_integer(
        self, value: str, field_name: str = "value"
    ) -> Optional[int]:
        """Validate that a string represents a positive integer.

        Args:
            value: The string to validate
            field_name: Name of the field for error messages

        Returns:
            The integer value if valid, None otherwise.
        """
        if not value:
            self.display_message(f"Error: {field_name} cannot be empty.")
            return None

        try:
            # Handle potential whitespace and check for non-numeric characters
            cleaned_value = value.strip()
            if not cleaned_value:
                self.display_message(f"Error: {field_name} cannot be empty.")
                return None

            # Check for decimal points or other non-integer characters
            if "." in cleaned_value or "," in cleaned_value:
                self.display_message(
                    f"Error: {field_name} must be a whole number (no decimals)."
                )
                return None

            num = int(cleaned_value)
            if num <= 0:
                self.display_message(f"Error: {field_name} must be greater than 0.")
                return None

            # Check for extremely large numbers that might cause issues
            if num > 1000000:  # 1 million limit
                self.display_message(
                    f"Error: {field_name} is too large. Maximum allowed is $1,000,000."
                )
                return None

            return num
        except ValueError:
            self.display_message(
                f"Error: '{value}' is not a valid number. Please enter a positive whole number."
            )
            return None

    def validate_number_choice(self, choice: str) -> Optional[int]:
        """Validate number choice input for number betting.

        Args:
            choice: The number choice string to validate

        Returns:
            Integer between 0-36 if valid, None otherwise.
        """
        if not choice:
            self.display_message("Error: Number choice cannot be empty.")
            return None

        choice_cleaned = choice.strip()
        if not choice_cleaned:
            self.display_message("Error: Number choice cannot be empty.")
            return None

        try:
            # Check for decimal points or other non-integer characters
            if "." in choice_cleaned or "," in choice_cleaned:
                self.display_message(
                    "Error: Number must be a whole number (no decimals)."
                )
                return None

            num = int(choice_cleaned)
            
            # Validate range (0-36 inclusive)
            if num < 0 or num > 36:
                self.display_message(
                    f"Error: '{num}' is not a valid number choice. Please enter a number between 0 and 36."
                )
                return None

            return num
        except ValueError:
            self.display_message(
                f"Error: '{choice}' is not a valid number. Please enter a whole number between 0 and 36."
            )
            return None

    def validate_color_choice(self, choice: str) -> Optional[Color]:
        """Validate color choice input with case-insensitive matching.

        Args:
            choice: The color choice string to validate

        Returns:
            Color enum if valid, None otherwise.
        """
        if not choice:
            self.display_message("Error: Color choice cannot be empty.")
            return None

        choice_cleaned = choice.strip().lower()
        if not choice_cleaned:
            self.display_message("Error: Color choice cannot be empty.")
            return None

        # Support multiple variations and abbreviations
        if choice_cleaned in ["red", "r"]:
            return Color.RED
        elif choice_cleaned in ["black", "b"]:
            return Color.BLACK
        elif choice_cleaned in ["green", "g", "0"]:
            return Color.GREEN
        else:
            self.display_message(f"Error: '{choice}' is not a valid color choice.")
            self.display_message(
                "Valid options: 'red' (or 'r'), 'black' (or 'b'), 'green' (or 'g')"
            )
            return None

    def get_bet_type(self) -> Optional[BetType]:
        """Prompt user to choose bet type and validate input.

        Returns:
            BetType enum if valid, None for invalid input.
        """
        self.display_message("\nChoose your bet type:")
        self.display_message("- Color betting: Bet on Red, Black, or Green")
        self.display_message("  • Red/Black pay 2:1 odds")
        self.display_message("  • Green pays 35:1 odds")
        self.display_message("- Number betting: Bet on specific numbers (0-36)")
        self.display_message("  • All numbers pay 35:1 odds")
        
        bet_type_input = self.get_user_input("Enter bet type (color/number): ")
        
        if not bet_type_input:
            self.display_message("Error: Bet type cannot be empty.")
            return None

        bet_type_cleaned = bet_type_input.strip().lower()
        if not bet_type_cleaned:
            self.display_message("Error: Bet type cannot be empty.")
            return None

        if bet_type_cleaned in ["color", "c"]:
            return BetType.COLOR
        elif bet_type_cleaned in ["number", "num", "n"]:
            return BetType.NUMBER
        else:
            self.display_message(f"Error: '{bet_type_input}' is not a valid bet type.")
            self.display_message("Valid options: 'color' (or 'c'), 'number' (or 'n')")
            return None

    def validate_yes_no(self, choice: str) -> Optional[bool]:
        """Validate yes/no input with case-insensitive matching.

        Args:
            choice: The yes/no choice string to validate

        Returns:
            True for yes, False for no, None for invalid input.
        """
        if not choice:
            self.display_message("Error: Please enter a response.")
            return None

        choice_cleaned = choice.strip().lower()
        if not choice_cleaned:
            self.display_message("Error: Please enter a response.")
            return None

        # Support multiple variations
        if choice_cleaned in ["y", "yes", "yeah", "yep", "1", "true"]:
            return True
        elif choice_cleaned in ["n", "no", "nope", "0", "false"]:
            return False
        else:
            self.display_message(f"Error: '{choice}' is not a valid response.")
            self.display_message("Please enter 'y' for yes or 'n' for no.")
            return None

    def setup_player(self) -> None:
        """Set up a new player with initial deposit."""
        while True:
            deposit_input = self.get_user_input("Enter your initial deposit amount: $")
            deposit_amount = self.validate_positive_integer(
                deposit_input, "deposit amount"
            )

            if deposit_amount is not None:
                self.player = Player(deposit_amount)
                self.display_message(f"Player created with balance: ${deposit_amount}")
                break

    def handle_additional_deposit(self) -> bool:
        """Handle additional deposit for existing player.

        Returns:
            True if deposit was made, False if player chose not to deposit.
        """
        while True:
            choice_input = self.get_user_input(
                "Would you like to make an additional deposit? (y/n): "
            )
            choice = self.validate_yes_no(choice_input)

            if choice is True:
                while True:
                    deposit_input = self.get_user_input("Enter deposit amount: $")
                    deposit_amount = self.validate_positive_integer(
                        deposit_input, "deposit amount"
                    )

                    if deposit_amount is not None:
                        self.player.add_to_balance(deposit_amount)
                        self.display_message(
                            f"Deposit successful! New balance: ${self.player.get_balance()}"
                        )
                        return True
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
            bet_amount = self.validate_positive_integer(bet_input, "bet amount")

            if bet_amount is None:
                continue

            if bet_amount > current_balance:
                self.display_message(
                    f"Error: Bet amount (${bet_amount}) exceeds your balance (${current_balance})."
                )
                continue

            # Handle exact balance bet scenario
            if bet_amount == current_balance:
                self.handle_exact_balance_bet(current_balance)
                # Ask again if they want to proceed with this amount
                confirm_input = self.get_user_input(
                    f"Confirm bet of ${bet_amount} (your entire balance)? (y/n): "
                )
                confirm = self.validate_yes_no(confirm_input)
                if confirm is False:
                    continue  # Ask for bet amount again
                elif confirm is None:
                    continue  # Invalid input, ask again

            break

        # Get color choice
        while True:
            self.display_message("Choose a color to bet on:")
            self.display_message("- Red (pays 2:1)")
            self.display_message("- Black (pays 2:1)")
            self.display_message("- Green (pays 35:1)")

            color_input = self.get_user_input(
                "Enter your color choice (red/black/green): "
            )
            color_choice = self.validate_color_choice(color_input)

            if color_choice is not None:
                break

        # Deduct bet amount from player balance and place bet
        try:
            # Double-check balance before deducting (edge case protection)
            if bet_amount > self.player.get_balance():
                self.display_message(
                    "Error: Balance changed unexpectedly. Please try again."
                )
                return False

            self.player.subtract_from_balance(bet_amount)
            bet = Bet(bet_amount, color_choice, self.player)
            self.table.place_bet(bet)

            self.display_message(f"Bet placed: ${bet_amount} on {color_choice.value}")
            self.display_message(f"Remaining balance: ${self.player.get_balance()}")
            return True

        except ValueError as e:
            self.display_message(f"Error placing bet: {e}")
            # Restore balance if bet placement failed after deduction
            try:
                self.player.add_to_balance(bet_amount)
                self.display_message("Bet amount has been refunded to your balance.")
            except:
                self.display_message(
                    "Warning: There may be an issue with your balance. Please check."
                )
            return False
        except Exception as e:
            self.display_message(f"Unexpected error placing bet: {e}")
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
        self.display_message(
            f"The ball landed on: {winning_position} ({winning_color.value.upper()})"
        )

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
            choice_input = self.get_user_input(
                "\nWould you like to play another round? (y/n): "
            )
            choice = self.validate_yes_no(choice_input)

            if choice is True:
                return True
            elif choice is False:
                self.display_final_balance()
                return False
            else:
                self.display_message("Error: Please enter 'y' for yes or 'n' for no.")

    def check_minimum_bet_capability(self) -> bool:
        """Check if player has enough balance for minimum bet ($1).

        Returns:
            True if player can make minimum bet, False otherwise.
        """
        return self.player.get_balance() >= 1

    def handle_zero_balance_scenario(self) -> bool:
        """Handle scenario when player balance becomes zero.

        Returns:
            True if player made deposit and can continue, False if quitting.
        """
        self.display_message("\n⚠️  Your balance is now $0!")
        self.display_message("You need money to continue playing.")

        while True:
            choice_input = self.get_user_input(
                "Would you like to make a deposit to continue? (y/n): "
            )
            choice = self.validate_yes_no(choice_input)

            if choice is True:
                return self.handle_additional_deposit()
            elif choice is False:
                self.display_message("Thanks for playing!")
                return False

    def handle_exact_balance_bet(self, current_balance: int) -> None:
        """Handle case where player wants to bet their exact balance.

        Args:
            current_balance: Player's current balance
        """
        self.display_message(f"\n💡 Note: You have exactly ${current_balance}.")
        self.display_message("If you bet all of it and lose, your balance will be $0.")

        while True:
            choice_input = self.get_user_input(
                "Are you sure you want to bet your entire balance? (y/n): "
            )
            choice = self.validate_yes_no(choice_input)

            if choice is not None:
                if choice is False:
                    self.display_message("Wise choice! You can bet a smaller amount.")
                return

    def display_final_balance(self) -> None:
        """Display final balance and goodbye message."""
        final_balance = self.player.get_balance()
        self.display_message("\n" + "=" * 40)
        self.display_message("Thanks for playing Roulette!")
        self.display_message(f"Your final balance: ${final_balance}")
        if final_balance > 0:
            self.display_message("🎉 You're leaving with money! Well done!")
        else:
            self.display_message("💸 Better luck next time!")
        self.display_message("=" * 40)

    def run_game(self) -> None:
        """Main game loop that orchestrates the entire game with comprehensive error handling."""
        try:
            # Display welcome and set up player
            self.display_welcome()
            self.setup_player()

            # Main game loop
            while True:
                # Check if player can make minimum bet before attempting to bet
                if not self.check_minimum_bet_capability():
                    if not self.handle_zero_balance_scenario():
                        self.display_final_balance()
                        break
                    continue

                # Handle betting
                try:
                    if not self.handle_betting():
                        # If betting failed due to insufficient funds, offer deposit or quit
                        if not self.handle_additional_deposit():
                            self.display_final_balance()
                            break
                        continue
                except Exception as e:
                    self.display_message(f"An error occurred during betting: {e}")
                    self.display_message("Please try again.")
                    continue

                # Execute the round
                try:
                    self.execute_round()
                except Exception as e:
                    self.display_message(
                        f"An error occurred during the game round: {e}"
                    )
                    self.display_message(
                        "The round will be skipped, but your bet has been processed."
                    )
                    continue

                # Check if player wants to continue
                try:
                    if not self.should_continue_playing():
                        break
                except Exception as e:
                    self.display_message(f"An error occurred: {e}")
                    self.display_message("Ending game for safety.")
                    self.display_final_balance()
                    break

        except KeyboardInterrupt:
            self.display_message("\n\nGame interrupted by user.")
            if self.player:
                self.display_final_balance()
        except Exception as e:
            self.display_message(f"\nAn unexpected error occurred: {e}")
            self.display_message("Game will now exit.")
            if self.player:
                self.display_final_balance()

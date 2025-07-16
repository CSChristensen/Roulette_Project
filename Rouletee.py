from game_controller import GameController


def main():
    """Main entry point for the roulette game."""
    try:
        game = GameController()
        game.run_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try running the game again.")


if __name__ == "__main__":
    main()

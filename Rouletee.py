from table import Table
from player import Player
from bet import Bet
from wheel import Color


def main():
    table = Table()
    player_1 = Player(1000)
    player_2 = Player(2000)
    bet_1 = Bet(100, Color.RED, player_1)
    bet_2 = Bet(100, Color.GREEN, player_2)
    table.place_bet(bet_1)
    table.place_bet(bet_2)

    table.spin_wheel()
    print(table.wheel.get_ball_position)


if __name__ == "__main__":
    main()

    # def deposit():
    # amount = input("what is your deposit")
    # if amount.isdigit():

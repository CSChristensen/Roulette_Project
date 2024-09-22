from wheel import Wheel


class Table:

    def __init__(self):
        self.bets = []
        self.wheel = Wheel()

    def spin_wheel_and_payout(self):
        self.wheel.spin()
        self._payout_bets()

    def _payout_bets(self):
        for bet in self.bets:
            bet.payout()
        self.bets = []

    def place_bet(self, bet):
        self.bets.append(bet)

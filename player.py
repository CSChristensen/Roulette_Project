class Player:

    def __init__(self, balance):
        self._balance = balance

    def subract_from_balance(self, amount):
        self._balance = self._balance - amount

    def add_to_balance(self, amount):
        self._balance = self._balance + amount

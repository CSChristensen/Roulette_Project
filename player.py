class Player:

    def __init__(self, balance):
        self._balance = balance

    def subtract_from_balance(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance = self._balance - amount

    def add_to_balance(self, amount):
        self._balance = self._balance + amount

    def get_balance(self):
        return self._balance

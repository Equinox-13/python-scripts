
class InsufficientBalance(Exception):
    """
    Insufficient Balance exception
    """
    pass


class Wallet:

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount_to_spend):
        if self.balance < amount_to_spend:
            raise InsufficientBalance(f"Not enough balance available to spend {amount_to_spend}.")
        self.balance = self.balance - amount_to_spend

    def add_cash(self, amount):
        self.balance = self.balance + amount

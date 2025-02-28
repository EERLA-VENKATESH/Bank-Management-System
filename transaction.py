class Transaction:
    def execute(self, customer, amount):
        pass  # Abstract method

class Deposit(Transaction):
    def execute(self, customer, amount):
        return customer.deposit(amount)

class Withdraw(Transaction):
    def execute(self, customer, amount):
        return customer.withdraw(amount)

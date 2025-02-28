class Customer:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance  # Encapsulated balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ₹{amount}. New Balance: ₹{self.__balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ₹{amount}. New Balance: ₹{self.__balance}"
        return "Insufficient balance or invalid amount!"

    def get_balance(self):
        return self.__balance

    def get_account_details(self):
        return f"Account Holder: {self.name}, Account Number: {self.account_number}, Balance: ₹{self.__balance}"
